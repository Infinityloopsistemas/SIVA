# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
# Create your models here.
import sys
from private_files import PrivateFileField, pre_download
from maestros_generales.models import TiposTerceros, Municipios, Paises, Provincias, CodigosPostales, Empresas, Marcas, TiposCatProfesional
from siva import settings
from siva.utils import RenameFilesModel, OPCIONES_DIAS, is_owner, obtenerImagen
from imagen.models import Imagen

SI_NO=(('S','Si'),('N','No'),)

class ExcepcionesCalendario(models.Model):
    denominacion = models.CharField(max_length=255,verbose_name=_("Razón de la excepción"))
    fecha_inicio  = models.DateField(_("Fecha Inicio"))
    fecha_final   = models.DateField(_("Fecha Final"))
    empresa       = models.ForeignKey(Empresas,null=True, blank=True,verbose_name=_('Empresa'),on_delete=models.PROTECT)
    class Meta:
        verbose_name        = "Excepción calendario"
        verbose_name_plural = "Excepciones calendario"

    def __unicode__(self):
        return "%s" % (self.denominacion)
class BaseMaestros(models.Model):
    fechaalta     = models.DateField(verbose_name=_("Fecha Alta"),blank=True)
    fechabaja     = models.DateField(verbose_name=_("Fecha Baja"), blank=True,null=True)
    empresa       = models.ForeignKey(Empresas,null=True, blank=True,verbose_name=_('Empresa'),on_delete=models.PROTECT)
    user          = models.ForeignKey(User,blank=True,null=True,on_delete=models.PROTECT)


#     def save(self, *args, **kwargs):
#         self.fechaalta=datetime.date.today()
#         super(BaseMaestros, self).save(*args, **kwargs)
    def save(self, user=None, *args, **kwargs):
        self.fechaalta=datetime.date.today()
        if user is not None:
            self.user= User.objects.get(username=user)
            if  self.user.is_staff==True:
                self.empresa = Empresas.objects.get(usuario=self.user)
                
            else:
                raise PermissionDenied
        super(BaseMaestros, self).save(*args, **kwargs)

    class Meta:
        abstract = True

    def urlImpresion(self):
        nombmodelo = self.__class__.__name__.lower()
        return '/reportes/lista/%s/0/%s/' % (nombmodelo,self.pk)

    def clone(self, empresa, user):
        old = self.__class__.__name__
        new_kwargs = dict([(fld.name, getattr(old, fld.name)) for fld in old._meta.fields if fld.name != 'id']);
        print new_kwargs
         #return self.__class__.objects.create(**new_kwargs)


    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "denominacion__icontains",)

class Terceros(BaseMaestros):
    tipotercero   = models.ForeignKey(TiposTerceros, verbose_name = _("Tipo Tercero"),related_name='rel_ter_tipo',on_delete=models.PROTECT)
    denominacion  = models.CharField(max_length=100, help_text=_("Razon social del Tercero"), verbose_name=_("Razon Social"))
    #cif          = ESIdentityCardNumberField( help_text ="Introducir cif de la empresa")
    cif           = models.CharField(max_length=20, verbose_name=_("CIF/NIF"))
    direccion1    = models.CharField(max_length=50,  help_text=_("Direccion"), verbose_name=_("Direccion"))
    direccion2    = models.CharField(max_length=50, verbose_name=_("Localidad"),blank=True,null=True)
    #telefono     = ESPhoneNumberField(help_text="Telefono para formato espanol")
    telefono      = models.CharField(max_length= 20, verbose_name=_("Telefono"), blank=True,null=True)
    email         = models.EmailField(max_length=50, verbose_name=_("Email"),blank=True,null=True)
    paginaweb     = models.CharField(max_length=100, verbose_name=_("www"),blank=True,null=True)
    municipio     = models.ForeignKey(Municipios,verbose_name=_("Municipio"),help_text=_("Se autocompleta"),on_delete=models.PROTECT)
    pais          = models.ForeignKey(Paises,verbose_name=_("Pais"), related_name='rel_ter_pais',help_text=_("Se autocompleta"),on_delete=models.PROTECT)
    provincia     = models.ForeignKey(Provincias,verbose_name=_("Provincia"),related_name='rel_ter_prov',help_text=_("Se autocompleta"),on_delete=models.PROTECT)
    codpostal     = models.ForeignKey(CodigosPostales,verbose_name=_("Codigo Postal"),related_name='rel_ter_cod',on_delete=models.PROTECT)
    percontacto   = models.CharField(verbose_name=_("Persona de Contacto"), max_length=50)
    registrosani  = models.CharField(verbose_name=_("Registro Sanitario") ,max_length=20)


    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","denominacion__icontains")


    def django_user(self):
        return self.user


    def delete(self, *args, **kwargs):
        """Never delete, just mark as deleted"""
        try:
            self.deleted = True
            self.save()
        except:
            print >> sys.stderr, "ERROR! No puede ser borrado"

    def __unicode__(self):
        return unicode(self.denominacion)

    class Meta:
        ordering = ('denominacion',)
        verbose_name = _("Tercero")
        verbose_name_plural = _("Terceros")

    def get_absolute_url(self):
        return reverse('terceros_actualizar',args=[self.pk])

    def urlDocumentos(self):
        return '/maestros/documentos/lista/terceros_id/%s/' % (self.pk)




class Personal(BaseMaestros):
    dni             = models.CharField( max_length=20,verbose_name="Dni")
    apellidos       = models.CharField(max_length=50, verbose_name="Apellidos")
    nombres         = models.CharField(max_length=50, verbose_name="Nombres")
    estadocivil     = models.CharField(choices=(('Casado','Casado'),('Soltero','Soltero')),max_length=50, blank=True, verbose_name="Estado Civil")
    fechanacimiento = models.DateField(null=True, blank=True,verbose_name="F.Nacimiento")
    sexo            = models.CharField(choices=(('M','Masculino'),('F','Femenino')),max_length=1, blank=True, verbose_name="Sexo")
    nss             = models.BigIntegerField(verbose_name="N. S.S")
    imagen          = models.ImageField(max_length=100, blank=True, verbose_name=_("Imagen"), upload_to="/subidas")
    cargo           = models.CharField(max_length=100,verbose_name="Cargo que ocupa")
    observaciones   = models.TextField(max_length=4000, blank=True,verbose_name=_("Observaciones"))
    catprofesional  = models.ForeignKey(TiposCatProfesional,verbose_name="Cat.Profesional",on_delete=models.PROTECT)
    email           = models.EmailField(verbose_name="Email",null=True,blank=True )
    emailnotifica   = models.EmailField(verbose_name="Email a efectos notificaciones del sistema",null=True,blank=True )
    telefonosms     = models.CharField(max_length=20,verbose_name="Telefono SMS", blank=True, null=True)
    imagen = GenericRelation(Imagen)

    class Meta:
        verbose_name        = _("Datos Personales")
        verbose_name_plural = _("Datos Personales")
        ordering =['apellidos','nombres']

    def __unicode__(self):
        return self.denominacion()

    def denominacion(self):
        return ('%s - %s %s') % (self.dni,self.apellidos,self.nombres)

    @models.permalink
    def get_absolute_url(self):
        return ('personal_actualizar',(), {'pk' :str(self.id), })
    def urlDocumentos(self):
            return '/maestros/documentos/lista/personal_id/%s/' % (self.pk)
    def get_model(self):
        return self.__class__.__name__.lower()
    def get_imagen(self):
        ct = ContentType.objects.filter(model=self.get_model())
        img = get_object_or_404(Imagen,content_type=ct.first(),object_id=self.pk)
        img = obtenerImagen(img)
        imgStr = "data:{ct};base64,{fi}".format(ct=img.content_type_file, fi=img.file)
        return imgStr
    def hay_imagenes(self):
        ct = ContentType.objects.filter(model=self.get_model())
        print Imagen.objects.filter(content_type=ct.first(),object_id=self.pk)
        if Imagen.objects.filter(content_type=ct.first(),object_id=self.pk).count() > 0:
            return True
        else:
            return False



class Firmas(BaseMaestros):
    personal   =  models.ForeignKey(Personal,verbose_name=_("Personal"),on_delete=models.PROTECT)
    fecha      =  models.DateField(verbose_name=_("Fecha"))

    def denominacion(self):
        return "%s - %s  -- %s " % (self.personal.apellidos,self.personal.nombres,self.fecha)

    class Meta:
        verbose_name_plural = _('Firmas')
        verbose_name        = _('Firmas')
        unique_together=['personal','fecha'] #nuevo

    def get_absolute_url(self):
        return reverse('firmas_actualizar',args=[self.pk])

#     class Meta:
#         unique_together=['personal','fecha']


class Etapas(BaseMaestros):
    denominacion = models.CharField(max_length=100, verbose_name=_("Denominación"))
    ayuda        = models.TextField(blank=True, null=True, verbose_name="Explicacion")
    def __unicode__(self):
        return self.denominacion

    class Meta:
        verbose_name_plural = _('Etapas')
        verbose_name        = _('Etapa')

    def get_absolute_url(self):
        return reverse('etapas_actualizar',args=[self.pk])

class Peligros(BaseMaestros):
    denominacion = models.CharField(max_length=100, verbose_name=_("Denominación"))
    ayuda        = models.TextField(blank=True, null=True, verbose_name="Explicacion")

    def __unicode__(self):
        return self.denominacion

    class Meta:
        verbose_name_plural = _('Actividades')
        verbose_name        = _('Actividad')

    def get_absolute_url(self):
        return reverse('peligros_actualizar',args=[self.pk])

class Actividades(BaseMaestros):
    denominacion = models.CharField(max_length=100, verbose_name=_("Denominación"))
    tipo         = models.CharField(max_length=1,choices=(('V','Toma de valores'),('C','Check')), help_text=_("Selección según el tipo de registro"))
    colorback    = models.CharField(max_length=20, verbose_name=_("Paleta de color de fondo"),blank=True,null=True)
    colortxt     = models.CharField(max_length=20, verbose_name=_("Paleta de color texto"),blank=True,null=True)
    agenda       = models.BooleanField(verbose_name=_("Incluir en Agenda"))

    def __unicode__(self):
        return self.denominacion

    class Meta:
        verbose_name_plural = _('Actividades')
        verbose_name        = _('Actividad')

    def get_absolute_url(self):
        return reverse('actividades_actualizar',args=[self.pk])




class Unidades(BaseMaestros):
    denominacion = models.CharField(max_length=100, verbose_name=_("Unidades"))

    def __unicode__(self):
        return self.denominacion

    class Meta:
        verbose_name_plural = _('Unidades')
        verbose_name        = _('Unidad')

    def get_absolute_url(self):
        return reverse('unidades_actualizar',args=[self.pk])



class ParametrosAnalisis(BaseMaestros):
    tipo          = models.CharField(max_length=1 , choices=(('I',_('Indicador')),('S',_('Sustancia'))), verbose_name=_("Tipo"), help_text=_("Tipo de valor"))
    denominacion  = models.CharField(max_length=100, verbose_name=_("Denominacion"))
    unidades      = models.ForeignKey(Unidades,verbose_name=_("Unidades"),on_delete=models.PROTECT)



    def __unicode__(self):
        return "%s %s" % (self.denominacion,self.unidades)

    class Meta:
        verbose_name_plural = _('Parametros Analisis')
        verbose_name        = _('Parametro Analisis')

    def get_absolute_url(self):
        return reverse('parametrosanalisis_actualizar',args=[self.pk])

class CatalogoEquipos(BaseMaestros):
    denominacion         = models.CharField(max_length=255, blank=True,verbose_name=_("Descripcion"))
    noserie              = models.CharField(max_length=255, blank=True,verbose_name=_("No. Serie"))
    caracteristicas      = models.TextField(max_length=255, blank=True,verbose_name=_("Caracteristicas"))
    marcas               = models.ForeignKey(Marcas, null=True, blank=True,verbose_name=_("Marcas"),on_delete=models.PROTECT)
    fadquirir            = models.DateField(null=True, blank=True,verbose_name=_("F.Adquisicion"))
    finstala             = models.DateField(null=True, blank=True,verbose_name=_("F.Instalacion"))
    modelo               = models.CharField(max_length=255, blank=True,verbose_name=_("Modelo"))
    tipo                 = models.CharField(max_length=1,verbose_name="Tipo",choices=(("E",_("Equipo") ),("I",_("Instalación")),("V",_("Vehículo") ) ))
    class Meta:
        verbose_name_plural = _('Catalogo Equipos')
        verbose_name        = _('Catalogo Equipo')
        ordering            = ['denominacion']

    def __unicode__(self):
        return self.denominacion

    def get_absolute_url(self):
        return reverse('catalogoequipos_actualizar',args=[self.pk])

    def urlDocumentos(self):
        return '/maestros/documentos/lista/catequipos_id/%s/' % (self.pk)

class TiposTemperaturas(BaseMaestros):
    denominacion = models.CharField(max_length=100, verbose_name=_("Denominación"),help_text=_("Denominación Temperatura") )
    tmax         = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_("Temp. Maxima"))
    tmin         = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_("Temp. Minima"))

    def __unicode__(self):
        return self.denominacion

    class Meta:
        verbose_name_plural = _('Tipos de Temperaturas')
        verbose_name        = _('Tipo de Temperatura')

    def get_absolute_url(self):
        return reverse('tipostemperaturas_actualizar',args=[self.pk])

class  Zonas(BaseMaestros):
    denominacion  = models.CharField(max_length=100,verbose_name=_("Denominación"))
    superficie    = models.IntegerField(max_length=10, verbose_name=_("Superfice"),help_text=_("Superfice en Mts2"))
    tipotemp      = models.ForeignKey(TiposTemperaturas,verbose_name=_("Tipos Temp."), help_text=_("Tipos de temperatura"),on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = _('Zonas')
        verbose_name        = _('Zona')

    def __unicode__(self):
        return self.denominacion

    def get_absolute_url(self):
        return reverse('zonas_actualizar',args=[self.pk])

    def urlDocumentos(self):
        return '/maestros/documentos/lista/zonas_id/%s/' % (self.pk)

class TiposMedidasActuacion(BaseMaestros):
    denominacion = models.CharField(max_length=100,verbose_name=_("Denominación"))
    ayuda        = models.TextField(verbose_name=_("Ayuda"))
    tipo         = models.CharField(max_length=1,choices=(("P","Prenventiva"),("C","Correctora")))

    class Meta:
        verbose_name_plural = _('Tipos Medidas de Actuacion')
        verbose_name        = _('Tipo de Medida Actuacion')

    def __unicode__(self):
        return self.denominacion

    def get_absolute_url(self):
        return reverse('tiposmedidasactuacion_actualizar',args=[self.pk])

class TiposMedidasVigilancia(BaseMaestros):
    denominacion = models.CharField(max_length=100,verbose_name=_("Denominación"))
    ayuda        = models.TextField(verbose_name=_("Ayuda"))

    class Meta:
        verbose_name_plural = _('Tipos de Medidas de Vigilancia')
        verbose_name        = _('Tipo Medida de Vigilancia')

    def __unicode__(self):
        return self.denominacion

    def get_absolute_url(self):
        return reverse('tiposmedidasvigilancia_actualizar',args=[self.pk])

class TiposLimitesCriticos(BaseMaestros):
    denominacion = models.CharField(max_length=100,verbose_name=_("Denominación"))
    ayuda        = models.TextField(null=True, blank=True, verbose_name=_("Ayuda"))
    valormax     = models.DecimalField(max_digits=10,decimal_places=2 ,null=True, blank=True, verbose_name=_("Valor Maximo"))
    valormin     = models.DecimalField( max_digits=10,decimal_places=2,null=True, blank=True, verbose_name=_("Valor Minimo"))
    unidades     = models.ForeignKey(Unidades, verbose_name="Unidades",null=True, blank=True,on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = _('Tipos de Limites Criticos')
        verbose_name        = _('Tipo de Limite Critico')

    def __unicode__(self):
        return self.denominacion

    def get_absolute_url(self):
        return reverse('tiposlimitescriticos_actualizar',args=[self.pk])

class Consumibles(BaseMaestros):
    denominacion = models.CharField(max_length=100,verbose_name=_("Denominación"))
    tipo         = models.CharField(max_length=100,verbose_name=_("Tipo de Uso"), help_text=_("Limpieza, Seguridad, Elemento de Limpieza"))

    class Meta:
        verbose_name_plural = _('Consumibles')
        verbose_name        = _('Consumible')

    def __unicode__(self):
        return self.denominacion

    def get_absolute_url(self):
        return reverse('consumibles_actualizar',args=[self.pk])

    def urlDocumentos(self):
        return '/maestros/documentos/lista/consumibles_id/%s/' % (self.pk)

    def save(self, user, *args, **kwargs):
        self.fechaalta=datetime.date.today()
        if user is not None:
            self.user= User.objects.get(username=user)
            if  self.user.is_staff==True:
                self.empresa = Empresas.objects.get(usuario=self.user)
                super(Consumibles, self).save(*args, **kwargs)
            else:
                raise PermissionDenied



class ConsumiEspecificaciones(models.Model):
    consumibles   = models.ForeignKey(Consumibles,on_delete=models.PROTECT)
    descripcion   = models.CharField(max_length=100,verbose_name=_("Descripcion"))

    def __unicode__(self):
        return self.denominacion



class TiposFrecuencias(BaseMaestros):
    denominacion   = models.CharField(max_length=100,verbose_name=_("Denominación"))
    nounidades     = models.IntegerField( max_length=6, verbose_name=_("No. unidades"), help_text=_("No. de Unidades en Horas"))
    diaslaborables = models.CharField(verbose_name=_("Excluir"),max_length=1,choices=OPCIONES_DIAS)

    class Meta:
        verbose_name_plural = _('Tipos de Frecuencia')
        verbose_name        = _('Tipo de Frecuencia')

    def __unicode__(self):
        return self.denominacion


    def get_absolute_url(self):
        return reverse('tiposfrecuencias_actualizar',args=[self.pk])

class TiposLegislacion(BaseMaestros):
    denominacion   = models.CharField(max_length=100,verbose_name=_("Denominación"))
    contenido      = models.TextField(verbose_name=_("Contenido"))

    def get_absolute_url(self):
        return reverse('tiposlegislacion_actualizar',args=[self.pk])


class TiposCursos(BaseMaestros):
    denominacion   = models.CharField(max_length=100,verbose_name=_("Denominación"))
    contenido      = models.TextField(verbose_name=_("Contenido"))
    legislacion    = models.ForeignKey(TiposLegislacion, verbose_name=_("Legislación"),null=True,blank=True)

    def get_absolute_url(self):
        return reverse('tiposcursos_actualizar',args=[self.pk])


class TiposTurnos(BaseMaestros):
    denominacion= models.CharField(max_length=200,verbose_name=_('Tipo de Turnos'))

    def save(self, user, *args, **kwargs):
        self.fechaalta=datetime.date.today()
        if user is not None:
            self.user= User.objects.get(username=user)
            if  self.user.is_staff==True:
                self.empresa = Empresas.objects.get(usuario=self.user)
                super(TiposTurnos, self).save(*args, **kwargs)
            else:
                raise PermissionDenied

    def __unicode__(self):
        return self.denominacion

    def get_absolute_url(self):
        return reverse('tiposturnos_actualizar',args=[self.pk])

class HorarioTurnos(models.Model):
    tpturnos = models.ForeignKey(TiposTurnos, related_name="horarioturnos")
    ihora    = models.IntegerField(verbose_name=_("Hora inicio"), help_text=_("En formato 24 horas"))
    fhora    = models.IntegerField(verbose_name=_("Hora fin"), help_text=_("En formato 24 horas"))

    def __unicode__(self):
        return "%s - %s" % (self.ihora,self.fhora)



class TiposProcesos(BaseMaestros):
    denominacion= models.CharField(max_length=200,verbose_name=_('Tipo de Proceso'))
    pesado      = models.CharField(max_length=1, choices=SI_NO )
    etiquetado  = models.CharField(max_length=1, choices=SI_NO)
    nivel       = models.CharField(max_length=1,verbose_name=_('Nivel'),choices=(('E',_('Entrada')),('I',_('Intermedio')),('S',_('Salida'),)))

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact","descripcion__icontains",)

    def __unicode__(self):
        return unicode(self.denominacion)

    class Meta:
        verbose_name_plural = _('Tipos de Procesos')
        verbose_name        = _('Tipo de Proceso')

    def get_absolute_url(self):
        return reverse('tiposprocesos_actualizar',args=[self.pk])



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
    fecha         = models.DateField(verbose_name="Fecha")
    denominacion  = models.CharField(max_length="200", verbose_name=_("Denominación"))
    contenido     = models.TextField(null=True,blank=True)
    archivos      = PrivateFileField( "file", upload_to='maestros',blank=True,null=True,help_text=_("Tamaño maximo 2.5 MB"),attachment=False,condition=is_owner)
    terceros      = models.ForeignKey(Terceros, null=True,blank=True,on_delete=models.PROTECT)
    personal      = models.ForeignKey(Personal, null=True,blank=True,on_delete=models.PROTECT)
    zonas         = models.ForeignKey(Zonas, null=True,blank=True,on_delete=models.PROTECT)
    catequipos    = models.ForeignKey(CatalogoEquipos, null=True,blank=True,on_delete=models.PROTECT)
    consumibles   = models.ForeignKey(Consumibles, null=True,blank=True,on_delete=models.PROTECT)
    fechaproceso  = models.DateField(verbose_name="Fecha de Proceso conversion", blank=True, null=True)
    nodescargas   = models.PositiveIntegerField("total descargas", default = 0)

    RENAME_FILES        = {
        'archivos': {'dest': 'maestros', 'keep_ext': True},
        }

    def get_absolute_url(self):
        return reverse('mdocumentos_actualizar',args=[self.pk])

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

