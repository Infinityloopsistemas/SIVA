# -*- coding: utf-8 -*-
from base64 import decode, encode
import datetime
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.db import connection
from appcc.models import DetallesRegistros, GestorIncidencias, CuadrosGestion, DetalleConfiguracion, APPCC, Registros
from loaddata.models import TrackSondasAlarmas
from maestros.models import Personal, HorarioTurnos,ExcepcionesCalendario
from maestros_generales.models import Empresas
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail, send_mass_mail
from siva import settings
from django.db import IntegrityError
from siva.utils import enviaTemperaturasSensor

__author__ = 'julian'




class Command(BaseCommand):



    def revisarRegistros(self,emp,diastolerar):
        user     =  User.objects.filter(empresas__id=emp.id)[0]
        pappccid =  APPCC.objects.filter(empresa_id=emp.id)[0].id
        hoy      = datetime.datetime.now().date() + datetime.timedelta(days =-diastolerar)
        #Filtra excepciones de calendario.
        excepcion = ExcepcionesCalendario.objects.filter(empresa_id=emp.id,fecha_inicio__lt=hoy ,fecha_final__gt=hoy)
        if not excepcion:
            pfecha   = str(hoy.year)+str(hoy.month).zfill(2)+str(hoy.day).zfill(2)
            sql = """ call siva.reportagenda(%s,%s) """ % (pappccid,pfecha)
            cur  = connection.cursor()
            cur.execute(sql)
            allReg = cur.fetchall()
            cur.close()
            for reg in allReg:
                print reg
                if reg[5] is None:
                    detreg= DetallesRegistros.objects.get(id=reg[3])
                    etapa=None
                    try:
                        etapa = CuadrosGestion.objects.get(registros=detreg.cabreg).etapa
                    except CuadrosGestion.DoesNotExist:
                        etapa = None
                    except CuadrosGestion.MultipleObjectsReturned:
                        etapa = None

                    if etapa is not None:
                        print "Crea Incidencia"
                        gincidencias=GestorIncidencias(appcc   = detreg.cabreg.manautctrl.appcc,
                                             fincidencia   = datetime.datetime.now().date(),
                                             estado        = "C",
                                             denominacion  = detreg.actividades,
                                             equipo        = detreg.equipos,
                                             zonas         = detreg.zonas,
                                             tpmedactc     = detreg.cabreg.tpmedactc,
                                             tipogenera    = "A",
                                             etapa         = etapa,
                                             observaciones =  _("Registro de fecha %s sin completar execede el tiempo de toma de datos ") % reg[0]  )
                        gincidencias.save(user=user.username)



    #Copntrol de incidencias
    def inicioPoll(self):
        listaempresas = Empresas.objects.filter(habilitar=True)
        for empre in listaempresas:
            self.revisarRegistros(empre,settings.DIAS_NOTIFICACION)


    def envioMail(self):
        remitente='incidencias@givasl.com'
        hoy = datetime.datetime.today().date()
        listaempresas = Empresas.objects.filter(habilitar=True,fechabaja__isnull=True)
        for emp in listaempresas:
            mensajes =""
            listaincidencias  =  GestorIncidencias.objects.filter(empresa=emp,fincidencia=hoy).exclude(estado='S')
            if len(listaincidencias) != 0:
                for inci in listaincidencias:
                    mensajes_actual = "Incidencia registrada: Dia %s \n Denominada: %s  \n Zona: %s \n Equipo: %s \n Observacion: %s \n --------------------------------------" % ( inci.fincidencia,inci.denominacion,inci.zonas,inci.equipo,inci.observaciones )
                    mensajes = mensajes+"\n"+mensajes_actual

                listaenvios = DetalleConfiguracion.objects.filter(configuracion__empresa__id=emp.id,habilitar='S')
                for envio in listaenvios:
                    subject  = "Gestor incidencias SIVA Empresa: %s" % emp.descripcion
                    email=[]
                    listapersonas  =  Personal.objects.filter(detalleconfiguracion__id=envio.id, emailnotifica__isnull=False , emailnotifica__contains='@')
                    if len(listapersonas) != 0:
                        for direccion in listapersonas:
                            email.append(direccion.emailnotifica)
                        send_mail(subject,mensajes,remitente,email)


    def envioSMS(self):
        import textmagic.client
        remitente='siva@infinityloop.es'
        fecha    = datetime.datetime.now()
        #- datetime.timedelta(days=5,hours=3) #el delta para testar
        tantes   = (fecha - datetime.timedelta(hours=4))
        client = textmagic.client.TextMagicClient('infinityloopsis', 'uTM0EwZF026AQCN')
        hoy      = fecha
        diasemana=  hoy.weekday()
        hora  = hoy.now()
        listaempresas = Empresas.objects.filter(habilitar=True,fechabaja__isnull=True)
        print listaempresas.count()
        for emp in listaempresas:
            listobjreg = DetallesRegistros.objects.filter(tracksondas__isnull=False,empresa_id=emp.id)
            if listobjreg:
                for objreg in listobjreg: #Detalle Registros
                    #Conseguir consignas de limites.
                    consigna= objreg.tplimitcrit.valormax
                    #Revision temperatura rango
                    temp = objreg.tracksondas.tempMin(fecha,15)
                    sondalarm ={'tracksonda_id': objreg.tracksondas.id ,'dateaviso' : fecha, 'valor': temp['Temperature__avg'], }
                    if temp['Temperature__avg'] is not None:
                        if temp['Temperature__avg']>consigna:
                            listaenvios = DetalleConfiguracion.objects.filter(configuracion__empresa__id=emp.id,habilitar='S',accion__in=('S','Z'))
                            for envio  in listaenvios: #Listas parametros envios
                                if envio.dias =='L':
                                    DIAS =[0,1,2,3,4]
                                elif envio.dias =='F':
                                    DIAS=[5,6]
                                elif envio.dias =='A':
                                    DIAS=[0,1,2,3,4,5,6]
                                else:
                                    DIAS=[envio.dias]
                                if DIAS:
                                    if diasemana in DIAS: #Comprueba que estamos en el dia de alarma
                                        listaturnos = HorarioTurnos.objects.filter(tpturnos=envio.turnos)
                                        if listaturnos:
                                            for objturno in listaturnos: #Recorre Turnos
                                                horavalida = (objturno.fhora>=hora and objturno.ihora <= hora) #Verifica que se encuentra en hora de aviso
                                        else:
                                            #Sin horario, por defecto todas las horas son validas
                                            horavalida= True

                                        if horavalida:
                                            no_avisos = TrackSondasAlarmas.objects.filter(tracksonda_id = objreg.tracksondas.id, dateaviso__gte=tantes ).count()
                                            if no_avisos is None:
                                                TrackSondasAlarmas.objects.create(**sondalarm)
                                            elif no_avisos in (13,21,34):
                                                listapersonas  =  Personal.objects.filter(detalleconfiguracion__id=envio.id, emailnotifica__isnull=False, telefonosms__isnull=False )
                                                if listapersonas !=[]:
                                                    email=[]
                                                    titulo= objreg.denominacion()
                                                    mensaje ="Alarma %s excede valor %s, valor actual ** %s ** " % (titulo,consigna, temp['Temperature__avg'])
                                                    for direccion in listapersonas: #Listas Personas
                                                        if envio.accion=='S' or envio.accion=='Z':
                                                            result = client.send(unicode(mensaje,'utf8') , direccion.telefonosms)
                                                            messager_id = result['message_id'].keys()[0]
                                                            print "Envia Mensajes %s" % mensaje
                                                            objtrack= TrackSondasAlarmas.objects.filter(tracksonda_id = objreg.tracksondas.id, dateaviso__gte=tantes,idavisosms__isnull=True ).update(idavisosms=messager_id)

                                                        if envio.accion=='Z':
                                                            email.append(direccion.emailnotifica)
                                                    if envio.accion=='Z':
                                                        send_mail("Urgente - Alarmas de fecha %s" % hoy ,mensaje,remitente,email)
                                                    TrackSondasAlarmas.objects.create(**sondalarm)
                                            else:
                                                TrackSondasAlarmas.objects.create(**sondalarm)


    def loadSensor(self):
        #Graba media de temperatura diaria sobre el registro
        #Envia grafica por correo electronico
        fecha = datetime.datetime.now()-datetime.timedelta(days= 1)
        dia   = int(fecha.day)
        mes   = int(fecha.month)
        ano   = int(fecha.year)
        objdetreg = DetallesRegistros.objects.filter(tracksondas__isnull=False)
        if len(objdetreg)!=0:
            for detrreg in objdetreg:
                temp = detrreg.tracksondas.tempDia(dia,mes,ano)
                if temp['Temperature__avg'] is not None:
                    regtemp ={'detreg_id': detrreg.id ,'fechadesde' : fecha, 'fechahasta': fecha, 'valor': temp['Temperature__avg'] ,'estado': 1 }
                    try:
                        Registros.objects.create(**regtemp)
                        print regtemp
                    except IntegrityError as error:
                        print "Error en loadSensor %s " % error


    #Recalcula tenperatura de los registros de un sensor desde un determinado numero de dias.
    def recalculaloadSensor(selfs):
        NUMERODIAS=3 #CAMBIAR
        #Graba media de temperatura diaria sobre el registro
        #Envia grafica por correo electronico
        for dias in range(NUMERODIAS,0,-1):
            fecha = datetime.datetime.now()-datetime.timedelta(days= dias)
            print fecha
            dia   = int(fecha.day)
            mes   = int(fecha.month)
            ano   = int(fecha.year)
            objdetreg = DetallesRegistros.objects.filter(tracksondas__isnull=False)
            print objdetreg
            if len(objdetreg)!=0:
                for detrreg in objdetreg:
                    temp = detrreg.tracksondas.tempDia(dia,mes,ano)
                    print temp
                    if temp['Temperature__avg'] is not None:
                        regtemp ={'detreg_id': detrreg.id ,'fechadesde' : fecha, 'fechahasta': fecha, 'valor': temp['Temperature__avg'],'estado':1  }
                        try:
                            print regtemp
                            Registros.objects.create(**regtemp)
                        except IntegrityError as error:
                            print "Error en loadSensor %s " % error




    option_list = BaseCommand.option_list + (
            make_option('--incidencias',
                action='store_true',
                dest='incidencias',
                default=False,
                help='Estado de las incidencias'),
            make_option('--comunica',
                action='store_true',
                dest='comunica',
                default=False,
                help='Comunica'),
             make_option('--sensor',
                action='store_true',
                dest='sensor',
                default=False,
                help='Carga de informacion Sensor'),
             make_option('--alarmas',
                action='store_true',
                dest='alarmas',
                default=False,
                help='Alarmas de comprobancion'),
             make_option('--recalcula',
                action='store_true',
                dest='recalcula',
                default=False,
                help='ReCarga de informacion Sensor'),


            )

    def handle(self, *args, **options):
        if options['incidencias']:
           self.inicioPoll()
        if options['comunica']:
            self.envioMail()
        if options['sensor']:
            self.loadSensor()
        if options['alarmas']:
            self.envioSMS()
        if options['recalcula']:
            self.recalculaloadSensor()
