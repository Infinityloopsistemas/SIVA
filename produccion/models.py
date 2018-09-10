from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _

# Create your models here.

SI_NO=(('S','Si'),('N','No'),)

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



class TiposAnaliticas(models.Model):
    descripcion = models.CharField(max_length=200,verbose_name=_('Recuento'))
    valoresmax  = models.CharField(max_length=200,verbose_name=_('Limite'))

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","descripcion__icontains",)

    def __unicode__(self):
        return unicode(self.descripcion)

    class Meta:
        verbose_name_plural = _('Tipos de Analiticas')
        verbose_name        = _('Tipo de Analitica')



class TiposUbicaciones(MPTTModel):
    descripcion = models.CharField(max_length=200,verbose_name=_('Ubicacion'))
    limita_up    = models.ForeignKey('self',null=True, blank=True,related_name="rel_up",verbose_name=_("Arriba"))
    limita_down  = models.ForeignKey('self',null=True, blank=True,related_name="rel_down",verbose_name=_("Abajo"))
    limita_right = models.ForeignKey('self',null=True, blank=True,related_name="rel_right",verbose_name=_("Derecha"))
    limita_left  = models.ForeignKey('self',null=True, blank=True,related_name="rel_left",verbose_name=_("Izquierda"))
    parent      = TreeForeignKey('self', null=True,blank=True,related_name="padre_hijos_ubica",verbose_name=_("Contenido en"))

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","descripcion__icontains",)

    class Meta:
        verbose_name_plural = _('Tipos Ubicaciones')
        verbose_name        = _('Tipo Ubicacion')

    def __unicode__(self):
        return "%s | %s "  % (self.descripcion,self.parent)



class TiposProcesos(models.Model):
    descripcion = models.CharField(max_length=200,verbose_name=_('Tipo de Proceso'))
    pesado      = models.CharField(max_length=1, choices=SI_NO )
    etiquetado  = models.CharField(max_length=1, choices=SI_NO)
    falta       = models.DateField(verbose_name=_('F.Alta'))
    fbaja       = models.DateField(verbose_name=_('F.Baja'),blank=True,null=True)
    nivel       = models.CharField(max_length=1,verbose_name=_('Nivel'),choices=(('E',_('Entrada')),('I',_('Intermedio')),('S',_('Salida'),)))

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","descripcion__icontains",)

    def __unicode__(self):
        return unicode(self.descripcion)

    class Meta:
        verbose_name_plural = _('Tipos de Procesos')
        verbose_name        = _('Tipo de Proceso')

#Descripcion del tipo de proceso para la linea de produccion
class CabProcesos(models.Model):
    descripcion = models.CharField(max_length=200, help_text=_("Descripcion del Proceso") )
    falta       = models.DateField(verbose_name=_('F.Alta'))
    fbaja       = models.DateField(verbose_name=_('F.Baja'),blank=True,null=True)


    class Meta:
        verbose_name_plural = _('Cabecera de Procesos')
        verbose_name        = _('Cabecera de Proceso')

    def __unicode__(self):
        return unicode(self.descripcion)

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","descripcion__icontains",)


class DetProcesos(MPTTModel):
    cabprocesos = models.ForeignKey(CabProcesos)
    descripcion = models.CharField( max_length=200, verbose_name=_('Descripcion'))
    tproceso    = models.ForeignKey(TiposProcesos, verbose_name=_('Tipo de Proceso'))
    tpubicacion = models.ForeignKey(TiposUbicaciones,verbose_name =_('Ubicacion'), blank=True, null=True)
    parent      = TreeForeignKey('self', null=True,blank=True,related_name="padre_hijos",verbose_name="Proceso Padre")



    class Meta:
        verbose_name_plural = _('Detalles de Procesos')
        verbose_name        = _('Detalle de Proceso')

    def __unicode__(self):
        return "%s | %s "  % (self.cabprocesos,self.tproceso)

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","descripcion__icontains",)