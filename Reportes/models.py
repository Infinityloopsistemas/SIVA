import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from maestros_generales.models import Empresas, TipoPlanControl
from siva import settings
from siva.settings import *

class BaseReportes(models.Model):
    fechaalta     = models.DateField(verbose_name=_("Fecha Alta"),blank=True)
    fechabaja     = models.DateField(verbose_name=_("Fecha Baja"), blank=True,null=True)
    empresa       = models.ForeignKey(Empresas,null=True, blank=True,verbose_name=_('Empresa'), related_name="infor_empresas")
    user          = models.ForeignKey(User,blank=True,null=True)


    def save(self, *args, **kwargs):
        self.fechaalta=datetime.date.today()
        super(BaseReportes, self).save(*args, **kwargs)

    class Meta:
        abstract = True



class Informes(BaseReportes):
    content_type  = models.ForeignKey(ContentType)
    tpplancontrol = models.ForeignKey(TipoPlanControl,null=True,blank=True,verbose_name="Tipo Plan", related_name="tpplan_tipo")
    descripcion   = models.CharField(max_length=200, verbose_name="Descripcion")
    nombrereport  = models.CharField(max_length=50, verbose_name="Nombre")
    #url           = models.URLField(max_length=500,verbose_name="Camino", default=settings.SERVER_URL_REPORTS+"={REPORTE}&j_acegi_security_check?&j_username=siva&j_password=56789_siva_1234&decorate=no&output=pdf")
    url           = models.URLField(max_length=500,verbose_name="Camino",default=settings.SERVER_URL_REPORTS)
    fecha         = models.DateField()
    nombprocede   = models.CharField(max_length=1000,verbose_name="Procedimiento", blank=True, null=True)

    def denominacion(self):
        return self.descripcion

    def urlInformes(self):
        return " /reportes/impresion/%s" % self.id

    def Impresion(self):
            return '<a class="dialogo" href="%s/%s" style="color:#FF0000">Imprimir</a>' % (BASE_URL_REPORTS,self.id)

    Impresion.short_description = "Imprimir"
    Impresion.allow_tags = True

    class Meta:
        verbose_name_plural= "Informes"
        verbose_name = "Informe"



class DetalleInformes(models.Model):
    informe       = models.ForeignKey(Informes)
    nombparametro = models.CharField(max_length=20,verbose_name="Parametro")
    tipoparametro = models.CharField(max_length=1,choices=[('D','Fecha'),('C','ComboBox'),('T','Texto'),('N','Numerico'),('O','CheckBox')])
    mostrar       = models.BooleanField()
    nombetiqueta  = models.CharField(max_length=50,verbose_name="Etiqueta")
    modelo        = models.ForeignKey(ContentType,verbose_name="modelo",null=True,blank=True)
    query_modelo  = models.CharField(max_length=500,verbose_name="query",null=True,blank=True,help_text=_("Paramerizar el modelo"))


