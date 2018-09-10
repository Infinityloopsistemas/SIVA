from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from maestros.models import Terceros
from produccion.models import DetProcesos, TiposAnaliticas, CabProcesos
from productos.models import Productos, Vista_Productos
from django.utils.encoding import force_unicode
import string, os



class RenameFilesModel(models.Model):
    RENAME_FILES = {}
    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None):
        rename_files = getattr(self, 'RENAME_FILES', None)
        if rename_files:
            super(RenameFilesModel, self).save(force_insert, force_update)
            force_insert, force_update = False, True
            for field_name, options in rename_files.iteritems():
                field = getattr(self, field_name)
                file_name = force_unicode(field)
                name, ext = os.path.splitext(file_name)
                if len(ext)!=0 :
                    keep_ext = options.get('keep_ext', True)
                    final_dest = options['dest']
                    if callable(final_dest):
                        final_name = final_dest(self, file_name)
                    else:
                        final_name = os.path.join(final_dest, '%s' % (self.pk,))
                        if keep_ext:
                            final_name += ext
                    if file_name != final_name:
                        field.storage.delete(final_name)
                        field.storage.save(final_name, field)
                        field.storage.delete(file_name)
                        setattr(self, field_name, final_name)
        super(RenameFilesModel, self).save(force_insert, force_update)




class SeriesLotes(models.Model):
    serie       = models.CharField(max_length=4,   verbose_name="Serie")
    descripcion = models.CharField(max_length=100, verbose_name="Descripcion")
    class Meta:
        ordering = ('serie',)
        verbose_name = "Serie de Lotes"
        verbose_name_plural = "Series de Lotes"
    def __unicode__(self):
        return "%s | %s " % (self.serie,self.descripcion)

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","descripcion__icontains")





class Counter(models.Model):

    "Para generar ID Unicos http://djangosnippets.org/snippets/1574/"
    key     = models.CharField(max_length=50, primary_key=True)
    counter = models.IntegerField(default = 0)

    @classmethod
    def next(cls, userid, key = 'default'):
        "Increments and returns the next unused integer"
        try:
            cls.objects.filter(key = key, user=userid).update(counter = F('counter') + 1)
            return cls.objects.get(key = key, user=userid).counter
        except cls.DoesNotExist:
            # This could raise an integrity error in a race condition :/
            return cls.objects.create(key = key, user=userid, counter = 1).counter

    @classmethod
    def next_hex(cls, key = 'default'):
        return hex(cls.next(key)).replace('0x', '').replace('L', '')

    def __unicode__(self):
        return u'%s = %s' % (self.key, self.counter)

    class Meta:
        ordering = ('key',)
        verbose_name_plural = _("Contador")



class Procedencia(models.Model):
    descripcion   =  models.CharField(max_length=100,verbose_name=_('Denominacion'))
    tercero       = models.ForeignKey(Terceros,verbose_name=_('Terceros'))
    zonafao       = models.ForeignKey(ZonasFao,verbose_name=_('Zona Fao'))
    pesquero      = models.CharField(max_length=100,verbose_name=_('Pesquero'),blank=True,null=True)
    origen        = models.CharField(max_length=100,verbose_name=_('Origen'))
    medio         = models.CharField(max_length=100,verbose_name=_('Medio'),blank=True,null=True)
    fbaja         = models.DateField(verbose_name=_('Fecha Baja'),blank=True, null=True)
    formobtencion = models.CharField(max_length=30,choices=( ('Pesca Extractiva',_('Pesca Extractiva')),('Acuicultura',_('Acuicultura')),) )
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","descripcion__icontains")


    def __unicode__(self):
        return " %s | %s | %s | % s" % ( self.descripcion, self.zonafao,self.tercero,self.medio)

    class Meta:
        verbose_name_plural = "Procedencias"


class CabAnaliticas(RenameFilesModel):
    denominacion  = models.CharField(max_length=200,verbose_name=_('Denominacion'))
    proceso       = models.ForeignKey(DetProcesos,verbose_name=_('Tipos de Procesos'))
    fecha         = models.DateField(verbose_name=_('Fecha'))
    laboratorio   = models.ForeignKey(Terceros, verbose_name=_("Laboratorios"))
    docanalitica  = models.FileField( upload_to='analiticas',blank=True,null=True, verbose_name=_("Analitica (PDF)"))
    RENAME_FILES        = {
        'docanalitica': {'dest': 'analiticas', 'keep_ext': True},
        }

    def __unicode__(self):
        return "%s | %s | %s" % (self.denominacion,self.fecha,self.proceso)


    class Meta:
        verbose_name_plural = _("Analiticas")
        verbose_name        = _("Analitica")

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","denominacion__icontains")

class DetAnaliticas(models.Model):
    cabanalitica  = models.ForeignKey(CabAnaliticas)
    tipoanalitica = models.ForeignKey(TiposAnaliticas, verbose_name=_('Tipo Analitica'))
    valores       = models.CharField(max_length=20, verbose_name=_('Valores'))


    class Meta:
        verbose_name_plural = _("Detalles Analiticas")
        verbose_name        = _("Detalle Analitica")


    def __unicode__(self):
        return "%s | %s " % (self.tipoanalitica,self.valores)


class OrdenProduccion(models.Model):
    fecha         = models.DateField(verbose_name=_('Fecha'))
    cuadcampo     = models.ForeignKey(Procedencia,verbose_name=_('Procedencia'))
    cabprocesos   = models.ForeignKey(CabProcesos,verbose_name=_('Proceso'))
    serlote       = models.ForeignKey(SeriesLotes,verbose_name='Seri Lote')
    numalbaran    = models.CharField(max_length=50,verbose_name=_('Num.Alba, S/Ref'))
    observaciones = models.TextField(verbose_name=_('Observaciones'),blank=True,null=True)
    #estado
    fecha_cierre  = models.DateField(verbose_name=_('Fecha Cierre'),blank=True, null=True)

    def iralotes(self):
        return '<a href="http://127.0.0.1/trazabilidad/admin/Gestion/lotes/?e=%s" style="color:#FF0000">Lotes</a>' % (self.id)

    iralotes.short_description="Lotes"
    iralotes.allow_tags = True



    def __unicode__(self):
        return "%s | %s " % (self.cabprocesos,self.cuadcampo)

    class Meta:
        verbose_name_plural = _("Ordenes de Produccion")
        verbose_name        = _("Orden de Produccion")


class CalculaLote(models.Model):
    #Calcula el numero de lote
    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None):
        super(CalculaLote, self).save(force_insert, force_update)
        self.lote = self.oproduccion.serlote.serie+string.zfill(str(self.oproduccion.id),7)+string.zfill(str(self.pk),7)
        super(CalculaLote, self).save(force_insert, force_update)

class Lotes(CalculaLote):
    oproduccion   = models.ForeignKey(OrdenProduccion,verbose_name=_('Orden Produccion'))
    analiticas    = models.ForeignKey(CabAnaliticas,verbose_name=_('Analiticas'), blank=True, null=True)
    procesos      = models.ForeignKey(DetProcesos,verbose_name=_('Linea Proceso'))
    lote          = models.CharField(max_length=50,verbose_name=_('Lote'))
    fecha         = models.DateField(verbose_name=_('Fecha'))
    templote      = models.CharField(max_length=10,verbose_name=_('Temp.Lote'))
    carorganolep  = models.CharField(max_length=200,verbose_name=_('Organolepticas'))
    observaciones = models.TextField(verbose_name=_('Observaciones'),blank=True,null=True)



    def __unicode__(self):
        return "%s | %s " % (self.oproduccion,self.procesos)

#    def save(self, *args, **kwargs):
#        if self.id == None:
#            self.lote = Counter.next(userid=self.user,key=SerieLotes.objects.get(serie=self.serielote).id )


    class Meta:
        verbose_name_plural = _("Lotes")
        verbose_name        = _("Lote")



class DetLotes(models.Model):
    lotes       = models.ForeignKey(Lotes)
    feccad      = models.DateField(verbose_name=_('Fecha Caducidad'))
    producto    = models.ForeignKey(Vista_Productos,verbose_name=_('Producto'))
    bultos      = models.IntegerField(verbose_name=_("Bultos"), blank=True, null=True)
    kilos       = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True, verbose_name=_("Kilos"))

    class Meta:
        verbose_name_plural = _("Detalles Lotes")
        verbose_name        = _("Detalle Lote")



