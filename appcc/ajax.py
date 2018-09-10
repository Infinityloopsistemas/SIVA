# -*- coding: utf-8 -*-
from dateutil.rrule import rruleset, DAILY, rrule, YEARLY, HOURLY, WEEKLY, MONTHLY
from decimal import Decimal
import simplejson
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
import datetime
from dajaxice.utils import deserialize_form
from django.contrib.auth.models import User
from django.db import connection
from django.shortcuts import get_object_or_404
from appcc.forms import RegistrosRapidosForms
from django.utils.translation import gettext_lazy as _
from appcc.models import DetallesRegistros, CabRegistros, Registros, GestorIncidencias, CuadrosGestion, APPCC, ValoresAnaliticas, CabAnaliticas
from maestros.models import ParametrosAnalisis, TiposTurnos, HorarioTurnos, Firmas,ExcepcionesCalendario
from maestros_generales.models import Empresas, Festivos
from dateutil.relativedelta import *
from siva.utils import JsonCuadrosGestion, JSONEncoder, HORA, colorHexRamdom, tiempoenMil


__author__ = 'julian'





def mensajes_error(dajax,titulo,mensaje):
    dajax.assign('#titulo', 'innerHTML', '<span> %s </span' % titulo )
    dajax.assign('#cuerpo', 'innerHTML', '<span> %s </span' % mensaje )
    dajax.script(" $('#mensajeserror').modal('toggle').css({'width': '500px','margin-left': function () {return -($(this).width() / 2);}})")

def mensajes_validacion(dajax,titulo,mensaje):
    dajax.assign('#id_dialogo_titulo', 'innerHTML', '<span> %s </span' % titulo )
    dajax.assign('#id_dialogo_cuerpo', 'innerHTML', '<span> %s </span' % mensaje )
    dajax.script(" $('#mensajesregistros').modal('toggle').css({'width': '600px','margin-left': function () {return -($(this).width() / 2);}})")


def dialogo_mensajes(dajax,titulo,mensaje,valor,paraid,cabregid,cabanaid):
    dajax.assign('#id_dialogo_titulo', 'innerHTML', '<span> %s </span' % titulo )
    dajax.assign('#id_dialogo_cuerpo', 'innerHTML', '<span> %s </span' % mensaje )
    dajax.script(" $('#dialogomensajes').modal('toggle').css({'width': '600px','margin-left': function () {return -($(this).width() / 2);}}); "
                 " $('#id_dialogomensajes').click(function(e){  Dajaxice.appcc.generaIncidenciaAnalitica(Dajax.process,{'valor': %s,'paraid' : %s, 'cabregid':%s,'cabanaid': %s } ); $('#dialogomensajes').modal('toggle').close(); return false;    });" % (valor,paraid,cabregid,cabanaid ) )


def registroRealizados(dajax,fechadesde,id,detreg_id,titulo,titulo1,orden):
    evento=[]
    forecolor ="#080707"
    backcolor ="#8d8f7f"
    sfecha= '%s-%s-%s 08:%s'% (str(fechadesde.year),str(fechadesde.month).zfill(2),str(fechadesde.day).zfill(2),str(59 if orden is None else orden).zfill(2))
    data    = {'accion' :'E'     , 'pk': id, 'detreg': detreg_id }
    datacal = {'data'   : data   ,'title': u"%s : %s" % (titulo,titulo1), "start" : sfecha, "end" : sfecha, 'textColor': forecolor , 'color' : backcolor  }
    evento.append(datacal)
    dajax.add_data(evento,'EventosActualiza');


def buscarDuplicados(data,arreglo):
    for i in range(len(arreglo)):
        if data == arreglo[i]['data']:
            return 1
    return 0


def esHoy(dias,difedia):
    #Ver si cae fin de semana, configuración de la frecuencia
    if dias > difedia:
        return False
    else:
        entero,resto = divmod(difedia,dias)
        if resto==0:
            return True
        else:
            return False

@dajaxice_register
def eventosHoy(request):
    verReg = DetallesRegistros.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user),actividades__agenda=True).order_by('actividades')
    hoy = datetime.date.today()
    tareas=[]
    for reg in verReg:
        fechainicio = reg.cabreg.fecha
        horas       = reg.cabreg.frecuencia.nounidades
        dias        = int(int(horas)/24)
        difference  = hoy-fechainicio
        if esHoy(dias,difference.days)==True:
            tareas.append({'tarea':"Zona:%s Equipo:%s" % (reg.zonas,reg.equipos)})

    return simplejson.dumps(tareas)


def limpiarRegistros(dajax,tipo):
    dajax.assign('#id_registros-id','value',"0")
    dajax.assign('#id_registros-detreg_id','value',"0")
    dajax.assign('#id_registros-fechadesde','value'," ")
    dajax.assign('#id_registros-fechadesde','value'," ")
    if tipo=="C":
        dajax.assign('#id_registros-valor', 'value', "0" )
    else:
        dajax.assign('#id_registros-valor', 'value', " " )
    dajax.assign('#id_registros-estado', 'checked',  "on"  )
    dajax.assign('#id_firmas','value', " ")
    dajax.assign('#id_registros-observaciones','value', " ")

@dajaxice_register
def registrosRapidosNuevo(request,pk,sfecha):
    ano,mes,dia= sfecha[:10].split('-')
    fecha      = ("%s/%s/%s") % (dia,mes,ano)
    firmas     = Firmas.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user), fechabaja=None)
    out = []
    out.append('<option value="" selected="selected">---------</option>')
    for option in firmas:
        out.append("<option value='%s'>%s</option>" % (option.id,option.personal.denominacion()))

    dajax      = Dajax()

    cabecera    = get_object_or_404(DetallesRegistros, pk=pk)
    auxiliar    = {"etiqueta" : "<strong>%s</strong>: %s" % (_(u"Registros"),cabecera.actividades), 'zona': "<strong>%s</strong>: %s" % (_(u"Zonas"), cabecera.zonas), 'equipos' : "<strong>%s</strong>: %s" % (_(u"Equipos"),cabecera.equipos)  }

    dajax.remove_css_class("#div_id_valor", "control-group hidden")
    dajax.remove_css_class("#div_id_estado", "control-group hidden")
    if cabecera.actividades.tipo == 'C':
        dajax.add_css_class("#div_id_valor", "control-group hidden")
        dajax.add_css_class("#div_id_estado", "control-group")
    else:
        dajax.add_css_class("#div_id_estado", "control-group hidden")
        dajax.add_css_class("#div_id_valor", "control-group")

    limpiarRegistros(dajax,cabecera.actividades.tipo)

    dajax.assign('#id_registros-detreg_id','value',pk)
    dajax.assign('#id_registros-fechadesde','value',fecha)
    dajax.assign('#id_firmas','innerHTML',''.join(out))

    dajax.assign('#registro', 'innerHTML', '<span> %s </span' % auxiliar['etiqueta'] )
    dajax.assign('#zona', 'innerHTML',  '<span> %s </span'  % auxiliar['zona'])
    dajax.assign('#equipo', 'innerHTML',  '<span> %s </span'  % auxiliar['equipos'])
    dajax.script(" $('#myModal').modal('toggle').css({'width': '500px','margin-left': function () {return -($(this).width() / 2);}}); ")
    return dajax.json()





@dajaxice_register
def registrosRapidosEditar(request,pk,detregid):
    dajax          = Dajax()

    cabecera    = get_object_or_404(DetallesRegistros, pk=detregid)
    auxiliar    = {"etiqueta" : "<strong>%s</strong>: %s" % (_(u"Registros"),cabecera.actividades), 'zona': "<strong>%s</strong>: %s" % (_(u"Zonas"), cabecera.zonas), 'equipos' : "<strong>%s</strong>: %s" % (_(u"Equipos"),cabecera.equipos)  }
    detalle     = get_object_or_404(Registros, pk=pk)
    firmas      = Firmas.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user),fechabaja=None)
    out = []
    out.append('<option value="" selected="selected">---------</option>')
    for option in firmas:
        if option.id == detalle.firmas_id:
            out.append("<option selected='selected' value='%s'>%s</option>" % (option.id,option.personal.denominacion()))
        else:
            out.append("<option value='%s'>%s</option>" % (option.id,option.personal.denominacion() ))
    dajax.assign('#registro', 'innerHTML', '<span> %s </span' % auxiliar['etiqueta'] )
    dajax.assign('#zona', 'innerHTML',  '<span> %s </span'  % auxiliar['zona'])
    dajax.assign('#equipo', 'innerHTML',  '<span> %s </span'  % auxiliar['equipos'])


    dajax.remove_css_class("#div_id_valor", "control-group hidden")
    dajax.remove_css_class("#div_id_estado", "control-group hidden")
    if cabecera.actividades.tipo == 'C':
        dajax.add_css_class("#div_id_valor", "control-group hidden")
        dajax.add_css_class("#div_id_estado", "control-group")
    else:
        dajax.add_css_class("#div_id_estado", "control-group hidden")
        dajax.add_css_class("#div_id_valor", "control-group")

    limpiarRegistros(dajax,cabecera.actividades.tipo)

    dajax.assign('#id_registros-id','value',pk)
    dajax.assign('#id_registros-detreg_id','value',detregid)
    dajax.assign('#id_registros-fechadesde','value',"%s/%s/%s" % (detalle.fechadesde.day,detalle.fechadesde.month,detalle.fechadesde.year))
    dajax.assign('#id_registros-valor', 'value', detalle.valor    )
    dajax.assign('#id_registros-estado', 'checked',  detalle.estado  )
    dajax.assign('#id_firmas','innerHTML',''.join(out))
    dajax.assign('#id_registros-observaciones','value', detalle.observaciones)


    dajax.script(" $('#myModal').modal('toggle').css({'width': '500px','margin-left': function () {return -($(this).width() / 2);}})")
    return dajax.json()


def validacionLimitesCriticos(detreg,valor):
    if detreg.tplimitcrit is not None:
        vmax = detreg.tplimitcrit.valormax
        vmin = detreg.tplimitcrit.valormin
        unid = detreg.tplimitcrit.unidades
        if valor>= vmin and valor<=vmax:
            return None
        else:
            return _("El valor de %s excede los limites establecidos maximos de %s y minimos de %s en %s " % (valor,vmax,vmin,unid) )
    else:
        return _("No se han parametrizado los limites criticos, contacte con Asesor Sanitario" )


#def DiasFestivosNacionales(fecha):
    #Canarias
#    festivos=['01-01-2014','06-01-2014','04-03-2014','17-04-2014','18-04-2014','01-05-2014','30-05-2014','24-06-2014','15-08-2014','08-09-2014','01-11-2014','08-12-2014','06-12-2014','25-12-2014']
#    for fec in festivos:
#        dfec=datetime.datetime.strptime(fec,"%d-%m-%Y")
#        if dfec.day ==fecha.day and dfec.month == fecha.month and dfec.year==fecha.year:
#            return True

#    return False
def DiasFestivosNacionales(fecha,empresa):
    #Canarias
    #festivos=['01-01-2014','06-01-2014','04-03-2014','17-04-2014','18-04-2014','01-05-2014','30-05-2014','24-06-2014','15-08-2014','08-09-2014','01-11-2014','08-12-2014','06-12-2014','25-12-2014']
    festivos = Festivos.objects.filter(empresas=empresa)
    excepciones = ExcepcionesCalendario.objects.filter(empresa=empresa)
    from dateutil import rrule
    for excepcion in excepciones:
        fechaIni = excepcion.fecha_inicio
        iter = 1
        while fechaIni < excepcion.fecha_final:            
            fechaIni=fechaIni +datetime.timedelta(days=1)            
            iter = iter + 1         
        list_days = list(rrule.rrule(rrule.DAILY,dtstart=excepcion.fecha_inicio,count=iter))
        for day in list_days:            
            if day.date() == fecha:
                return True        
    for fec in festivos:
        if fec.fecha == fecha:
            return True


    return False


def FechaValida(fecha,dialaboral,nodias,diaejecuta):

    fecha      = fecha + datetime.timedelta(days=-nodias)
    ndia       = fecha.weekday()
    diacompara = ndia
    
    if diaejecuta in ("A","T","L","F"):
            diaejecuta=None

    if diaejecuta != None:

        dif   = int(diaejecuta) - ndia
        fecha = fecha + datetime.timedelta(days=dif)

    if   dialaboral=="F"   and  ndia == 6: #fin de semana no genera enventos
                fecha = fecha+ datetime.timedelta(days=-2)
    if   dialaboral=="F" and ndia ==5:
                fecha = fecha+ datetime.timedelta(days=-1)
    elif dialaboral==str(diacompara): #Para los dias de semanas que no se trabajan
                return FechaValida(fecha,dialaboral,nodias,diaejecuta)
    elif  nodias==1 and ndia==0 and dialaboral=="F":
                fecha = fecha + datetime.timedelta(days=-3)
    elif  nodias==1 and ndia==0 and dialaboral=="6":
                fecha = fecha + datetime.timedelta(days=-2)
    else:
            return fecha

    return FechaValida(fecha,dialaboral,nodias,diaejecuta)


def validacionFechanterior(fecha,cabecera):
    diajecuta  = cabecera.diaejecuta
    dialaboral = cabecera.cabreg.frecuencia.diaslaborables
    nodias     = int(round(cabecera.cabreg.frecuencia.nounidades/24,0)) #Frecuencia de registro
    fecha      = FechaValida(fecha,dialaboral,nodias,diajecuta)

    if fecha > cabecera.cabreg.fecha: #Solo valida resultados de fecha mayores desde la fecha de inicio
        try:
            objreg = Registros.objects.get(fechadesde=fecha, detreg=cabecera, horarioturno__ihora__lt=HORA, horarioturno__fhora__gt=HORA )
        except Registros.DoesNotExist:
            if DiasFestivosNacionales(fecha,cabecera.empresa):
                pass
            else:
                return _("No existe registro anterior, complete primero el de fecha %s " % fecha)

        except Registros.MultipleObjectsReturned:
            return _("Existe mas de un registro para la fecha %s " % fecha)

    return None


@dajaxice_register
def registrosRapidosGuardar(request,form,pk,detregid,incidencia):
    dajax = Dajax()
    cabecera =  get_object_or_404(DetallesRegistros, pk=detregid)
    mensajeError=None
    mensajeValidacion= None
    if pk !="0": #Edicion
        detalle  =  get_object_or_404(Registros, pk=pk)
        form     =  RegistrosRapidosForms(deserialize_form(form),instance=detalle)
    else:
        form = RegistrosRapidosForms(deserialize_form(form))


    if form.is_valid():
        padre                 = form.save(commit=False)
        padre.detreg          = cabecera
        padre.fechahasta      = padre.fechadesde
        print incidencia
        if incidencia == "N":
            if padre.fechadesde>cabecera.cabreg.fecha :
                mensajeError=validacionFechanterior(padre.fechadesde,cabecera)
            if cabecera.actividades.tipo =="V":
                mensajeValidacion=  validacionLimitesCriticos(cabecera,padre.valor)
            if mensajeError is None and mensajeValidacion is None:
                padre.save()
                registroRealizados(dajax,padre.fechadesde,padre.id,padre.detreg_id,cabecera.actividades,cabecera.zonas ,cabecera.ordagenda)
            elif mensajeError is not None:
                mensajes_error(dajax,_("Error de Integridad"),mensajeError)
            elif mensajeValidacion is not None:
                mensajes_validacion(dajax,_("Error de Validación"), mensajeValidacion)
            else:
                mensajes_validacion(dajax,_("Error de Validación"), "%s,%s" % (mensajeError,mensajeValidacion))
        else:
            padre.save()
            registroRealizados(dajax,padre.fechadesde,padre.id,padre.detreg_id,cabecera.actividades,cabecera.zonas ,cabecera.ordagenda)
            etapa=None
            try:
                objetos = CuadrosGestion.objects.filter(registros=cabecera.cabreg)
                etapa = objetos[0].etapa
                
            except CuadrosGestion.DoesNotExist:
                etapa =None
                mensajes_error(dajax,_("Error de Integridad"),"No existe cuadro de gestión")
            except CuadrosGestion.MultipleObjectsReturned:
                etapa = etapa[0]

            if etapa is not None:
                gincidencias=GestorIncidencias(appcc   = cabecera.cabreg.manautctrl.appcc,
                                     fincidencia   = datetime.datetime.now().date(),
                                     estado        = "C",
                                     denominacion  = cabecera.actividades,
                                     equipo        = cabecera.equipos,
                                     zonas         = cabecera.zonas,
                                     tpmedactc     = cabecera.cabreg.tpmedactc,
                                     tipogenera    = "A",
                                     etapa         = etapa,
                                     observaciones = ("%s en fecha %s") % (validacionLimitesCriticos(cabecera,padre.valor),padre.fechadesde)  )
                gincidencias.save(user=request.user)

    else:
        mensaje=form.errors.as_text()
        mensajes_error(dajax,_("Error de Integridad"),mensaje)


    return dajax.json()



# def llenarAgendaNuevos(reg,rango,fecha):
#     eventos     = []
#     dialaboral  = reg[8]
#     diaejecuta  = reg[13]
#     horas       = reg[14]
#     forecolor   = reg[10]
#     backcolor   = reg[11]
#     dias        = reg[7]
#     if dias>2 and dias <=15:
#         rango=3
#     if dias>15:
#         rango=1
#
#     set = rruleset()
#     if dialaboral=="F" and dias==1:
#         set.rrule(rrule(DAILY,count=rango,dtstart=fecha))
#         set.exrule(rrule(YEARLY,byweekday=(6,7),dtstart=fecha))
#     elif dialaboral!='F' and dias==1 and dialaboral is not None:
#         wday= int(dialaboral)
#         set.rrule(rrule(DAILY,count=rango,dtstart=fecha))
#         set.exrule(rrule(YEARLY,byweekday=(wday),dtstart=fecha))
#     elif dias>=7 and dias<30 and diaejecuta is not None:
#         wday= int(diaejecuta)
#         intervalo = int(round(dias/7),0)
#         set.rrule(rrule(WEEKLY,count=4,dtstart=fecha,interval=intervalo,wkst=0,byweekday=wday))
#     elif dias>=30 and diaejecuta is not None:
#         wday= int(diaejecuta)
#         intervalo = int(round(dias/4),0)
#         set.rrule(rrule(MONTHLY,count=3,dtstart=fecha,interval=intervalo,wkst=0,byweekday=wday))
#     elif dias>30 and diaejecuta is not None:
#         wday= int(diaejecuta)
#         intervalo = int(round(dias/30),0)
#         set.rrule(rrule(YEARLY,count=3,dtstart=fecha,interval=intervalo,wkst=0,byweekday=wday))
#
#
#     lfechas= list(set)
#     for fecha in lfechas:
#             sfecha= '%s-%s-%s 08:%s'% (str(fecha.year),str(fecha.month).zfill(2),str(fecha.day).zfill(2),str(59 if reg[12] is None else reg[12]).zfill(2))
#             data  = { 'accion' : 'C', 'pk': int(reg[9]), 'fecha': sfecha}
#             if buscarDuplicados(data,eventos) == 0:
#                 datacal = {'data': data   ,'title': u"%s : %s" % (reg[0],reg[1]), "start" : sfecha, "end" : sfecha, 'textColor': forecolor , 'color' : backcolor  }
#                 eventos.append(datacal)
#             fecha = fecha + datetime.timedelta(days=dias)
#
#     return eventos


def llenarAgendaNuevos(reg,rango,fecha):
    eventos     = []
    dialaboral  = reg[8]
    forecolor   = reg[10]
    backcolor   = reg[11]
    dias        = reg[7]
    diajecuta   = reg[13]
    if dias>2 and dias <=15:
        rango=4
    if dias>15:
        rango=2

    for i in range(rango):
        ndia  = fecha.weekday()
        #Nos aseguramos que el tipo no es caracter

        if diajecuta in ("A","T","L","F"):
            diajecuta=None

        if diajecuta is None:
            diacompara = ndia
            if   dialaboral=="F"   and  ndia == 5: #fin de semana no genera enventos
                fecha = fecha+ datetime.timedelta(days=2)
            elif dialaboral=="F"   and  ndia == 6: #fin de semana no genera enventos
                fecha = fecha+ datetime.timedelta(days=1)
            elif dialaboral==str(diacompara): #Para los dias de semanas que no se trabajan
                fecha = fecha+ datetime.timedelta(days=1)
        else:
            dif = int(diajecuta) - ndia
            fecha = fecha + datetime.timedelta(days=dif)

        if fecha>=reg[3]:
            sfecha= '%s-%s-%s 08:%s'% (str(fecha.year),str(fecha.month).zfill(2),str(fecha.day).zfill(2),str(59 if reg[12] is None else reg[12]).zfill(2))
            data  = { 'accion' : 'C', 'pk': int(reg[9]), 'fecha': sfecha}
            if buscarDuplicados(data,eventos) == 0:
                datacal = {'data': data   ,'title': u"%s : %s" % (reg[0],reg[15]), "start" : sfecha, "end" : sfecha, 'textColor': forecolor , 'color' : backcolor  }
                eventos.append(datacal)
        fecha = fecha + datetime.timedelta(days=dias)

    return eventos



def llenarRegistrosEdicion(reg,rango):
    hora    = datetime.datetime.now().hour
    eventos =[]
    fini = reg[2]+datetime.timedelta(days=-rango)
    ffin = reg[2]+datetime.timedelta(days=1)
    registros = Registros.objects.filter(detreg_id=reg[9] , fechadesde__gt=fini ,fechadesde__lt=ffin,horarioturno__ihora__lt=HORA,horarioturno__fhora__gt=HORA)
    forecolor ="#080707"
    backcolor ="#8d8f7f"

    for areg in registros:
        inihora = areg.horarioturno.ihora
        sfecha= '%s-%s-%s %s:%s'% (str(areg.fechadesde.year),str(areg.fechadesde.month).zfill(2),str(areg.fechadesde.day).zfill(2),str(inihora).zfill(2), str(59 if reg[12] is None else reg[12]).zfill(2))
        data    = {'accion' :'E'     , 'pk': areg.id, 'detreg': areg.detreg_id }
        datacal = {'data'   : data   ,'title': u"%s : %s" % (reg[0],reg[15]), "start" : sfecha, "end" : sfecha, 'textColor': forecolor , 'color' : backcolor  }
        eventos.append(datacal)
    return eventos

def verificaTurno(pid):
     if pid!=0:
            horarios = HorarioTurnos.objects.filter(tpturnos__id=pid)
            for horaturno in horarios:
                if horaturno.ihora<HORA and horaturno.fhora>=HORA:
                    return True
            return False

     else:
         return True

@dajaxice_register
def eventos(request):
    eventos=[]
    rango=1
    user_id = User.objects.get(username=request.user).id
    sql =   """ select actividades,
                       zonas,
                       fechaultimo,
                       fechaalta,
                       diasinicio,
                       empresa_id,
                       user_id,
                       dias,
                       diaslaborables,
                       id,
                       colortxt,
                       colorback,
                       orden,
                       diaejecuta,
                       horas,
                       equipo,
                       tpturnos_id,
                       horarioturno_id
                 from v$detreg_agenda where user_id= %s order by orden,actividades,equipo desc """ % user_id

    cur    = connection.cursor()
    cur.execute(sql)
    verReg = cur.fetchall()
    #Crear dos set unos con los detalles de registros para iniciar el recorrido  y otro con los registros para buscar a nivel de tupla los ya existentes
    for reg in verReg:
        regnuevos=[]
        regeditar=[]
        #Comprobamos dias desde inicio a  utlimo registro
        diasinicio = reg[4]
        if verificaTurno(reg[16]):
            #print  "Detalle registro id %s " % reg[9]
            regnuevos = llenarAgendaNuevos(reg, 30  , reg[2] if diasinicio ==0 else reg[2]+datetime.timedelta(days=reg[7]) )

            if diasinicio>0:
                regeditar = llenarRegistrosEdicion(reg, 30 if diasinicio>=15 else diasinicio)

            eventos =  eventos+regnuevos+regeditar


    return simplejson.dumps(eventos)



@dajaxice_register
def validaAnaliticas(request,valor,paraid,cabregid,cabanaid):
    dajax = Dajax()
    objcomparar=[]
    txtunidades      = ParametrosAnalisis.objects.get(pk=paraid).unidades.denominacion
    if cabregid !=0:
        objcomparar      = ValoresAnaliticas.objects.filter(manautctrl__manautctrl_id= CabRegistros.objects.get(pk=cabregid).manautctrl, paramanali_id=paraid)
    else:
        try:
            objmanu = CabAnaliticas.objects.get(pk=cabanaid).cabreg.manautctrl
        except CabAnaliticas.DoesNotExist:
            objmanu=0
        if objmanu!=0:
            objcomparar      = ValoresAnaliticas.objects.filter(manautctrl__manautctrl_id= objmanu, paramanali_id=paraid)

    if objcomparar == []:
        mensajeError= _("Parametro no definido en el Plan de Auto Control")
        mensajes_error(dajax,_("Error Parametrización"),mensajeError)
    else:
        valorcomp        = objcomparar[0].valores
        tolerancia       = Decimal(objcomparar[0].tolerancia)/100
        decivalor        = Decimal(valor)
        porc_error       = valorcomp*Decimal(tolerancia)
        diferror         = abs(valorcomp-decivalor)
        if diferror > porc_error :
            mensajeValidacion =_("El parametro introducido supera el valor admisible de %s %s , si continua se genera incidencia" % (valorcomp,txtunidades) )
            dialogo_mensajes(dajax,_("Error de Validación"), mensajeValidacion, valor,paraid,cabregid,cabanaid)
    return dajax.json()


@dajaxice_register
def generaIncidenciaAnalitica(request,valor,paraid,cabregid,cabanaid):
    dajax = Dajax()
    txtunidades      = ParametrosAnalisis.objects.get(pk=paraid).unidades.denominacion
    if cabregid !=0:
        objcabreg        = CabRegistros.objects.get(pk=cabregid)
        objcomparar      = ValoresAnaliticas.objects.filter(manautctrl__manautctrl_id= CabRegistros.objects.get(pk=cabregid).manautctrl, paramanali_id=paraid)
    else:
        objcabreg        = CabAnaliticas.objects.get(pk=cabanaid).cabreg
        objcomparar      = ValoresAnaliticas.objects.filter(manautctrl__manautctrl_id= CabAnaliticas.objects.get(pk=cabanaid).cabreg.manautctrl, paramanali_id=paraid)
    etapa=None
    if objcomparar == []:
        mensajeError= _("Parametro no definido en el Plan de Auto Control")
        mensajes_error(dajax,_("Error Parametrización"),mensajeError)
    else:
        valorcomp        = objcomparar[0].valores
        tolerancia       = Decimal(objcomparar[0].tolerancia)/100
        decivalor        = Decimal(valor)
        porc_error       = valorcomp*Decimal(tolerancia)
        diferror         = abs(valorcomp-decivalor)


    etapa=[]
    etapa = CuadrosGestion.objects.filter(registros=objcabreg.id)[0].etapa


    if etapa !=[]:
                gincidencias=GestorIncidencias(appcc   = objcabreg.manautctrl.appcc,
                                     fincidencia   = datetime.datetime.now().date(),
                                     estado        = "C",
                                     denominacion  = "Analiticas",
                                     tpmedactc     = objcabreg.tpmedactc,
                                     tipogenera    = "A",
                                     etapa         = etapa,
                                     observaciones = ("Para el parametro %s el valor obtenido por analitica de  %s %s no se encuentra dentro de los limites de control de %s %s ") % (objcomparar[0].paramanali.denominacion ,decivalor,txtunidades,valorcomp,txtunidades)   )
                gincidencias.save(user=request.user)


@dajaxice_register
def arbolCuadrosGestion(request,empresaid):
    arbol = JsonCuadrosGestion(empresaid)
    listarbol = arbol.generar()
    resjson = simplejson.dumps(listarbol,cls=JSONEncoder)
    return resjson

def arbolDiccionario(ele,expand,check,tipo):
        #diccionario= { "id" : str(ele[0]) , "text": ele[1].encode('utf-8') , "leaf": False ,"value" :ele[2] , "expanded":expand, "checked": check, "cls":tipo }
        diccionario = {"id" : str(ele[0]) , "label" : '<a href="%s">%s</a>' %(ele[2],ele[1].encode('utf-8')) }
        return diccionario
#--------------------------------------------------
#Construye json para la impresion de registros
#--------------------------------------------------
@dajaxice_register
def JsonImpRegPanel(request):
        empresaid= Empresas.objects.get(usuario=request.user).id
        from appcc.models import CabRegistros, DetallesRegistros,ManualAutoControl
        root = ManualAutoControl.objects.filter(empresa_id=int(empresaid))
        nivel1=[]
        for hijos in root:
            cabreg = CabRegistros.objects.filter(manautctrl=hijos)
            if cabreg.count() !=0:
                nivel2=[]
                for ecab in cabreg:
                 detreg = DetallesRegistros.objects.filter(cabreg=ecab, actividades__agenda=True )
                 if detreg.count()!=0:
                     nivel3=[]
                     for edet in detreg:
                         ele    =[int(edet.id),"%s - %s" % (edet.actividades.denominacion,edet.zonas),edet.urlImpresion()]
                         arbol= arbolDiccionario(ele,False,False,'null')
                         arbol['leaf'] = True
                         nivel3.append(arbol)
                         ele=[]

                     ele = [int(ecab.id),ecab.denominacion,ecab.urlImpresion()]
                     arbol = arbolDiccionario(ele,False,False,'folder')
                     arbol['leaf'] = False
                     arbol['children'] = nivel3
                     nivel2.append(arbol)
                     ele=[]

                if len(nivel2)!=0:
                    ele   = [int(hijos.id),hijos.tpplancontrol.denominacion,hijos.urlImpresion()]
                    arbol = arbolDiccionario(ele,False,False,'folder')
                    arbol['children']=nivel2
                    nivel1.append(arbol)
                    ele=[]
        return simplejson.dumps(nivel1)



@dajaxice_register
def graficaentrada(request):
    empresaid  = Empresas.objects.get(usuario=request.user).id
    listcab    = CabRegistros.objects.filter(empresa_id=empresaid)
    dajax = Dajax()
    out = []
    out.append('<option value="" selected="selected">---------</option>')
    for cab in listcab:
            regvalido  = DetallesRegistros.objects.filter( cabreg_id=cab.id , actividades__agenda=True, actividades__tipo='V')
            if  len(regvalido) !=0:
                out.append("<option value='%s'>%s</option>" % (cab.id,cab.denominacion))

    dajax.assign('#id_selcabreg','innerHTML',''.join(out))
    dajax.script(" $('#grafregModal').modal('toggle').css({'width': '1200px','margin-left': function () {return -($(this).width() / 2);}}); ");
    return dajax.json()

@dajaxice_register
def  graficaregistros(request,idcab):
    hoy = datetime.datetime.now().date()
    empresaid  = Empresas.objects.get(usuario=request.user).id
    listdetreg = DetallesRegistros.objects.filter(cabreg_id=idcab,empresa_id=empresaid, actividades__agenda=True, actividades__tipo='V')
    grafico    =[]
    datos      =[]
    for detreg in listdetreg:
        listreg    = Registros.objects.filter(detreg_id = detreg.id, fechadesde__year=hoy.year).order_by('fechadesde')
        for reg in listreg:
            datos.append((tiempoenMil(int(reg.fechadesde.day),int(reg.fechadesde.month),int(reg.fechadesde.year),0,0),reg.valor))
        grafico.append({'label' : detreg.zonas.denominacion ,'data': datos,'color': colorHexRamdom() })
        datos =[]


    return simplejson.dumps(grafico)