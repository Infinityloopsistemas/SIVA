# -*- coding: utf-8 -*-
import datetime
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
import maestros
from maestros.models import Zonas, HorarioTurnos
from maestros_generales.models import Empresas
from django.db.models import Avg,Q
from django.db.models.signals import post_save
import logging
logger = logging.getLogger(__name__)






class TrackTemperaturas(models.Model):
    DeviceName      = models.CharField(max_length=30)
    HostName        = models.CharField(max_length=30)
    MACAddress      = models.CharField(max_length=17)
    zonas           = models.ForeignKey(Zonas)
    fechaalta       = models.DateField(auto_now_add=True,verbose_name=("Fecha Alta"),blank=True,null=True)
    fechabaja       = models.DateField(verbose_name=("Fecha Baja"), blank=True,null=True)
    empresa         = models.ForeignKey(Empresas,null=True, blank=True,verbose_name=('Empresa'),on_delete=models.PROTECT)

    def __unicode__(self):
        return "%s -%s -%s" % (self.DeviceName,self.HostName,self.empresa)

    def tempDia(self,dia,mes,ano):
        # Retorna {'Temperature__avg': -18.24487705}
        temp = {'Temperature__avg': 0}
        if dia!=None and mes !=None and ano!=None:
           temp = LoadDataSensor.objects.filter(Q(tracksonda_id=self.id), Q(date__gt=datetime.datetime(ano,mes,dia,0,0) ) & Q(date__lt=datetime.datetime(ano,mes,dia,23,59) ) ).aggregate(Avg('Temperature'))
        return temp

    def numeroSondas(self):
        numsondas = TrackSondas.objects.filter(tracktemp=self.id).count()
        if numsondas != []:
            return numsondas
        else:
            return 0
    numeroSondas.short_description = "Numero de Sondas"
    numeroSondas.allow_tags = True

class TrackSondas(models.Model):
    tracktemp       = models.ForeignKey(TrackTemperaturas)
    Name            = models.CharField(max_length=30)
    Family          = models.IntegerField()
    ROMId           = models.CharField(max_length=30)
    rangoaviso      = models.IntegerField(verbose_name="Tiempo de Aviso (min)", null=True)

    def __unicode__(self):
        return "%s -%s -%s" % (self.ROMId,self.Name,self.tracktemp.empresa)

    def tempDia(self,dia,mes,ano):
        #Calcula dia de semana para seleccionar configuracion correcta.
        diasemana = datetime.datetime(ano,mes,dia,0,0).weekday()
        if diasemana in [0,1,2,3,4]:
            pardia='L'
        elif diasemana in [5,6]:
            pardia='F'
        else:
            pardia = diasemana
        # Retorna {'Temperature__avg': -18.24487705}
        empresaid= self.tracktemp.empresa.id
        cabregid = appcc.models.DetallesRegistros.objects.filter(tracksondas_id=self.id, empresa_id= empresaid )[0].cabreg_id
        turnos   = appcc.models.DetalleConfiguracion.objects.filter(configuracion__empresa__id=empresaid, habilitar='S',registros__in=[cabregid], dias=pardia )[0].turnos

        hturnos  = maestros.models.HorarioTurnos.objects.filter( tpturnos_id = turnos.id)
        hinicio  = hturnos[0].ihora #   No contempla mas horas en el turno
        hfin     = hturnos[0].fhora
        horas    =  24-(hfin-hinicio)
        minu     = 59 if hfin ==24 else 0
        hfin     = 23 if hfin ==24 else hfin
        #OBTENCION DE FECHA PARA EL CALCULO TEMPERATURA
        fini     = datetime.datetime(ano,mes,dia,hfin,minu)
        reshoras =  24 if horas ==0 else horas
        ffin     = fini + datetime.timedelta( hours= reshoras )
        temp = {'Temperature__avg': 0}
        logger.debug("Fecha inicio %s  Fecha Fin %s" % (fini,ffin))
        if dia!=None and mes !=None and ano!=None:
            temp = LoadDataSensor.objects.filter(tracksonda_id=self.id,date__range=[fini,ffin]).aggregate(Avg('Temperature'))
        return temp

    def tempMin(self,fecha,minutos):
        minutos= 10 if minutos is None else minutos
        tantes   = (fecha - datetime.timedelta(minutes=minutos))
        temp = LoadDataSensor.objects.filter(tracksonda_id=self.id,date__range=[tantes,fecha]).aggregate(Avg('Temperature'))
        return temp


class LoadDataDevice(models.Model):
    tracktemp     = models.ForeignKey(TrackTemperaturas)
    fechaalta     = models.DateField(auto_now_add=True,verbose_name=("Fecha Alta"),blank=True,null=True)
    fechabaja     = models.DateField(verbose_name=("Fecha Baja"), blank=True,null=True)
    empresa       = models.ForeignKey(Empresas,null=True, blank=True,verbose_name=('Empresa'),on_delete=models.PROTECT)
    user          = models.ForeignKey(User,blank=True, null=True,on_delete=models.PROTECT)
    PollCount     = models.IntegerField()
    DevicesConnected = models.IntegerField()
    LoopTime = models.DecimalField(max_digits=10,decimal_places=3)
    DevicesConnectedChannel1 = models.IntegerField()
    DevicesConnectedChannel2 = models.IntegerField()
    DevicesConnectedChannel3 = models.IntegerField()
    DataErrorsChannel1 = models.IntegerField()
    DataErrorsChannel2 = models.IntegerField()
    DataErrorsChannel3 = models.IntegerField()
    VoltageChannel1 = models.DecimalField(max_digits=10,decimal_places=3)
    VoltageChannel2 = models.DecimalField(max_digits=10,decimal_places=3)
    VoltageChannel3 = models.DecimalField(max_digits=10,decimal_places=3)
    VoltagePower    = models.DecimalField(max_digits=10,decimal_places=3)
    DeviceName      = models.CharField(max_length=30)
    HostName        = models.CharField(max_length=30)
    MACAddress      = models.CharField(max_length=17)


    def temperaturas(self):
        filas = LoadDataSensor.objects.filter(loadatadevice_id=self.id)
        cabhtml=""" <table> <thead> <th> Fecha </th> <th> Sensor </th> <th> Temp. </th> </thead> """
        filhtml=""
        for row in filas:
         sonda = TrackSondas.objects.get(ROMId=row.ROMId).Name
         filhtml = filhtml+ """ <tr> <td> %s </td> <td> %s </td> <td> %s </td> </tr>""" % (row.date,sonda,row.Temperature)

        finhtml = "</table>"
        return cabhtml+filhtml+finhtml

    temperaturas.short_description = "Temperaturas"
    temperaturas.allow_tags = True

def fechaAlterada():
        return timezone.now() + datetime.timedelta(hours=1)

class LoadDataSensor(models.Model):
    loadatadevice   = models.ForeignKey(LoadDataDevice)
    tracksonda      = models.ForeignKey(TrackSondas)
    Name            = models.CharField(max_length=30)
    Family          = models.IntegerField()
    ROMId           = models.CharField(max_length=30)
    Health          = models.IntegerField()
    Channel         = models.IntegerField()
    PrimaryValue    = models.CharField(max_length=20)
    Temperature     = models.DecimalField(max_digits=10,decimal_places=4)
    date            = models.DateTimeField(default= lambda: timezone.now() + datetime.timedelta(hours=1), blank=True)

    #Problema con la zona horaria de django , pendiente de solucionar, se suma una hora para Canarias



#Guarda cuando se  genera las alarmas
class TrackSondasAlarmas(models.Model):
    tracksonda       = models.ForeignKey(TrackSondas)
    dateaviso        = models.DateTimeField()
    valor            = models.DecimalField(max_digits=10,decimal_places=4)
    idavisosms       = models.CharField(max_length=100,blank=True,null=True)

    def __unicode__(self):
        return "%s -%s -%s" % (self.tracktemp,self.dateaviso,self.valor)

import appcc.models
@receiver(post_save, sender=LoadDataSensor)
def auditoriIndicadores(sender, instance, created, **kwargs):
    logger.debug("Entra en poast_save")
    emp = instance.loadatadevice.empresa

    tiempoaviso = instance.tracksonda.rangoaviso
    fecha = fechaAlterada()
    logger.debug("Fecha actual %s" % fecha)
    # - datetime.timedelta(days=5,hours=3) #el delta para testar
    tantes = (fecha - datetime.timedelta(hours=4))
    hoy = fecha
    diasemana = hoy.weekday()
    if diasemana in [0,1,2,3,4]:
            pardia='L'
    elif diasemana in [5,6]:
            pardia='F'
    else:
            pardia = diasemana
    hora = hoy.now().hour
    #Filtra por EMAIL/INCIDENCIAS, SMS , SMS/EMAIL
    listaenvios = appcc.models.DetalleConfiguracion.objects.filter(configuracion__empresa__id=emp.id, habilitar='S',
                                                                   accion__in=('S', 'Z','T'), dias=pardia)
    listobjreg = appcc.models.DetallesRegistros.objects.filter(tracksondas__isnull=False, empresa_id=emp.id)
    logger.debug("Empresa id %s " % listobjreg)
    if listobjreg:
        logger.debug("Entra en lista objetos")
        for objreg in listobjreg:  #Detalle Registros
            #Conseguir consignas de limites.
            consigna = objreg.tplimitcrit.valormax
            #Revision temperatura rango
            temp = objreg.tracksondas.tempMin(fecha, tiempoaviso)
            sondalarm = {'tracksonda_id': objreg.tracksondas.id, 'dateaviso': fecha,
                         'valor': temp['Temperature__avg'], }
            logger.debug("Sonda valores: %s" % sondalarm)
            if temp['Temperature__avg'] is not None:
                logger.debug("Temperatura de consigna %s" % consigna)
                logger.debug("Temperatura leida %s" %  temp['Temperature__avg'])
                if temp['Temperature__avg'] > consigna:
                    # Apartir de aqui delegar tarea
                    logger.debug("Ejecuta delegacion del evento")
                    from loaddata.tasks import enviosdelegados

                    resul = enviosdelegados.delay(listaenvios, temp, objreg, sondalarm, hora, diasemana, tantes,
                                                  consigna, hoy)
