# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

import datetime
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from private_files import PrivateFileField, pre_download
from loaddata.models import TrackTemperaturas, TrackSondas
from maestros.models import TiposFrecuencias, Terceros, Zonas, Consumibles, CatalogoEquipos, Personal, TiposMedidasVigilancia, TiposLimitesCriticos, TiposMedidasActuacion, Actividades, ParametrosAnalisis, Etapas, Peligros, TiposCursos, TiposTurnos, HorarioTurnos, Firmas, TiposLegislacion
from maestros_generales.models import Empresas, TipoPlanControl
from productos.models import Productos
#from rest_waspmote.models import WaspSensor
from siva.utils import RenameFilesModel, OPCIONES_DIAS, is_owner, buscaHorario,\
    obtenerImagen
from django.db.models.signals import post_save, post_delete
from trazabilidad.models import *

from imagen.models import Imagen



class BaseAPPCC(models.Model):
    fechaalta     = models.DateField(verbose_name=_("Fecha Alta"))
    fechabaja     = models.DateField(verbose_name=_("Fecha Baja"), blank=True,null=True)
    empresa       = models.ForeignKey(Empresas,null=True, blank=True,verbose_name=_('Empresa'),on_delete=models.PROTECT)
    user          = models.ForeignKey(User,on_delete=models.PROTECT)

    def save(self, user, *args, **kwargs):
        if self.fechaalta is None:
            self.fechaalta=datetime.date.today()
        if user is not None:
            self.user= User.objects.get(username=user)
            if  self.user.is_staff==True or (self.user.is_staff ==False and   self.user.has_perm('appcc.change_%s' % self.__class__.__name__.lower())==True) :
                self.empresa = Empresas.objects.get(usuario=self.user)
                super(BaseAPPCC, self).save(*args, **kwargs)
            else:
                raise PermissionDenied


    class Meta:
        abstract = True

class APPCC(BaseAPPCC):
    fechaedicion = models.DateField(verbose_name=_("Fecha Edición"))
    denominacion = models.CharField(max_length="200", verbose_name=_("Denominación"))
    contenido    = models.TextField(verbose_name="Descripción Actividad",blank=True,null=True)

    def __unicode__(self):
        return ('%s %s') % (self.denominacion,self.fechaedicion)

    class Meta:
        verbose_name_plural = _('APPCC')
        verbose_name        = _('APPCC')

    def get_absolute_url(self):
        return reverse('appcc_actualizar',args=[self.pk])

    def urlDocumentos(self):
        #return '/appcc/documentos/lista/appcc_id/%s/' % (self.pk)
        return '/appcc/appcc/documentos/appcc_id/%s/' % (self.pk)

    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/0/%s/' % (nombmodelo,self.pk)

    def urlCuadGestion(self):
        #return '/appcc/cuadrosgestion/lista/%s/' % (self.pk)
        return '/appcc/appcc/cuadrosgestion/%s/' % (self.pk)

    def urlGestorIncidencias(self):
        #return '/appcc/gestorincidencias/lista/%s/' % (self.pk)
        return '/appcc/appcc/gestorincidencias/%s/' % (self.pk)



class HistorialRevisiones(models.Model):
    #Guardar historial completo del APPC , registros y demas crear copia completa
    fecharevision = models.DateField(verbose_name=_("Fecha de Revisión"))
    appcc         = models.ForeignKey(APPCC)

    def __unicode__(self):
        return  self.fecharevision

    class Meta:
        verbose_name_plural = _('Historial de Revisiones')
        verbose_name        = _('Historial de Revisiones')



class ManualAutoControl(BaseAPPCC):
    objeto        = models.TextField(verbose_name=_("Objeto"))
    alcance       = models.TextField(verbose_name=_("Alcance"))
    contenido     = models.TextField(verbose_name=_("Contenido"))
    marcolegal    = models.TextField(verbose_name=_("Marco Legal"))
    procedimiento = models.TextField(verbose_name=_("Pocedimiento Documental"))
    appcc         = models.ForeignKey(APPCC, verbose_name=_("APPCC"),on_delete=models.PROTECT)
    tpplancontrol = models.ForeignKey(TipoPlanControl, verbose_name=_("Tipo Plan Control"),on_delete=models.PROTECT)

    class Meta:
        unique_together = ("appcc", "tpplancontrol")
        verbose_name_plural = _('Manual de Auto Control')
        verbose_name        = _('Manual de Auto Control')

    def __unicode__(self):
        return "%s  --- %s " % (self.tpplancontrol.denominacion, self.appcc)

    def get_absolute_url(self):
        #return reverse('manualautocontrol_actualizar',args=[self.pk])
        return reverse('manualautocontrol_actualizar',args=[self.appcc.id,self.pk])

    def denominacion(self):
        return ("%s --- > %s") % (self.appcc,self.tpplancontrol)

    def etiquetasTemplate(self):
        etiquetas= self.tpplancontrol.etiquetas
        if etiquetas is None:
            return None
        return etiquetas.replace("<p>","").replace("</p>","")


    def urlIra(self):
        if self.tpplancontrol.campoprimario == "RELACION_FORMACION":
            #camino='/appcc/relacionespersonal/lista/%s' % self.pk
            camino = '/appcc/appcc/manualautocontrol/%s/relacionespersonal/%s' % (self.appcc.id,self.pk)
        elif self.tpplancontrol.campoprimario == "RELACION_PROVEEDOR":
            #camino='/appcc/relacionesterceros/lista/%s' % self.pk
            camino = '/appcc/appcc/manualautocontrol/%s/relacionesterceros/%s' % (self.appcc.id,self.pk)
        else:
            #camino='/appcc/planautocontrol/lista/%s' %self.pk
            
            camino = '/appcc/appcc/manualautocontrol/%s/planautocontrol/%s' % (self.appcc.id,self.pk)
        return camino

    def urlDocumentos(self):
        #return '/appcc/documentos/lista/manautctrl_id/%s/' % (self.pk)
        return '/appcc/appcc/manualautocontrol/%s/documentos/manautctrl_id/%s/' % (self.appcc.id,self.pk)

    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/%s/%s' % (nombmodelo,self.tpplancontrol_id,self.pk)
    def urlRegistros(self):
        return '/appcc/appcc/manualautocontrol/%s/cabregistros/%s' % (self.appcc.id,self.pk)


class PlanAutoControl(BaseAPPCC):
    manautctrl   = models.ForeignKey(ManualAutoControl,on_delete=models.PROTECT)
    frecuencia   = models.ForeignKey(TiposFrecuencias, verbose_name=_("Frecuencia"),blank=True,null=True,on_delete=models.PROTECT )
    zonas        = models.ForeignKey(Zonas,verbose_name=_("Zonas Limpieza"),blank=True,null=True,on_delete=models.PROTECT)
    zonalimpieza = models.TextField(verbose_name=_("Zonas de limpieza"),blank=True,null=True)
    proclimpieza = models.TextField(verbose_name=_("Instrucciones de limpieza"),blank=True,null=True)
    tercero      = models.ForeignKey(Terceros, verbose_name=_("Mantenedor"),blank=True,null=True,on_delete=models.PROTECT)
    operaciones  = models.TextField(verbose_name=_("Operaciones"),blank=True,null=True)
    equipos      = models.ForeignKey(CatalogoEquipos,verbose_name=_("Equipos"),blank=True,null=True,on_delete=models.PROTECT)
    productos    = models.ForeignKey(Productos,verbose_name=_("Productos"),blank=True,null=True,on_delete=models.PROTECT)
    personal     = models.ForeignKey(Personal,verbose_name=_("Personal"),blank=True,null=True,on_delete=models.PROTECT)
    fecha        = models.DateField(verbose_name=_("Fecha"),blank=True,null=True)
    tpmedvig     = models.ForeignKey(TiposMedidasVigilancia,verbose_name=_("Medidas de Vigilancia"),blank=True,null=True, related_name="planauto_medvig",on_delete=models.PROTECT)
    tpmedactp    = models.ForeignKey(TiposMedidasActuacion, related_name="rel_preventivas",verbose_name=_("Medidas de Actuacion Preventiva"),blank=True,null=True,on_delete=models.PROTECT)
    tpmedactc    = models.ForeignKey(TiposMedidasActuacion, related_name="rel_correctivas",verbose_name=_("Medidas Correctivas"),blank=True,null=True,on_delete=models.PROTECT)
    observaciones= models.TextField(verbose_name=_("Observaciones"),null=True, blank=True )

    class Meta:
        verbose_name_plural = _('Plan de Auto Control')
        verbose_name        = _('Plan de Auto Control')


    def denominacion(self):
        return ("%s -- %s -- %s") % ((" " if  self.zonas is None else self.zonas),( self.productos if  self.equipos is None else self.equipos ),self.manautctrl)

    def get_absolute_url(self):
        return reverse('planautocontrol_actualizar',args=[self.manautctrl.appcc.id,self.manautctrl.id,self.pk])

    def urlDocumentos(self):
        #return '/appcc/documentos/lista/planautoctrl_id/%s/' % (self.pk)
        return '/appcc/appcc/manualautocontrol/%s/planautocontrol/%s/documentos/planautoctrl_id/%s/' % (self.manautctrl.appcc.id,self.manautctrl.id,self.pk)

    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/%s/%s' % (nombmodelo,self.manautctrl.tpplancontrol.id,self.pk)

class ConsumiblesDosis(models.Model):
    planautctrl  =  models.ForeignKey(PlanAutoControl,verbose_name=_("Plan Limpieza"),on_delete=models.PROTECT)
    consumible   =  models.ForeignKey(Consumibles,verbose_name=_("Productos Limpieza"),on_delete=models.PROTECT)
    dosis        =  models.CharField(max_length=100, verbose_name=_("Dosis"))

    class Meta:
        verbose_name_plural = _('Dosis Consumibles')
        verbose_name        = _('Dosis Consumibles')

#class ProcedimientosLimpieza(MPTTModel):
#    planautctrl   = models.ForeignKey(PlanAutoControl,verbose_name=_("Plan Limpieza"))
#    descripcion   = models.CharField(max_length=100, verbose_name=_("Descripción"))
#    parent        = TreeForeignKey('self', null=True, blank=True, related_name='children')
#    orden         = models.IntegerField(verbose_name=_("Orden"))
#
#
#    class Meta:
#        verbose_name_plural = _('Procedimientos de Limpieza')
#        verbose_name        = _('Procedimientos de Limpieza')
#
#    class MPTTMeta:
#        level_attr        = 'mptt_level'
#        order_insertion_by=['orden']




class ValoresAnaliticas(models.Model):
    paramanali  = models.ForeignKey(ParametrosAnalisis,verbose_name=_("Parametro"),on_delete=models.PROTECT)
    valores     = models.DecimalField(max_digits=12,decimal_places=4, verbose_name=_("Valor"), help_text="Introduzca Valor de Referencia")
    #manautctrl  = models.ForeignKey(PlanAutoControl,on_delete=models.PROTECT)
    manautctrl  = models.ForeignKey(ManualAutoControl,on_delete=models.PROTECT)
    tolerancia  = models.IntegerField( max_length=3, verbose_name=_("Margen de Tolerancia"))

    def __unicode__(self):
        return "%s %s" % (self.paramanali,self.valores)

    class Meta:
        verbose_name_plural = _('Valores de Referencia Analiticas')
        verbose_name        = _('Valor de Referencia Analitica')


class CabRegistros(BaseAPPCC):
    fecha        = models.DateField( verbose_name="Fecha Inicio", null=True, blank=True)
    manautctrl   = models.ForeignKey(ManualAutoControl, verbose_name="Manual de Autocontrol",on_delete=models.PROTECT)
    denominacion = models.CharField(max_length="200", verbose_name=_("Denominación"))
    tpmedvig     = models.ForeignKey(TiposMedidasVigilancia,verbose_name=_("Medidas de Vigilancia"),blank=True,null=True,on_delete=models.PROTECT)
    frecuencia   = models.ForeignKey(TiposFrecuencias, verbose_name=_("Frecuencia"),blank=True,null=True,on_delete=models.PROTECT )
    tpmedactc    = models.ForeignKey(TiposMedidasActuacion, related_name="reg_medact",verbose_name=_("Medidas Correctoras"),blank=True,null=True,on_delete=models.PROTECT)


    class Meta:
        verbose_name_plural = _('Cabecera de Registros')
        verbose_name        = _('Cabecera de Registro')


    def get_absolute_url(self):
        #return reverse('cabregistros_actualizar',args=[self.pk])
        return reverse('cabregistros_actualizar',args=[self.manautctrl.appcc.id,self.manautctrl.id,self.pk])


    def urlDocumentos(self):
        #return '/appcc/documentos/lista/cabreg_id/%s/' % (self.pk)
        return '/appcc/appcc/manualautocontrol/%s/cabregistros/%s/documentos/cabreg_id/%s/' % (self.manautctrl.appcc.id,self.manautctrl.id,self.pk)
        

    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/%s/%s' % (nombmodelo,self.manautctrl.tpplancontrol.id,self.pk)

    def __unicode__(self):
        return self.denominacion


class DetallesRegistros(BaseAPPCC):
    cabreg      = models.ForeignKey(CabRegistros,on_delete=models.PROTECT)
    actividades = models.ForeignKey(Actividades, verbose_name=_("Actividades"),on_delete=models.PROTECT)
    tplimitcrit = models.ForeignKey(TiposLimitesCriticos,verbose_name=_("Limites Criticos"),blank=True,null=True,on_delete=models.PROTECT)
    zonas       = models.ForeignKey(Zonas,verbose_name=_("Zonas"),blank=True,null=True,on_delete=models.PROTECT)
    equipos     = models.ForeignKey(CatalogoEquipos,verbose_name=_("Equipos"),blank=True,null=True,on_delete=models.PROTECT)
    valanali    = models.ForeignKey(ParametrosAnalisis,verbose_name=_("Parametro a controlar"),blank=True,null=True,on_delete=models.PROTECT)
    ordagenda   = models.CharField(max_length=3,verbose_name=_("Orden Agenda"), blank=True,null=True)
    diaejecuta  = models.CharField(max_length=1,verbose_name=_("Día ejecución"),blank=True,null=True,choices=OPCIONES_DIAS)
    tpturnos      = models.ForeignKey(TiposTurnos, verbose_name=_("Turno"),on_delete=models.PROTECT,blank=True,null=True)
    tracksondas   = models.ForeignKey(TrackSondas, blank=True, null=True,verbose_name="Sensor NetConnect")
    #trackwaspsensor = models.ForeignKey(WaspSensor, blank=True, null=True,verbose_name="Sensores WaspMote")

    class Meta:
        verbose_name_plural = _('Detalle de Registros')
        verbose_name        = _('Detalle de Registro')

    def get_absolute_url(self):
        #return reverse('detallesregistros_actualizar',args=[self.pk])
        return reverse('detallesregistros_actualizar',args=[self.cabreg.manautctrl.appcc.id,self.cabreg.manautctrl.id,self.cabreg.id,self.pk])


    def denominacion(self):
        return ("%s %s %s %s") % (self.actividades,(" " if  self.valanali is None else self.valanali),(" " if  self.zonas is None else self.zonas),(" " if  self.equipos is None else self.equipos ))

    denominacion.short_description="Nombre Registro"
    denominacion.allow_tags = True

    def urlDocumentos(self):
        #return '/appcc/documentos/lista/detreg_id/%s/' % (self.pk)
        return '/appcc/appcc/manualautocontrol/%s/cabregistros/%s/detallesregistros/%s/documentos/detreg_id/%s/' % (self.cabreg.manautctrl.appcc.id,self.cabreg.manautctrl.id,self.cabreg.id,self.pk)

    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/%s/%s' % (nombmodelo,self.cabreg.manautctrl.tpplancontrol.id,self.pk)


class Registros(models.Model):

    detreg       = models.ForeignKey(DetallesRegistros,on_delete=models.PROTECT)
    fechadesde   = models.DateField(verbose_name=_("Fecha Desde"))
    fechahasta   = models.DateField(verbose_name=_("Fecha Hasta"),blank=True,null=True)
    valor        = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_("Valor"),blank=True,null=True)
    estado       = models.BooleanField(verbose_name=_("Estado"))
    observaciones= models.CharField(max_length=500,blank=True,null=True, verbose_name=_("Observaciones"),help_text=_("Incidencias detectadas"))
    firmas       = models.ForeignKey(Firmas,verbose_name=_("Firmar Registro"),blank=True,null=True,on_delete=models.PROTECT)
    horarioturno = models.ForeignKey(HorarioTurnos,verbose_name=_("Horario Turno"),blank=True,null=True,on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = _('Registros')
        verbose_name        = _('Registro')

    def __unicode__(self):
        return ("%s %s %s %s %s") % (self.detreg.id,self.detreg.actividades,(" " if  self.detreg.valanali is None else self.detreg.valanali),(" " if  self.detreg.zonas is None else self.detreg.zonas),(" " if  self.detreg.equipos is None else self.detreg.equipos ))


    def denominacion(self):
        return ( ("%s %s %s %s %s") % (self.detreg.id,self.detreg.actividades,(" " if  self.detreg.valanali is None else self.detreg.valanali),(" " if  self.detreg.zonas is None else self.detreg.zonas),(" " if  self.detreg.equipos is None else self.detreg.equipos ))).decode('utf-8')

    denominacion.short_description="Nombre Registro"
    denominacion.allow_tags = True

    unique_together     = ("detreg","fechadesde","horarioturno")
    index_together	    = [["detreg","fechadesde","horarioturno"],]

    def save(self, *args, **kwargs):
        #El turno no se puede cambiar una vez introducido
        if self.horarioturno_id is None:
            self.horarioturno_id =buscaHorario(self.detreg)
        super(Registros, self).save(*args, **kwargs)


class CuadrosGestion(MPTTModel, BaseAPPCC):
    appcc        = models.ForeignKey(APPCC, verbose_name=_("APPCC"),on_delete=models.PROTECT)
    parent       = TreeForeignKey('self', null=True, blank=True, related_name='hijo',on_delete=models.PROTECT)
    orden        = models.CharField(max_length=50 ,verbose_name=_("Orden"),null=True,blank=True)
    etapa        = models.ForeignKey(Etapas, verbose_name=_("Etapa"),on_delete=models.PROTECT)
    peligro      = models.ForeignKey (Peligros, max_length=500, verbose_name=_("Peligro"),on_delete=models.PROTECT)
    tpmedactp    = models.ForeignKey(TiposMedidasActuacion, related_name="cuadgest_preventivas",verbose_name=_("Medidas de Actuacion Preventiva"),blank=True,null=True,on_delete=models.PROTECT)
    ptocritico   = models.CharField(max_length=3,verbose_name=_("P.C"))
    ptoctrlcrit  = models.CharField(max_length=3,verbose_name=_("P.C.C"))
    tplimitcrit  = models.ForeignKey(TiposLimitesCriticos,verbose_name=_("Limites Criticos"),blank=True,null=True,related_name="cuadgest_limcrit",on_delete=models.PROTECT)
    tpmedvig     = models.ForeignKey(TiposMedidasVigilancia,verbose_name=_("Medidas de Vigilancia"),blank=True,null=True, related_name="cudgest_medvig",on_delete=models.PROTECT)
    momento      = models.CharField(max_length=500, verbose_name=_("Momento"),help_text=_("Cuando se realializa la acción"))
    ente         = models.ForeignKey(Personal,verbose_name=_("Personal"),on_delete=models.PROTECT,blank=True,null=True)
    tpmedactc    = models.ForeignKey(TiposMedidasActuacion, related_name="cuadgest_correctiva",verbose_name=_("Medidas de Actuacion Correctora"),blank=True,null=True,on_delete=models.PROTECT)
    registros    = models.ForeignKey(CabRegistros,verbose_name=_("Registros"),null=True,blank=True,on_delete=models.PROTECT)
    tpfrecreg    = models.ForeignKey(TiposFrecuencias, related_name="frecuencia_registro", verbose_name="Frec Reg.",null=True,blank=True,on_delete=models.PROTECT)

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by=['etapa']

    def denominacion(self):
        return ("%s.- %s (%s)") % (self.orden,self.etapa,self.peligro)

    def urlDocumentos(self):
        #return '/appcc/documentos/lista/cuadgest_id/%s/' % (self.pk)
        return '/appcc/appcc/cuadrosgestion/%s/documentos/cuadgest_id/%s/' % (self.appcc.id,self.pk)

    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/0/%s/' % (nombmodelo,self.pk)

    def get_absolute_url(self):
        #return reverse('cuadrosgestion_actualizar',args=[self.pk])
        return reverse('cuadrosgestion_actualizar',args=[self.appcc.id,self.pk])

    def niveles(self):
        return self.mptt_level *"--"




class RelacionesEntes(BaseAPPCC):
    manautctrl   = models.ForeignKey(ManualAutoControl,on_delete=models.PROTECT)
    frecuencia   = models.ForeignKey(TiposFrecuencias, verbose_name=_("Frecuencia"),on_delete=models.PROTECT)
    personal     = models.ForeignKey(Personal,verbose_name=_("Personal"),blank=True,null=True,on_delete=models.PROTECT)
    tercero      = models.ForeignKey(Terceros, verbose_name=_("Tercero"),blank=True,null=True,on_delete=models.PROTECT )
    actividades  = models.ForeignKey(Actividades,verbose_name=_("Actividad"),blank=True,null=True,on_delete=models.PROTECT)
    fechavalida  = models.DateField(verbose_name=_("Fecha Certificacion"))
    tiposcursos  = models.ForeignKey(TiposCursos,verbose_name=_("Tipo Curso"),blank=True,null=True,on_delete=models.PROTECT)

    def denominacion(self):
        return ("%s" ) % (self.tercero if  self.personal is None else self.personal)

    def get_absolute_url(self):
        #return reverse('relacionesentes_actualizar',args=[self.pk])
        if self.manautctrl.tpplancontrol.campoprimario == "RELACION_FORMACION":            
            rel = "relacionespersonal"            
        else:
            rel = "relacionesterceros"  
        return reverse('relacionesentes_actualizar',args=[self.manautctrl.appcc.id,rel,self.manautctrl.id,self.pk])

    def urlDocumentos(self):
        #return '/appcc/documentos/lista/relentes_id/%s/' % (self.pk)
        if self.manautctrl.tpplancontrol.campoprimario == "RELACION_FORMACION":            
            rel = "relacionespersonal"            
        else:
            rel = "relacionesterceros" 
        return '/appcc/appcc/manualautocontrol/%s/%s/%s/documentos/relentes_id/%s/' % (self.manautctrl.appcc.id,rel,self.manautctrl.id,self.pk)

    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/%s/%s' % (nombmodelo,self.manautctrl.tpplancontrol.id,self.pk)




ESTADOS=(('C',_('Comunicada')),('P',_('Pendiente')),('S',_('Solucionada')))

class GestorIncidencias(BaseAPPCC):
    appcc          = models.ForeignKey(APPCC)
    fincidencia    = models.DateField(verbose_name=_("F. Incidendia"))
    festado        = models.DateField(verbose_name=_("F. Resolucion"),null=True,blank=True)
    estado         = models.CharField(max_length=1,choices=ESTADOS)
    denominacion   = models.CharField(max_length=200,verbose_name=_("Incidencia"))
    observaciones  = models.TextField(verbose_name=_("Descripción de la incindencia"),blank=True,null=True,help_text=_("Descripción amplia de la incidencia"))
    personal       = models.ForeignKey(Personal,blank=True,null=True,verbose_name=_("Personal"),help_text=_("Persona encargada incidencia"),on_delete=models.PROTECT)
    etapa          = models.ForeignKey(Etapas,verbose_name=_("Etapa"),help_text=_("Etapa del cuadro de gestión"),on_delete=models.PROTECT)
    equipo         = models.ForeignKey(CatalogoEquipos,related_name="incidencias_equipos",verbose_name=_("Equipos o Instalación"),blank=True,null=True,on_delete=models.PROTECT)
    zonas          = models.ForeignKey(Zonas,blank=True,null=True,verbose_name=_(u"Zonas"),on_delete=models.PROTECT)
    tpmedactc      = models.ForeignKey(TiposMedidasActuacion, related_name="incidencias_correctiva",verbose_name=_("Medidas de Actuación Correctora"),blank=True,null=True,on_delete=models.PROTECT)
    tipogenera     = models.CharField(max_length=1,verbose_name="Tipo de Generación",null=True,blank=True)

    def urlDocumentos(self):
        #return '/appcc/documentos/lista/gestincid_id/%s/' % (self.pk)
        return '/appcc/appcc/gestorincidencias/%s/documentos/gestincid_id/%s/' % (self.appcc.id,self.pk)

    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/0/%s/' % (nombmodelo,self.pk)

    def get_absolute_url(self):
        #return reverse('gestorincidencias_actualizar',args=[self.pk])
        return reverse('gestorincidencias_actualizar',args=[self.appcc.id,self.pk])

    def nomestado(self):
        return filter((lambda x: x[1] if x[0]==self.estado else None), ESTADOS)[0][1]


class CabAnaliticas(BaseAPPCC):
    cabreg        = models.ForeignKey(CabRegistros,on_delete=models.PROTECT)
    cuadgestion   = models.ForeignKey(CuadrosGestion,related_name="cabana_cuadgest",verbose_name=_('Tipos de Procesos'),on_delete=models.PROTECT)
    denominacion  = models.CharField(max_length=200,verbose_name=_('Denominacion'))
    fecha         = models.DateField(verbose_name=_('Fecha'),help_text=_("Fecha Analitica"))
    laboratorio   = models.ForeignKey(Terceros, verbose_name=_("Laboratorio"))
    lotes         = models.ForeignKey('trazabilidad.Lotes',verbose_name=_("No. de Lote de la muestra"),null=True,blank=True)
    observaciones = models.TextField(verbose_name=_("Observaciones"),null=True,blank=True)

    def __unicode__(self):
        return "%s | %s | %s" % (self.denominacion,self.fecha,self.proceso)

    def denominacion_fecha(self):
        return ("%s - %s" % ( self.fecha,self.denominacion))

    def urlDocumentos(self):
        #return '/appcc/documentos/lista/cabanali_id/%s/' % (self.pk)
        return '/appcc/appcc/manualautocontrol/%s/cabregistros/%s/cabanaliticas/%s/documentos/cabanali_id/%s/' % (self.cabreg.manautctrl.appcc.id,self.cabreg.manautctrl.id,self.cabreg.id,self.pk)

    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/0/%s/' % (nombmodelo,self.pk)

    def get_absolute_url(self):
        #return reverse('cabanaliticas_actualizar',args=[self.pk])
        return reverse('cabanaliticas_actualizar',args=[self.cabreg.manautctrl.appcc.id,self.cabreg.manautctrl.id,self.cabreg.id,self.pk])

    class Meta:
        verbose_name_plural = _("Analiticas")
        verbose_name        = _("Analitica")

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","denominacion__icontains")

class DetAnaliticas(models.Model):
    cabanalitica  = models.ForeignKey(CabAnaliticas)
    parametros    = models.ForeignKey(ParametrosAnalisis, verbose_name=_('Parametros Analisis'))
    valores       = models.CharField(max_length=20, verbose_name=_('Valores'))


    class Meta:
        verbose_name_plural = _("Detalles Analiticas")
        verbose_name        = _("Detalle Analitica")


    def __unicode__(self):
        return "%s | %s " % (self.parametros,self.valores)

class CabInformesTecnicos(BaseAPPCC):
    appcc           = models.ForeignKey(APPCC,on_delete=models.PROTECT)
    establecimiento = models.CharField(max_length=200,verbose_name=_('Establecimiento') )
    expediente      = models.CharField(max_length=100,verbose_name=_('Expediente'))
    responsable     = models.ForeignKey(Personal, verbose_name=_('Responsable'), related_name='personal_responsable',on_delete=models.PROTECT)
    auditor         = models.ForeignKey(Personal, verbose_name=_('Auditor'),related_name='personal_auditor',on_delete=models.PROTECT)
    fecha           = models.DateField()
    legislacion     = models.ForeignKey(TiposLegislacion)

    def get_absolute_url(self):
        #return reverse('cabinftecnicos_actualizar',args=[self.pk])
        return reverse('cabinftecnicos_actualizar',args=[self.appcc.id,self.pk])

    def denominacion(self):
        return ("%s - %s - %s " % ( self.fecha,self.establecimiento,self.expediente) )

    def urlDocumentos(self):
        #return '/appcc/documentos/lista/cabinftec_id/%s/' % (self.pk)
        return '/appcc/appcc/auditorias/%s/documentos/cabinftec_id/%s/' % (self.appcc.id,self.pk)

    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/0/%s/' % (nombmodelo,self.pk)


    class Meta:
        verbose_name_plural = _("Informes Técnicos")
        verbose_name        = _("Informe Técnico")

class DetInformesTecnicos(models.Model):
    cabifortec  = models.ForeignKey(CabInformesTecnicos,on_delete=models.PROTECT)
    titulo      = models.CharField(max_length=500,verbose_name=_('Titulo'))
    texto       = models.TextField(verbose_name=_('Texto'))
    orden       = models.IntegerField()
    imagen = GenericRelation(Imagen)
    
    def get_model(self):
        return self.__class__.__name__.lower()
    def get_imagen(self):
        ct = ContentType.objects.filter(model=self.get_model())
        #img = Imagen.objects.get(content_type=ct.first(),object_id=self.pk)
        img = get_object_or_404(Imagen,content_type=ct.first(),object_id=self.pk)
        img = obtenerImagen(img)
        imgStr = "data:{ct};base64,{fi}".format(ct=img.content_type_file, fi=img.file)
        return imgStr
    def hay_imagenes(self):
        #if Propiedades.objects.filter(modelo=self.__class__.__name__,modelo_id=self.pk).count() > 0:
        ct = ContentType.objects.filter(model=self.get_model())
        print Imagen.objects.filter(content_type=ct.first(),object_id=self.pk)
        if Imagen.objects.filter(content_type=ct.first(),object_id=self.pk).count() > 0:
            return True
        else:
            return False


from south.modelsinspector import add_introspection_rules
rules = [
    (
        (PrivateFileField,),
        [],
        {
            "attachment" : ["attachment", {"default": True}],
        },
    )]

add_introspection_rules(
    rules,
    ["^private_files\.models\.fields\.PrivateFileField"])






class Documentos(RenameFilesModel):
    fecha        =  models.DateField(verbose_name=_("Fecha"))
    denominacion =  models.CharField(max_length="200", verbose_name=_("Denominación"))
    contenido    =  models.TextField(null=True,blank=True)
    archivos      = PrivateFileField( "file", upload_to='appcc',blank=True,null=True,help_text=_("Tamaño maximo 2.5 MB"),attachment=False,condition=is_owner)
    appcc        =  models.ForeignKey(APPCC, null=True,blank=True, verbose_name=_("APPCC"),on_delete=models.PROTECT)
    manautctrl   =  models.ForeignKey(ManualAutoControl, verbose_name=_("Manual de Autocontrol"),null=True,blank=True,on_delete=models.PROTECT)
    planautoctrl =  models.ForeignKey(PlanAutoControl, verbose_name=_("Plan de Autocontrol"),null=True,blank=True,on_delete=models.PROTECT)
    cabreg       =  models.ForeignKey(CabRegistros, verbose_name=_("Inicio de Registro"),null=True,blank=True,on_delete=models.PROTECT)
    detreg       =  models.ForeignKey(DetallesRegistros, verbose_name="Detalles de Registros",null=True,blank=True,on_delete=models.PROTECT)
    registros    =  models.ForeignKey(Registros, verbose_name=_("Registros"),null=True,blank=True,on_delete=models.PROTECT)
    cuadgest     =  models.ForeignKey(CuadrosGestion,verbose_name="Cuad.Gestion",null=True,blank=True,on_delete=models.PROTECT)
    relentes     =  models.ForeignKey(RelacionesEntes,verbose_name=_("Rel. Entes"),null=True,blank=True,on_delete=models.PROTECT)
    gestincid    =  models.ForeignKey(GestorIncidencias,verbose_name=_("Gestor Incidencias"),null=True,blank=True,on_delete=models.PROTECT)
    cabanali     =  models.ForeignKey(CabAnaliticas,verbose_name=_("Analiticas"),null=True,blank=True,on_delete=models.PROTECT)
    cabinftec    =  models.ForeignKey(CabInformesTecnicos,verbose_name=_("Informes Técnicos"),null=True,blank=True,on_delete=models.PROTECT)
    fechaproceso =  models.DateField(verbose_name="Fecha de Proceso convesion", blank=True, null=True)
    nodescargas  =  models.PositiveIntegerField("total descargas", default = 0,blank=True, null=True)
    RENAME_FILES        = {
        'archivos': {'dest': 'appcc', 'keep_ext': True},
        }

    def get_absolute_url(self):
        return reverse('documentos_actualizar',args=[self.pk])

    def verDocumento(self):
       if len(self.archivos.name)!=0:
        URL_DOCUMENTOS = "/documental/%s/Documentos/archivos/%s/%s"% (self.archivos.name.split('/')[0],self.pk,self.archivos.name.split('/')[1])
        return  """<button type="button" class="btn btn-info btn-mini" onclick="window.open('%s'); return false;">Archivo</button>""" % URL_DOCUMENTOS
       else:
        return ""

def handle_pre_download(instance, field_name, request, **kwargs):
    if instance.nodescargas is None:
        instance.nodescargas =1
    else:
        instance.nodescargas += 1
    instance.save()

pre_download.connect(handle_pre_download, sender = Documentos)

class Configuracion(BaseAPPCC):
    operador = models.ForeignKey(Terceros,on_delete=models.PROTECT)
    activar  = models.CharField(max_length=1, choices=(('S',_('Si')),('N',_('No'))))

    class Meta:
        verbose_name_plural = _('Configuraciones')
        verbose_name        = _('Configuracion')


OPCIONES_DIAS_1 = (('L',_('Lunes a Viernes')),('F',_('Fin de Semana')),('5',_('Sabado')),('6',_('Domingo')),('0',_('Lunes')),('1',_('Martes')),('2',_('Miercoles')),('3',_('Jueves')),('4',_('Viernes')))
class DetalleConfiguracion(models.Model):
    configuracion =  models.ForeignKey(Configuracion,on_delete=models.PROTECT)
    personas      =  models.ManyToManyField(Personal, verbose_name=_("Personas"),help_text=_("a efectos de avisos"))
    registros     =  models.ManyToManyField(CabRegistros, verbose_name="Registros a Supervisar")
    accion        =  models.CharField(max_length=1, choices=(('I',_('Incidencias')),('A',_('EMAIL')),('T',_('EMAIL/Incidencias')),('S',_('SMS')),( 'Z',_('SMS/EMAIL')) ), verbose_name=_("Acción a realizar" ) )
    habilitar     =  models.CharField( verbose_name=_("Habilitar"),max_length=1, choices=(('S',_('Si')),('N',_('No'))))
    dias          =  models.CharField(max_length=1,choices=OPCIONES_DIAS_1, null=True,blank=True, verbose_name="Dias Activa")
    turnos        =  models.ForeignKey(TiposTurnos, blank=True, null=True, verbose_name="Horario Desactiva")
