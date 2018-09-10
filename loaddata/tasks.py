# -*- encoding: utf-8 -*-
from __future__ import absolute_import
import datetime
from django.core.mail import send_mail, EmailMessage
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from appcc.models      import DetallesRegistros, DetalleConfiguracion
from pyjasperclient    import JasperClient
from loaddata.models   import TrackSondasAlarmas
from maestros.models   import HorarioTurnos, Personal
from notificaciones.management.commands.notificaciones import Command
from siva.celery import app

import logging
from siva.settings import USUARIO_JASPER, SERVER_URL_REPORTS, PASSWD_JASPER

logger = logging.getLogger(__name__)

def normalizadias(dias):
    DIAS =dias
    if dias == 'L':
            DIAS = [0, 1, 2, 3, 4]
    elif dias == 'F':
            DIAS = [5, 6]
    elif dias == 'A':
            DIAS = [0, 1, 2, 3, 4, 5, 6]
    else:
            DIAS = [dias]
    return DIAS


@periodic_task(run_every=(crontab(hour="05", minute="00", day_of_week="*")))
def asyncLoadDataSensor():
    logger.debug("Inicia tarea de calculo")
    tareas= Command()
    tareas.loadSensor()


#Envio de Graficas de sondas de temperaturas.
@periodic_task(run_every=(crontab(hour="07", minute="00", day_of_week="*")))
def enviosGraficas():
    logger.debug("Inicia tarea de envio de graficas de los sensores de temperatura")
    nombrereport = '/siva/sensores/graph_temp_alone'
    j = JasperClient(SERVER_URL_REPORTS,USUARIO_JASPER,PASSWD_JASPER)
    diasemana = datetime.datetime.now().weekday()
    listobjreg  = DetallesRegistros.objects.filter(tracksondas__isnull=False)

    for obj in listobjreg:
        #Generamos primero la grafica y comprobamos su existencia
        idtrack= obj.tracksondas.id
        referencia = obj.tracksondas.Name
        print "Id Track %s Referencia %s Nombre reportes %s" % (idtrack,referencia,nombrereport)
        ret = j.runReport(nombrereport,"PDF",params={"tracksid": str(idtrack)})
        attach =ret['data']
        if attach is not None:
            listaenvios = DetalleConfiguracion.objects.filter(configuracion__empresa__id=obj.empresa.id, habilitar='S')
            for envio in listaenvios:
                DIA = normalizadias(envio.dias)
                if diasemana in  DIA:
                    listapersonas = Personal.objects.filter(detalleconfiguracion__id=envio.id,emailnotifica__isnull=False)
                    if listapersonas != []:
                        email = []
                        for direccion in listapersonas:  #Listas Personas
                            if envio.accion in ('T','Z','A'):
                             if direccion.emailnotifica is not None:
                                email.append(direccion.emailnotifica)

                        from_email= "incidencias@givasl.com"
                        titulo = obj.denominacion()
                        subject = "Grafica de seguimiento de temperatura de la instalacion %s" % referencia
                        html_content="""<h1> ENVIO AUTOMATIZADO, NO RESPONDER </h1> <p>  <b>
                        Este correo electrónico contiene información legal confidencial y privilegiada. Si Usted no es el destinatario a quien se desea enviar este mensaje, tendrá prohibido darlo a conocer a persona alguna, así como a reproducirlo o copiarlo. Si recibe este mensaje por error, favor de notificarlo al remitente de inmediato y desecharlo de su sistema. </b>
                         </p>"""
                        msg = EmailMessage(subject, html_content, from_email, email)
                        hoy=datetime.datetime.now()
                        msg.content_subtype = "html"  # Main content is now text/html
                        msg.attach('grafica_%s_%s.pdf' % (referencia.replace(' ',''),hoy), attach, 'application/pdf')
                        msg.send()

                        logger.debug( "Envia email a %s " % email)




#Aviso de alarmas de sondas de temperatura.
@app.task
def enviosdelegados(listaenvios,temp,objreg,sondalarm,hora,diasemana,tantes,consigna,hoy):
    import textmagic.client
    logger.debug("Imprime informacion de sonda alarm  %s " % sondalarm)
    logger.debug("Lista de envios %s " % listaenvios )
    remitente='incidencias@givasl.com'
    client = textmagic.client.TextMagicClient('infinityloopsis', 'uTM0EwZF026AQCN')
    for envio  in listaenvios: #Listas parametros envios
        logger.debug("Envios  %s %s " % (envio.dias,envio.turnos))
        DIAS = normalizadias(envio.dias)
        if DIAS:
            if diasemana in DIAS:  # Comprueba que estamos en el dia de alarma
                listaturnos = HorarioTurnos.objects.filter(tpturnos=envio.turnos)
                if listaturnos:
                    for objturno in listaturnos:  #Recorre Turnos
                        horavalida = (objturno.fhora >= hora and objturno.ihora <= hora)  #Verifica que se encuentra en hora de aviso
                else:
                    #Sin horario, por defecto todas las horas son validas
                    horavalida = True

                if horavalida:
                    no_avisos = TrackSondasAlarmas.objects.filter(tracksonda_id=objreg.tracksondas.id,
                                                                  dateaviso__gte=tantes).count()
                    logger.debug("Cuenta no de aviso %s" % no_avisos)
                    if no_avisos is None:
                        TrackSondasAlarmas.objects.create(**sondalarm)
                    elif no_avisos in (13, 21, 34):
                        listapersonas = Personal.objects.filter(detalleconfiguracion__id=envio.id,
                                                                emailnotifica__isnull=False, telefonosms__isnull=False)
                        if listapersonas != []:
                            email = []
                            titulo = objreg.denominacion()
                            mensaje = "Alarma %s excede valor %s, valor actual ** %s ** " % (
                            titulo, consigna, temp['Temperature__avg'])
                            for direccion in listapersonas:  #Listas Personas
                                if envio.accion == 'S' or envio.accion == 'Z':
                                    result = client.send(unicode(mensaje, 'utf8'), direccion.telefonosms)
                                    messager_id = result['message_id'].keys()[0]
                                    logger.debug( "Envia Mensajes %s" % mensaje)
                                    objtrack = TrackSondasAlarmas.objects.filter(tracksonda_id=objreg.tracksondas.id,
                                                                                 dateaviso__gte=tantes,
                                                                                 idavisosms__isnull=True).update(idavisosms=messager_id)
                                if envio.accion == 'Z':
                                    email.append(direccion.emailnotifica)

                            if envio.accion == 'Z':
                                send_mail("Urgente - Alarmas de fecha %s" % hoy, mensaje, remitente, email)
                                logger.debug( "Envia email a %s " % email)
                            TrackSondasAlarmas.objects.create(**sondalarm)
                    else:
                        TrackSondasAlarmas.objects.create(**sondalarm)
                        logger.debug(sondalarm)