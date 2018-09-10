# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
import datetime
import sys

# Create your models here.

from siva import settings
#from maestros.models import Terceros


class BaseMaestrosGenerales(models.Model):
    fechaalta   = models.DateField(verbose_name=_('F.Alta'))

    def save(self, *args, **kwargs):
        self.fechaalta=datetime.date.today()
        super(BaseMaestrosGenerales, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class TiposDocumentos(BaseMaestrosGenerales):
    denominacion = models.CharField(max_length=100,verbose_name=_("Descripción"))
    abrv         = models.CharField(max_length=10, verbose_name= _("Abreviado"))

    def  __unicode__(self):
        return unicode(self.abrv)

    def get_absolute_url(self):
        return reverse('tiposdocumentos_actualizar',args=[self.pk])


class TiposImpuestos(BaseMaestrosGenerales):
    descripcion = models.CharField(max_length=100, verbose_name=_('Descripcion'),help_text =_("Denominacion del tipo de impuesto"))
    epigrafe    = models.CharField(max_length=100, verbose_name=_('Epigrafe')   ,help_text = _("Epigrafe para el que se ha reconocido el tipo de impuesto"))
    aplica      = models.CharField(max_length=1,   verbose_name=_('Aplica a')   ,choices=( ('1',_('Nivel Global')),('2',_('Nivel Detalle'))), help_text= _("Impuesto a donde se aplica"))
    valor       = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True, verbose_name=_('Valor'),help_text=_("Tipo Impositivo"))

    def denominacion(self):
        return self.descripcion

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","descripcion__icontains")



    def __unicode__(self):
        return unicode(self.descripcion)

    class Meta:
        ordering = ('descripcion',)
        verbose_name_plural = _("Tipos de Impuestos")
        verbose_name = _("Tipo de Impuesto")


    def get_absolute_url(self):
        return reverse('tiposimpuestos_actualizar',args=[self.pk])

class TiposTerceros(BaseMaestrosGenerales):
    descripcion = models.CharField(max_length=100, help_text=_("Denominacion del tercero, proeveedor, cliente, etc"),verbose_name=_("Tipo Tercero"))
    accion      = models.CharField(max_length=1, choices=( ('1',_('Proveedor')),('2',_('Cliente')),('3',_('Acreedor')),('4', _('Bancos')),('5',_('Admin. Publica') ),('6',_('Empresa')), ), verbose_name=_("Indicador"))


    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","descripcion__icontains")



    def denominacion(self):
        return self.descripcion

    def __unicode__(self):
        return unicode(self.descripcion)
    class Meta:
        ordering = ('descripcion',)
        verbose_name_plural = _("Tipos de Terceros")
        verbose_name = _("Tipo de Tercero")

    def get_absolute_url(self):
        return reverse('tiposterceros_actualizar',args=[self.pk])

class Paises(models.Model):
    isonum  = models.IntegerField(verbose_name=_("Iso Numero"))
    iso2    = models.CharField(max_length=2,verbose_name=_("Iso 2"))
    iso3    = models.CharField(max_length=3,verbose_name=_("Iso 3"))
    nombre  = models.CharField(max_length=100,help_text=_("Introduzca nombre del Pais"),verbose_name=_("Nombre Pais"))

    def denominacion(self):
        return self.nombre

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","nombre__icontains")


    def __unicode__(self):
        return unicode(self.nombre)
    class Meta:
        verbose_name_plural =_("Paises")
        verbose_name = _("Pais")

    def get_absolute_url(self):
        return reverse('paises_actualizar',args=[self.pk])

class Provincias(models.Model):
    codprovincia = models.CharField(max_length=3,verbose_name=_("Codigo Provincia"))
    nombre       = models.CharField(max_length=100, verbose_name =_("Provincia"))
    tipo         = models.CharField(max_length = 2, choices =(('x',_('Capital')), ('0', _('Ciudad')),('1', _('Mas Ciudad')),), verbose_name=_("Tipo"))
    pais         = models.ForeignKey(Paises, verbose_name="Pais",on_delete=models.PROTECT)
    def __unicode__(self):
        return unicode(self.codprovincia+' '+self.nombre)
    class Meta:
        verbose_name_plural = _("Provincias")
        ordering=['nombre']

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","nombre__icontains")

    def get_absolute_url(self):
        return reverse('provincias_actualizar',args=[self.pk])

    def denominacion(self):
        return self.nombre

class CodigosPostales(models.Model):
    codpostal = models.CharField(max_length=5, help_text= _("Codigo postal de la ciudad"), verbose_name=_("Codigo Postales"))
    provincia = models.ForeignKey(Provincias,verbose_name=_("Provincias"),on_delete=models.PROTECT)
    calle     = models.CharField(max_length=100,verbose_name=_("Calle"))

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","codpostal__icontains")


    def __unicode__(self):
        return unicode(self.codpostal)

    class Meta:
        verbose_name_plural = _("Codigos Postales")
        verbose_name = _("Codigo Postal")

    def get_absolute_url(self):
        return reverse('codigospostales_actualizar',args=[self.pk])

    def denominacion(self):
        return "%s %s" % (self.codpostal,self.provincia)

class Municipios(models.Model):
    municipio = models.CharField(max_length=255, verbose_name=_('Nombre Municipio'))
    provincia = models.ForeignKey(Provincias, verbose_name=_('Provincias'),on_delete=models.PROTECT)

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","municipio__icontains")

    def __unicode__(self):
        return unicode(self.municipio)

    class Meta:
        verbose_name_plural = _("Municipios")
        ordering = ['provincia','municipio']
        verbose_name = _("Municipio")

    def get_absolute_url(self):
        return reverse('municipios_actualizar',args=[self.pk])

    def denominacion(self):
        return self.municipio

class Festivos(models.Model):
    denominacion = models.CharField(max_length=255,verbose_name=_("Festivos"))
    fecha   = models.DateField(_("Fecha"))
    anio      = models.IntegerField(verbose_name="Año")
    
    class Meta:
        verbose_name        = "Festivo"
        verbose_name_plural = "Festivos"

    def __unicode__(self):
        return "%s" % (self.denominacion)


class Empresas(models.Model):
    descripcion = models.CharField(max_length=100, blank=True,verbose_name=_("Descripción"))
    url         = models.CharField(max_length=100, blank=True,verbose_name=_("Url"))
    nombrecomercial = models.CharField(max_length=100,null=True, blank=True,verbose_name=_("Nombre Comercial"))
    fechaalta   = models.DateField(_("Fecha de Alta"))
    fechabaja   = models.DateField(_("Fecha de Baja"), null=True, blank=True)
    habilitar   = models.BooleanField(verbose_name="Habilitar Empresa")
    usuario     = models.ManyToManyField(User)
    festivo = models.ManyToManyField(Festivos, verbose_name=_('Festivos'))
    class Meta:
        verbose_name        = "Empresa"
        verbose_name_plural = "Empresas"

    def __unicode__(self):
        return "%s" % (self.descripcion)

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","descripcion__icontains")

#     class Meta:
#         verbose_name_plural = _("Empresas")
#         verbose_name = _("Empresa")

    def denominacion(self):
        return self.descripcion

    def get_absolute_url(self):
        return reverse('empresas_actualizar',args=[self.pk])
    
    def direccion(self):
        from maestros.models import Terceros
        tipoTercero = TiposTerceros.objects.get(pk='9')
        terceros = Terceros.objects.filter(empresa_id=self.pk,tipotercero = tipoTercero).first()
        direccion = terceros.direccion1 + terceros.direccion2
        return direccion
    
    def hay_landing_page(self):
        from landing_page.models import CabLandingPage
        lp = CabLandingPage.objects.filter(empresa=self)
        if lp.count() > 0:
            return True
        return False
    def verRegistrosEmpresas(self):

        url = "%sappcc/imprimir/registrosEmpresa/%s" % (settings.URL_SERVER,self.id)         
        return '<a class="link" href="%s" target=_blank>  Ver registro empresa </a> ' % url
    verRegistrosEmpresas.short_description = "Ver registro empresa"
    verRegistrosEmpresas.allow_tags = True
	
    def entrarEmpresa(self):
        url = "%sadminempresa/%s"% (settings.URL_SERVER,self.id)
        return '<a class="link" href="%s">  Cambiar Empresa </a> ' % url

    entrarEmpresa.short_description = "Cambiar Empresa"
    entrarEmpresa.allow_tags = True

class EmpresasEdit(Empresas):
    class Meta:
        proxy = True
        app_label= "maestros_generales"
        verbose_name = "Empresas Edit"
        verbose_name_plural = "Empresas Edits"
        
class MetaUsuarios(models.Model):
    nombre = models.CharField(max_length=30, blank=True)
    usuario = models.ManyToManyField(User)
    class Meta:
        verbose_name        = "Meta Usuario"
        verbose_name_plural = "Meta Usuarios"

    def __unicode__(self):
        return "%s" % (self.nombre)

class Marcas(models.Model):
    descripcion = models.CharField(max_length=100, blank=True,verbose_name=_("Descripcion"))

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "descripcion__icontains",)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = _('Marcas')
        verbose_name        = _('Marca')
        ordering            = ['descripcion']

    def denominacion(self):
        return  self.descripcion

    def get_absolute_url(self):
        return reverse('marcas_actualizar',args=[self.pk])

class TipoPlanControl(models.Model):
    denominacion       = models.CharField(max_length=100,verbose_name=_("Denominacion"),help_text=_("Definicion del Tipo de Plan de Control"))
    habilitaregistros  = models.CharField(max_length=1, choices=(('S','Si'),('N','No')))
    habilitanaliticas  = models.CharField(max_length=1, choices=(('S','Si'),('N','No')))
    etiquetas          = models.TextField(verbose_name="Etiquetas confiuracion planes de auto control",null=True,blank=True)
    campoprimario      = models.CharField(max_length=20, choices=settings.SIVA_OPCION)
    def __unicode__(self):
        return self.denominacion

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","denominacion__icontains")

    class Meta:
        verbose_name_plural = _('Tipos de Planes de Control')
        verbose_name        = _('Tipo Plan de Control')

    def get_absolute_url(self):
        return reverse('tipoplancontrol_actualizar',args=[self.pk])


GRUPO = ( ('1','PERSONAL DIRECTIVO'),('2','PERSONAL NO SANITARIO (TITULADO)'),('3','PERSONAL ADMINISTRATIVO'),('4','PERSONAL SANITARIO (TITULADO)'),('5','PERSONAL SANITARIO (NO TITULADO)'),('6','PERSONAL SUBALTERNO'),('7','PERSONAL SERVICIOS GENERALES'),('8','PERSONAL OFICIOS VARIOS'),('9','APRENDICES Y ASPIRANTES'),('10','OTROS'))

class TiposCatProfesional(models.Model):
    grupo = models.CharField(max_length=2, choices=GRUPO)
    denominacion = models.CharField(max_length=200,verbose_name=_("Categoria Profesional"))

    def get_absolute_url(self):
        return reverse('tiposcatprofesional_actualizar',args=[self.pk])



class ZonasFao(models.Model):
    denominacion   = models.CharField(max_length=200, verbose_name=_('Denominacion'))
    zonasmaritimas = models.CharField(max_length=200, verbose_name=_('Zonas Maritimas'))
    url_zona       = models.URLField(verbose_name=_('Url ZonaFao'))

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","zonasmaritimas__icontains",)

    def __unicode__(self):
        return "%s" % ( self.zonasmaritimas)

    class  Meta:
        verbose_name_plural = _('Zonas Faos')
        verbose_name        = _('Zona Fao')

    def urlZonaFao(self):
        return '<a class="ajuste" href="%s" style="color:#FF0000">%s</a>' % ( self.url_zona,self.zonasmaritimas)

    urlZonaFao.allow_tags = True
    urlZonaFao.short_description = _('Zonas Maritimas')


class Ingredientes(models.Model):
    nombre             = models.CharField(max_length=255,verbose_name=_("Denomina Español"))
    nombingles         = models.CharField(max_length=255,verbose_name=_("Denomina Ingles"), null=True,blank=True)
    nombcientifico     = models.CharField(max_length=255,verbose_name=_("Nombre cientfico"), null=True,blank=True)

    def get_absolute_url(self):
        return reverse('ingredientes_actualizar',args=[self.pk])

    def denominacion(self):
        return ("%s - %s -%s"  % (self.nombre,self.nombingles,self.nombcientifico))

COMPONENTES =(('P',_('Proximales')),('H',_('Hidratos de Carbono')),('G',_('Grasas')),('V',_('Vitaminas')),('M',_('Minerales')))

class Componentes(models.Model):
    denominacion =  models.CharField(max_length=255,verbose_name=_("Componentes"))
    tipocompo    =  models.CharField(max_length=2,verbose_name="Tipo Componente",choices=COMPONENTES)

    def get_absolute_url(self):
        return reverse('componentes_actualizar',args=[self.pk])


UNIDADES =(('kcal','kcal'),('g','Gramos'),('mg','mg'),('micgr','mucgr'))
class ComposicionIngre(models.Model):
    ingrediente = models.ForeignKey(Ingredientes)
    componente  = models.ForeignKey(Componentes)
    valor       = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_("Valor"))
    unidades    = models.CharField(max_length=20,verbose_name="Unidades",choices=UNIDADES)
    fuente      = models.IntegerField(verbose_name="Fuente")






