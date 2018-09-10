# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _
from maestros.models import Unidades
from maestros_generales.models import Marcas, Empresas, Ingredientes
from siva.utils import SI_NO


class BaseProductos(models.Model):
    fechaalta     = models.DateField(verbose_name=_("Fecha Alta"),blank=True)
    fechabaja     = models.DateField(verbose_name=_("Fecha Baja"), blank=True,null=True)
    empresa       = models.ForeignKey(Empresas,null=True, blank=True,verbose_name=_('Empresa'),on_delete=models.PROTECT)
    user          = models.ForeignKey(User,blank=True, null=True,on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.fechaalta=datetime.date.today()
        super(BaseProductos, self).save(*args, **kwargs)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse( '%s_actualizar' % self.__class__.__name__.lower()  ,args=[self.pk])

    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/0/%s/' % (nombmodelo,self.pk)



class Canales(BaseProductos):
    denominacion = models.CharField(max_length=100, blank=True,verbose_name=_('Canal de Comercializacion') )

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","descripcion__icontains")

    class Meta:
        verbose_name_plural ="Canales"

    def __unicode__(self):
        return "%s" % (self.denominacion)


#class PartidasArancelarias(models.Model):
#    descripcion         = models.CharField(max_length=100,verbose_name=(_('Aranceles')))
#    codigo_estadistico  = models.CharField(max_length=10,verbose_name=(_('Codigo Estadistico')))
#
#    @staticmethod
#    def autocomplete_search_fields():
#        return ("id__iexact","descripcion__icontains")
#
#    class Meta:
#        ordering =['descripcion']
#
#    def __unicode__(self):
#        return "%s - %s" % (self.descripcion, self.codigo_estadistico)



class Grupos(BaseProductos):
    denominacion = models.CharField(max_length=100)

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","denominacion__icontains")

    class Meta:
        ordering =['denominacion']
        verbose_name_plural =_("Grupos")

    def __unicode__(self):
        return "%s"%(self.denominacion)


class Tipos(BaseProductos):
    denominacion = models.CharField( max_length=100,verbose_name=_('Tipos'))

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","denominacion__icontains")

    class Meta:
        verbose_name_plural =_("Tipos")
        ordering =['denominacion']

    def __unicode__(self):
        return "%s"%(self.denominacion)



class Familias(BaseProductos):
    denominacion = models.CharField(max_length=100)
    grupos       = models.ForeignKey(Grupos,on_delete=models.PROTECT, verbose_name="Grupos")

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","denominacion__icontains")

    class Meta:
        ordering =['denominacion']
        verbose_name_plural =_("Familias")

    def __unicode__(self):
        return "%s" % (self.denominacion)



class Denominacion(BaseProductos):
    denominacion = models.CharField(unique=True, max_length=100, blank=True, verbose_name=_("Descripcion"))
    dcientifico  = models.CharField(max_length=100, blank=True,verbose_name=_("Cientifico"))
    familias     = models.ForeignKey(Familias,verbose_name=_("Familia"),on_delete=models.PROTECT, related_name="denomina_familia")
    #p_arancela_p_arancela = models.ForeignKey(PartidasArancelarias,verbose_name=_("Partida Arancel"))
    url          = models.URLField(verbose_name=_('Url'),null=True,blank=True)
    descripcion  = models.TextField(null=True,blank=True,verbose_name=_("Descripción del Producto"))

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","denominacion__icontains")

    class Meta:
        verbose_name_plural = _("Denomiación Comercial")
        ordering =['denominacion']

    def __unicode__(self):
        return "%s"%(self.denominacion)



class TiposEnvases(BaseProductos):
    denominacion     = models.CharField(unique=True, max_length=100, blank=True,verbose_name=('Denominacion'))
    f_master         = models.DecimalField(unique=True, null=True, max_digits=15, decimal_places=5, blank=True, verbose_name=_('Factor Master'))
    peso_ud          = models.DecimalField(null=True, max_digits=15, decimal_places=5, blank=True, verbose_name=_('Peso Unidad'))
    peso_envase      = models.DecimalField(null=True, max_digits=15, decimal_places=5, blank=True,verbose_name =_('Peso Envase'))
    agranel          = models.CharField(max_length=1, blank=True, choices=SI_NO, verbose_name="Granel")
    volumen          = models.DecimalField(null=True, max_digits=7, decimal_places=3, blank=True,verbose_name=_('Volumen'), help_text=_('En m3 cubicos'))
    unidadesporpalet = models.IntegerField(null=True, blank=True,verbose_name =_('Unidades por Palet'))
    filasporpalet    = models.IntegerField(null=True, blank=True,verbose_name =_('Filas por Palet'))

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","denominacion__icontains")

    class Meta:
        verbose_name_plural =_("Envases")
        ordering =['denominacion']

    def __unicode__(self):
        return "%s"%(self.denominacion)



class Dimensiones(BaseProductos):
    unidades         = models.ForeignKey(Unidades,null=True, blank=True,verbose_name=_('Unidades de Medidas'),on_delete=models.PROTECT)
    denominacion     = models.CharField(unique=True, max_length=100, verbose_name='Descripcion')
    maximo           = models.DecimalField(null=True, max_digits=15, decimal_places=5, blank=True,verbose_name=('Maximo'))
    minimo           = models.DecimalField(null=True, max_digits=15, decimal_places=5, blank=True,verbose_name=('Minimo'))
    piezas           = models.CharField(max_length=50, blank=True,null=True, verbose_name=_('Piezas'))
    alto             = models.DecimalField(null=True, max_digits=15, decimal_places=5, blank=True,verbose_name=('Alto'))
    largo            = models.DecimalField(null=True, max_digits=15, decimal_places=5, blank=True,verbose_name=('Largo'))
    ancho            = models.DecimalField(null=True, max_digits=15, decimal_places=5, blank=True,verbose_name=('Ancho'))

    @staticmethod
    def autocomplete_search_fields(self):
        return ("id__iexact","denominacion__icontains")

    class Meta:
        ordering =['denominacion']
        verbose_name_plural =_("Dimensiones")

    def __unicode__(self):
        return "%s"%(self.denominacion)




class Productos(BaseProductos):
    dimension          = models.ForeignKey(Dimensiones ,verbose_name=_('Dimensiones') ,on_delete=models.PROTECT)
    denomina           = models.ForeignKey(Denominacion,verbose_name=_('Denominación'),on_delete=models.PROTECT)
    tipo               = models.ForeignKey(Tipos,verbose_name=_('Tipos'),on_delete=models.PROTECT)
    canal              = models.ForeignKey(Canales,null=True, blank=True, verbose_name=_('Canal'), on_delete=models.PROTECT)
    envase             = models.ForeignKey(TiposEnvases,null=True, blank=True,verbose_name=_('Envase'),on_delete=models.PROTECT)
    elaborado          = models.CharField(max_length=1, blank=True, choices=SI_NO)
    marca              = models.ForeignKey(Marcas,null=True, blank=True,verbose_name=_('Procedencia'), on_delete=models.PROTECT )
    codeancaja         = models.CharField(max_length=255, blank=True,   verbose_name=_("Codigo EAN MASTER"))
    codeanproducto     = models.CharField(max_length=255, blank=True,   verbose_name=_("Codigo EAN"))
    regsanitario       = models.CharField(max_length=255, blank=True,   verbose_name=_("Reg.Sanitario"))


    def denominacion(self):
        return ("%s %s " %  (self.denomina,self.tipo) )


    def __unicode__(self):
        return u'%s %s %s %s'%(self.denominacion,self.tipo,self.dimension,self.envase)

    class Meta:
        verbose_name_plural = _("Productos")
        verbose_name = _("Producto")
        ordering =['denomina','tipo']

class Composicion(models.Model):
    productos     = models.ForeignKey(Productos,verbose_name=_("Productos"))
    ingredientes  = models.ForeignKey(Ingredientes,verbose_name=_("Ingredientes"))
    cantidad      = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_("Cantidad"))

    class Meta:
        verbose_name_plural = _("Composciones")
        verbose_name = _("Composicion")





# class Vista_Productos(models.Model):
#     id              = models.IntegerField(primary_key=True)
#     producto        = models.CharField(max_length=403,verbose_name='Producto')
#     familias        = models.CharField(max_length=100,verbose_name='Familias')
#     denominacion    = models.CharField(max_length=100,verbose_name='Especies')
#     tipos           = models.CharField(max_length=100,verbose_name='Tipos')
#     dimension       = models.CharField(max_length=100,verbose_name='Dimension')
#     envases         = models.CharField(max_length=100,verbose_name='Envases')
#     grupos          = models.CharField(max_length=100,verbose_name='Grupos')
#     partidasarancel = models.CharField(max_length=100,verbose_name='Arnacel')
#     marcas          = models.CharField(max_length=100,verbose_name='Marcas')
#     umedidas        = models.CharField(max_length=100,verbose_name='U.Medidas')
#     canales         = models.CharField(max_length=100,verbose_name="Canal")
#
#     @staticmethod
#     def autocomplete_search_fields():
#         return ("id__iexact","producto__icontains","especies__icontains")
#
#     def __unicode__(self):
#         return u'%s' % self.producto
#
#     class Meta:
#         db_table = u'v$productos'
#         managed=False
#         verbose_name_plural = _("Vista Productos")
#         verbose_name        = _("Vista Producto")
#         ordering            = ['denominacion','tipos']






