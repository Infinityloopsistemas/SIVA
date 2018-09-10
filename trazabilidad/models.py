# -*- coding: utf-8 -*-
import string
import datetime
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import F
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _
from private_files import PrivateFileField, pre_download
from maestros.models import Zonas, TiposProcesos, Terceros
from maestros_generales.models import Empresas, ZonasFao, TiposDocumentos
from productos.models import Productos
from siva import settings
from siva.utils import SI_NO, RenameFilesModel, is_owner


class BaseTrazabilidad(models.Model):
    fechaalta     = models.DateField(verbose_name=_("Fecha Alta"))
    fechabaja     = models.DateField(verbose_name=_("Fecha Baja"), blank=True,null=True)
    empresa       = models.ForeignKey(Empresas,null=True, blank=True,verbose_name=_('Empresa'),on_delete=models.PROTECT)
    user          = models.ForeignKey(User,on_delete=models.PROTECT)

#     def save(self, *args, **kwargs):
#         self.fechaalta=datetime.date.today()
#         super(BaseTrazabilidad, self).save(*args, **kwargs)
    def save(self, user=None, *args, **kwargs):
        self.fechaalta=datetime.date.today()
        if user is not None:
            self.user= User.objects.get(username=user)
            if  self.user.is_staff==True:
                self.empresa = Empresas.objects.get(usuario=self.user)                
            else:
                raise PermissionDenied
        super(BaseTrazabilidad, self).save(*args, **kwargs)


    class Meta:
        abstract = True

class Albaran(BaseTrazabilidad):
    tpdoc         = models.ForeignKey(TiposDocumentos, verbose_name=_("Tipo de Documento"))
    fecha         = models.DateField(verbose_name=_('Fecha'))
    referencia    = models.CharField(max_length=50,verbose_name=_('Num.Alba, S/Ref'))
    proveedor = models.ForeignKey(Terceros,verbose_name=_('Proveedor'), null=True)
    observaciones = models.TextField(verbose_name=_('Observaciones'),blank=True,null=True)
    fecha_cierre  = models.DateField(verbose_name=_('Fecha Cierre'),blank=True, null=True)
 
    def denominacion(self):
        return "%s | %s | Fecha: %s" % (self.tpdoc.denominacion, self.referencia, self.fecha )
 
    def __unicode__(self):
        return "%s | %s " % (self.tpdoc,self.referencia, )
 
    class Meta:
        verbose_name_plural = _("Albaranes")
        verbose_name        = _("Albaran")
 
    def get_absolute_url_entrada(self):
        return reverse('albaranentrada_actualizar',args=[self.pk])
    def get_absolute_url_salida(self):
        return reverse('albaransalida_actualizar',args=[self.pk])
 
    def urlDocumentos(self):
        return '/trazabilidad/documentos/lista/albaran_id/%s/' % (self.pk)
 
 
 
 
class Lotes(BaseTrazabilidad):
    producto = models.ForeignKey(Productos,verbose_name=_('Producto'),on_delete=models.PROTECT,blank=True, null=True)
    referencia       = models.CharField(max_length=50,verbose_name=_('Referencia Lote'),null=True,blank=True)
    fechacaducidad         = models.DateField(verbose_name=_('Fecha Caducidad'),help_text="Fecha caducidad")
    templote      = models.CharField(max_length=10,verbose_name=_('Temp.Lote'),blank=True, null=True)
    carorganolep  = models.CharField(max_length=200,verbose_name=_('Organolepticas'),blank=True, null=True)
    observaciones = models.TextField(verbose_name=_('Observaciones'),blank=True,null=True)
    cantidad      = models.IntegerField(verbose_name=_("Unidades"), blank=True, null=True)
    peso          = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True, verbose_name=_("Peso"))
    volumen       = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True, verbose_name=_("Volumen"))
    pesobulto     = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True, verbose_name=_("Peso/Unidad"))
 
    def denominacion(self):
        return ("%s | %s") % (self.referencia,self.producto)
 
    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/0/%s/' % (nombmodelo,self.pk)
 
    def urlDocumentos(self):
        return '/trazabilidad/documentos/lista/lotes_id/%s/' % (self.pk)
 
    def get_absolute_url(self):
        return reverse('lotes_actualizar',args=[self.pk])
 
    def __unicode__(self):
        detalb = DetalleAlbaran.objects.filter(lote__pk=self.pk)
        print detalb
        if detalb.count() > 0:
            stock = StockActual.objects.get(id=self.pk)
            if stock.cant > 0:
                max = "Max. cantidad (%s)" %  stock.cant
            elif stock.peso > 0:
                max = "Max. peso (%s)" %  stock.peso
            else:
                max = "Sin stock"
            return "%s | %s | %s " % (self.referencia,self.producto,max,)
        return "%s | %s | Sin introducir stock" % (self.referencia,self.producto,)
 
#     def save(self, force_insert=False, force_update=False, using=None):
#         super(Lotes, self).save(force_insert, force_update)
#         if len(self.numlote)==0:
#             self.numlote = self.albaran.serlote.serie+string.zfill(str(self.albaran.id),7)+string.zfill(str(self.pk),7)
#             super(Lotes, self).save(force_insert, force_update)
 
    class Meta:
        verbose_name_plural = _("Lotes")
        verbose_name        = _("Lote")
 
 
class DetalleAlbaran(BaseTrazabilidad):
    albaran       = models.ForeignKey(Albaran,verbose_name=_('Albaran'),on_delete=models.PROTECT)
    lote          = models.ForeignKey(Lotes,verbose_name=_('Lote'),on_delete=models.PROTECT)
    referencia    = models.CharField(max_length=50,verbose_name=_('Ref.'),null=True,blank=True)
    producto       = models.ForeignKey(Productos,verbose_name=_('Producto'),on_delete=models.PROTECT)
    cantidad       = models.IntegerField(verbose_name=_("Cantidad"), blank=True, null=True)
    peso           = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True, verbose_name=_("Peso"))
    volumen        = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True, verbose_name=_("Volumen"))
    pesobulto      = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True, verbose_name=_("Peso/Bulto"))
 
    class Meta:
        verbose_name_plural = _("Detalles Lotes")
        verbose_name        = _("Detalle Lote")


class Documentos(RenameFilesModel):
    fecha        =  models.DateField(verbose_name=_("Fecha"))
    denominacion =  models.CharField(max_length="200", verbose_name=_("Denominación"))
    contenido    =  models.TextField(null=True,blank=True)
    archivos     =  PrivateFileField( "file", upload_to='trazabilidad',blank=True,null=True,help_text=_("Tamaño maximo 2.5 MB"),attachment=False,condition=is_owner)
    #cuadcampo    =  models.ForeignKey(CuadernoCampo, verbose_name=_("Cuaderno"),null=True,blank=True,on_delete=models.PROTECT)
    albaran      =  models.ForeignKey(Albaran, verbose_name=_("Albaran"),null=True,blank=True,on_delete=models.PROTECT)
    lotes        =  models.ForeignKey(Lotes, verbose_name=_("Lotes"),null=True,blank=True,on_delete=models.PROTECT)
    fechaproceso =  models.DateField(verbose_name="Fecha de Proceso conversion", blank=True, null=True)
    nodescargas  =  models.PositiveIntegerField("total descargas", default=0, blank=True, null=True)

    RENAME_FILES        = {
        'archivos': {'dest': 'trazabilidad', 'keep_ext': True},
        }

    def get_absolute_url(self):
        return reverse('tdocumentos_actualizar',args=[self.pk])

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


class StockActual(models.Model):
    id = models.IntegerField(verbose_name=_("Lote id"), primary_key=True)
    referencia = models.TextField(verbose_name=_("REF. Lote"))
    producto_id = models.IntegerField(verbose_name=_("Producto id"))
    producto = models.TextField(verbose_name=_("Producto"))
    fechacaducidad         = models.DateField(verbose_name=_('Fecha Caducidad'),help_text="Fecha caducidad")
    empresa_id = models.IntegerField(verbose_name=_("Empresa id"))
    empresa = models.TextField(verbose_name=_("Nombre empresa"))
    cant      = models.IntegerField(verbose_name=_("Cantidad"), blank=True, null=True)
    peso = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True, verbose_name=_("Peso"))
    class Meta:
        db_table='trazabilidad_stockactual'
        managed = False
