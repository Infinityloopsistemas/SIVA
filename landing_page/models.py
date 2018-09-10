from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from geoposition.fields import GeopositionField

from maestros_generales.models import Empresas
from imagen.models import Imagen

# Create your models here.

class CabLandingPage(models.Model):
    empresa       = models.ForeignKey(Empresas,null=True, blank=True,verbose_name=('Empresa'),on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=1000)
    url = models.URLField(blank=True,default='#')
    fechaalta     = models.DateField(verbose_name=("Fecha Alta"))
    fechabaja     = models.DateField(verbose_name=("Fecha Baja"), blank=True,null=True)
    geolocalizacion = GeopositionField()
    nota = models.CharField(max_length=1000)
    tags = models.CharField(max_length=1000)
    imagen = GenericRelation(Imagen)
    
    def __unicode__(self):
        return ('Landing Page %s') % (self.empresa.descripcion)
    
    def get_model(self):
        return self.__class__.__name__.lower()
    
