# -*- coding: utf-8 -*-
# __author__ = 'julian'
from base64 import encode
import calendar
from django.core.mail import EmailMessage
#from django.db.models import get_model
from reportes.models import Informes
from context_processors import empresa
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import ModelFormMixin
from maestros_generales.models import Empresas
from django.conf.urls import url, include
from django.template.loader import render_to_string
import datetime
import decimal
import base64
from django.contrib import admin
from django.db import connection
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext, Context
from django.forms.util import ErrorList
#from django.utils import simplejson
import json as simplejson
from crispy_forms.utils import render_field
import maestros
import maestros_generales
import appcc
import productos
import trazabilidad
import settings
from django.db import models
from django.utils.encoding import force_unicode
import string, os
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import length
from gestion_usuarios.utils import is_allowed_edit, is_allowed_see


HORA = datetime.datetime.now().hour

genericaview      =  "Generica"
lista_template    =  {'template_name' : "base/list.html",}
detalle_template  =  {'template_name' : "base/detalle.html",}
form_template     =  {'template_name' : "base/form.html",}
eliminar_template =  {'template_name' : "base/eliminar.html",}

s12="span12"   # 1 por fila
s6 ="span6"    # 2 por fila
s4 ="span4"    # 3 por fila
s3 ="span3"    # 4 por fila
s10 ="span10"  # 4 por fila
fecha     = "form/field_date.html"
editor    = "form/field_textarea.html"
campo     = "form/field.html"

mini    ="input-mini"
small   ="input-small"
medium  ="input-medium"
xlarge  ="input-xlarge"
xxlarge ="input-xxlarge"

OPCIONES_DIAS = (('T',_('Ningun día')),('A',_('Todos los dias')),('L',_('Lunes a Viernes')),('F',_('Fin de Semana')),('5',_('Sabado')),('6',_('Domingo')),('0',_('Lunes')),('1',_('Martes')),('2',_('Miercoles')),('3',_('Jueves')),('4',_('Viernes')))
SI_NO = [(_('S'),'Si'),(_('N'),'No'),]

#Valida si muestra los documentos por usuario y empresa
def is_owner(request, instance):
    if not request.user.is_anonymous():
        empresa_id  = Empresas.objects.get(usuario=request.user).id
        print empresa_id
        for field in instance._meta.fields:
            if field.get_internal_type() in ("ForeignKey"):
                valor = getattr(instance,field.get_attname())
                if valor is not None:
                    model = field.rel.to
                    emp_id = get_object_or_404(model,pk=valor).empresa_id
                    print emp_id
        return ( not request.user.is_anonymous() ) and request.user.is_authenticated and (emp_id == empresa_id)
    else:
        return False

#Renombra archivos con Id del modelo
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




class JSONEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if (isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date)):
            return obj.strftime('%d-%m-%Y')
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return simplejson.JSONEncoder.default(self, obj)


class EsqueletoModelAdmin(admin.ModelAdmin):

    change_list_template = "admin/change_list_filter_sidebar.html"

    class Media:
        css = {
            "all": (settings.STATIC_URL+"css/jquery.autocomplete.css",settings.STATIC_URL+"css/iconic.css",settings.STATIC_URL+"css/jquery.ui.dialog.css",settings.STATIC_URL+"css/apprise.css")
        }
        #js  = (settings.STATIC_URL+"js/jquery-1.5.1.min.js",settings.STATIC_URL+"js/dajaxice.core.js",settings.STATIC_URL+"js/jquery-ui-1.8.13.custom.min.js",settings.STATIC_URL+"js/jquery.autocomplete.min.js",settings.STATIC_URL+"js/jquery.dajax.core.js",settings.STATIC_URL+"js/jquery.number_format.js",settings.STATIC_URL+"js/adminlib.js",settings.STATIC_URL+"js/apprise-1.5.full.js")
        js  = ("https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js",'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
               '/static/grappelli/tinymce_setup/tinymce_setup.js',)

        #    formfield_overrides = {
    #        models.TextField: {'widget': RichTextEditorWidget},
    #    }
    #    valid_lookups = ()
    list_per_page = 15
#    def lookup_allowed(self, lookup,args, **kwargs):
#        if lookup.startswith(self.valid_lookups):
#            return True
#        return super(EsqueletoModelAdmin, self).lookup_allowed(lookup,*args, **kwargs)


class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return u''
        return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="error">%s</div>' % e for e in self])




def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)


def make_url_list(input, prefix=''):
    l = []

    for name in input:
        #l.append( url(regex= '^%s/lista/$' % name,
        l.append( url(regex= '^%s/$' % name,
            view = user_passes_test(is_allowed_see)(eval('%s.views.%sListaView.as_view()' % (prefix,name.capitalize()))),
            name = '%s_list' %name) )

        l.append( url(regex= '^%s/detalle/(?P<pk>\d+)/$' % name,
            view = eval('%s.views.%sDetalleView.as_view()' % (prefix,name.capitalize())),
            name = '%s_detalle' %name) )

#         l.append( url(regex= '^%s/crear/$' % name,
#             view = eval('%s.views.%sCrearView.as_view()' %(prefix, name.capitalize())),
#             name = '%s_crear' %name) )
        l.append( url(regex= '^%s/crear/$' % name,
            view = user_passes_test(is_allowed_edit)(eval('%s.views.%sCrearView.as_view()' %(prefix, name.capitalize()))),
            name = '%s_crear' %name) )

        l.append( url(regex= '^%s/eliminar/(?P<pk>\d+)/$' % name,
            view = user_passes_test(is_allowed_edit)(eval('%s.views.%sEliminarView.as_view()' % (prefix,name.capitalize()))),
            name = '%s_eliminar' %name) )

        l.append( url(regex= '^%s/actualizar/(?P<pk>\d+)/$' % name,
            view = eval('%s.views.%sActualizarView.as_view()' % (prefix,name.capitalize())),
            name = '%s_actualizar' %name) )


    return l


class BaseTable(object):

    template = "form/layout/table_elmens.html"

    def __init__(self, *fields, **kwargs):
        self.fields = fields

        if hasattr(self, 'css_class') and 'css_class' in kwargs:
            self.css_class += ' %s' % kwargs.get('css_class')
        if not hasattr(self, 'css_class'):
            self.css_class = kwargs.get('css_class', None)

        self.css_id = kwargs.get('css_id', '')
        self.template = kwargs.get('template', self.template)

    def render(self, form, form_style, context):
        fields = ''
        for field in self.fields:
            fields += render_field(field, form, form_style, context)
        return render_to_string(self.template, Context({'tag': self.element,
                                                        'elem': self,
                                                        'fields': fields}))



class TD(BaseTable):
    element = 'td'



class TR(BaseTable):
    element = 'tr'



class ReordenarCuadrosGestion:

    def __init__(self,usuario):
        from appcc.models import CuadrosGestion
        self.usuario=usuario
        self.cuadros=CuadrosGestion


    def recursivaOrden(self,hijo,draiz):
        child = hijo.get_children()
        dummy=0
        subnodo =0
        fijo = draiz['txt']
        for elemento in child:
            subnodo += 1
            draiz['nodo']=subnodo
            draiz['txt'] = fijo +'.'+str(subnodo)
            ord= self.cuadros.objects.get(pk=elemento.id)
            ord.orden = draiz['txt']
            ord.save(user=self.usuario)
            if elemento.get_children().count() !=0:
                dummy = self.recursivaOrden(elemento,draiz)
        return dummy

    def reordenar(self):
        root = self.cuadros.objects.root_nodes().filter(empresa__in=Empresas.objects.filter(usuario__username=self.usuario)).order_by('id')
        draiz={ 'nodo' :0 , 'txt': "" }
        nraiz=0
        for hijos in root:
            nraiz+=1
            draiz={ 'nodo' :nraiz , 'txt': str(nraiz) }
            ord  = self.cuadros.objects.get(pk=hijos.id)
            ord.orden = draiz['txt']
            ord.save(user=self.usuario)
            final= self.recursivaOrden(hijos,draiz)


def buscaHorario(detreg):
    if detreg.tpturnos_id is None:
        return None
    else:
        horarios = maestros.models.HorarioTurnos.objects.filter(tpturnos__id=detreg.tpturnos_id)
        for horaturno in horarios:
                if horaturno.ihora<=HORA and horaturno.fhora>=HORA:
                    return horaturno.id

#--------------------------------------------------
#Construye json para la impresion de registros
#--------------------------------------------------
class JsonImpRegPanel:

    def __init__(self,empresaid):
        from appcc.models import ManualAutoControl
        self.empresaid=empresaid
        self.manual=ManualAutoControl

    def arbolDiccionario(self,ele,expand,check,tipo):
        diccionario= { "id" : str(ele[0]) , "text": ele[1].encode('utf-8') , "leaf": False ,"value" :ele[2] , "expanded":expand, "checked": check, "cls":tipo }
        return diccionario

    def generar(self):
        from appcc.models import CabRegistros, DetallesRegistros
        root = self.manual.objects.filter(empresa_id=self.empresaid)
        draiz={ 'nodo' :0 , 'txt': "" }
        nraiz=0
        jsonarbol      =[]
        nivel1=[]
        for hijos in root:
            nraiz+=1
            cabreg = CabRegistros.objects.filter(manautctrl=hijos)
            if cabreg.count() !=0:
                nivel2=[]
                for ecab in cabreg:
                 detreg = DetallesRegistros.objects.filter(cabreg=ecab, actividades__agenda=True )
                 if detreg.count()!=0:
                     nivel3=[]
                     for edet in detreg:
                         ele    =[int(edet.id),"%s - %s" % (edet.actividades.denominacion,edet.zonas),edet.urlImpresion()]
                         arbol= self.arbolDiccionario(ele,False,False,'null')
                         arbol['leaf'] = True
                         nivel3.append(arbol)
                         ele=[]

                     ele = [int(ecab.id),ecab.denominacion,ecab.urlImpresion()]
                     arbol = self.arbolDiccionario(ele,False,False,'folder')
                     arbol['leaf'] = False
                     arbol['children'] = nivel3
                     nivel2.append(arbol)
                     ele=[]

                if len(nivel2)!=0:
                    ele   = [int(hijos.id),hijos.tpplancontrol.denominacion,hijos.urlImpresion()]
                    arbol = self.arbolDiccionario(ele,False,False,'folder')
                    arbol['children']=nivel2
                    nivel1.append(arbol)
                    ele=[]
        return simplejson.dumps(nivel1)




class JsonCuadrosGestion:

    def __init__(self,empresaid):
        from appcc.models import CuadrosGestion
        self.empresaid=empresaid
        self.cuadros=CuadrosGestion


    def arbolDiccionario(self,ele,expand,check,tipo):
        titulo = "%s-%s-%s-%s" % (ele.orden,ele.etapa,ele.peligro,ele.tpmedactp)
        diccionario= { "id" : str(ele.id) , "text": unicode(titulo) , "leaf": ele.is_leaf_node(),"value" :"/appcc/cuadrosgestion/actualizar/%s" % ele.id , "expanded":expand, "checked": check, "cls":tipo }
        return diccionario




    def recursivaOrden(self,hijo,draiz):
        child = hijo.get_children()
        dummy=0
        subnodo =0
        fijo = draiz['txt']
        jsonarbol=[]
        for elemento in child:
            elediccionario = self.arbolDiccionario(elemento,subnodo,False,None)
            subnodo += 1
            draiz['nodo']=subnodo
            draiz['txt'] = fijo +'.'+str(subnodo)
            ord= self.cuadros.objects.get(pk=elemento.id)
            ord.orden = draiz['txt']
            #Guardar aqui
            if elemento.get_children().count() !=0:
                elediccionario['leaf'] = True
                elediccionario['children']=self.recursivaOrden(elemento,draiz)
            jsonarbol.append(elediccionario)
        return jsonarbol

    def generar(self):
        root = self.cuadros.objects.root_nodes().filter(empresa_id=self.empresaid)
        draiz={ 'nodo' :0 , 'txt': "" }
        nraiz=0
        jsonarbol      =[]
        for hijos in root:
            nraiz+=1
            draiz          = { 'nodo' :nraiz , 'txt': str(nraiz) }
            elediccionario = self.arbolDiccionario(hijos,False,False,'folder')
            ord            = self.cuadros.objects.get(pk=hijos.id)
            ord.orden      = draiz['txt']
            if hijos.get_children().count() !=0:
                elediccionario['children']= self.recursivaOrden(hijos,draiz)
            jsonarbol.append(elediccionario)
        return jsonarbol



class BreadcrumbTemplateMixin(TemplateResponseMixin):

    def render_to_response(self, context, **response_kwargs):

#         allowed_ordered_breadcrumbs =['panel','lista','crear','actualizar']
#         breadcrumb_list = [
#             ( ('Principal'), '/panelprincipal'),
#         ]
#         print self.request.path_info
#         urlsecciones= self.request.path.split('/')
#         print urlsecciones
#         #breadcrumb_list.append( (("panel"),"/%s/%s" %(urlsecciones[1],"panel") ))
#         breadcrumb_list.append( ((urlsecciones[1]),"/%s/%s" %(urlsecciones[1],"panel") ))
#         if len(urlsecciones)>2:
#             breadcrumb_list.append( ( (urlsecciones[2]),"/%s/%s/%s" %(urlsecciones[1],urlsecciones[2],"lista")) )
#         if len(urlsecciones)> 3:
#             breadcrumb_list.append(( (urlsecciones[3]),self.request.path ))
        breadcrumb_list = generarBreadCrumb(self.request.path)

        self.request.breadcrumbs(breadcrumb_list)

        return self.response_class(
            request = self.request,
            template = self.get_template_names(),
            context = context,
            **response_kwargs
        )




class ReordenarDetProcesos:

    def __init__(self,usuario,id):
        from trazabilidad.models import DetProcesos
        self.usuario=usuario
        self.detprocesos=DetProcesos
        self.id = id


    def recursivaOrden(self,hijo,draiz):
        child = hijo.get_children()
        dummy=0
        subnodo =0
        fijo = draiz['txt']
        for elemento in child:
            subnodo += 1
            draiz['nodo']=subnodo
            draiz['txt'] = fijo +'.'+str(subnodo)
            ord= self.detprocesos.objects.get(pk=elemento.id)
            ord.orden = draiz['txt']
            ord.save()
            if elemento.get_children().count() !=0:
                dummy = self.recursivaOrden(elemento,draiz)
        return dummy

    def reordenar(self):
        root = self.detprocesos.objects.root_nodes().filter(cabprocesos_id=self.id,empresa__in=Empresas.objects.filter(usuario__username=self.usuario))
        draiz={ 'nodo' :0 , 'txt': "" }
        nraiz=0
        for hijos in root:
            nraiz+=1
            draiz={ 'nodo' :nraiz , 'txt': str(nraiz) }
            ord  = self.detprocesos.objects.get(pk=hijos.id)
            ord.orden = draiz['txt']
            ord.save()
            final= self.recursivaOrden(hijos,draiz)




def llenadoAutomatico(fechahasta,empid,userid):
    from appcc.models import Registros
    from maestros.models import Actividades
    sql =   """ select actividades,
                       zonas,
                       fechaultimo,
                       fechaalta,
                       diasinicio,
                       empresa_id,
                       user_id,
                       dias,
                       diaslaborables,
                       id,
                       colortxt,
                       colorback,
                       orden,
                       diaejecuta,
                       horas,
                       equipo,
                       tpturnos_id,
                       horarioturno_id
                 from v$detallesregistros_agenda where user_id=%s order by orden,actividades,equipo desc""" % userid

    cur  = connection.cursor()
    cur.execute(sql)
    verReg = cur.fetchall()
    fechaparar = datetime.datetime.strptime(fechahasta,"%d-%m-%Y").date()
    for  reg in verReg:
        obj = Actividades.objects.filter(denominacion=reg[0],empresa_id=empid)
        if obj[0].tipo==u"C":
            fecha=reg[2]
            while fecha<=fechaparar:
                fecha=fecha+datetime.timedelta(days=1)
                print "Fecha:%s DetReg:%s Actividad: %s " % (fecha,reg[9],reg[0])
                objreg = Registros(fechadesde=fecha,fechahasta=fecha,detreg_id= reg[9], estado=1 )
                objreg.save()
    cur.close()


def colorHexRamdom():
    from random import randrange
    return "#%s" % "".join([hex(randrange(0, 255))[2:] for i in range(3)])


def tiempoenMil(dia,mes,ano,hora,min):
    tiempo = datetime.datetime.strptime("%s-%s-%s %s:%s" %(dia,mes,ano,hora,min), "%d-%m-%Y %H:%M")
    return str(calendar.timegm(tiempo.timetuple())*1000)



def enviaTemperaturasSensor(tracksid,end_date,destinos):
    from reportes.views import llamareporte
    avisolegal="""
    <b>AVISO LEGAL</b>
    <p>
    <p>
    <p>La información incluida en el presente es SECRETO PROFESIONAL Y COFIDENCIAL, siendo para eluso exclusivo del destinatario de correo arriba mencionado. Si usted lee este mensaje y no es el destinatario señalado, el empleado o el agente responsable de entregar el mensaje al destinatario, o ha recibido esta comunicación por error, le informamos que está totalmente prohibida su divulgación o reproducción de esta comunicación y le rogamos que lo notifique inmediatamente y nos devuelva el mensaje original a la dirección arriba mencionada y borre el mensaje. Gracias</p>
    <p>
    <p>
    <p>The information contained in this e-mail is LEGALLY PRIVILEDGED AND CONFIDENTIAL, and is intended only for the use of the addressee named above. If the reader of this message is not the intended recipiente or the employee or agent responsible for delivering the message to the intended recipiente, or you have recived this communication is strictly prohibited, and please notify us immediately and returm the original message to us at the address above. Thank you</p>
    """
    de='siva@infinityloop.es'
    informe          = Informes.objects.get(descripcion='GRAFICA SENSOR TEMPERATURA')
    cd= [{'nombparametro': 'tracksid', 'valor': int(tracksid)},{ 'nombparametro': 'end_date', 'valor' : end_date }]
    data= llamareporte(informe.nombrereport,informe.url,cd)
    msg= EmailMessage("Informe Temperatura", avisolegal,'info@infinityloop.es', destinos)
    msg.attach('%s_%s.pdf' % (tracksid, end_date), data, "application/pdf" )
    msg.content_subtype = "html"
    try:
        msg.send()
    except Exception, e:
        print e

def generarBreadCrumb(path):
    allowed_ordered_breadcrumbs =['panel','lista','crear','actualizar']
    breadcrumb_list = []
    #print path
    pathNormalizado = normalizarSlash(path)
    urlsecciones= pathNormalizado.split('/')
    #urlsecciones= path.split('/')
    #print urlsecciones
    #print len(urlsecciones)
    #breadcrumb_list.append( (("panel"),"/%s/%s" %(urlsecciones[1],"panel") ))
    iter = 0
    url = '/'
    primero = True
    esDocumentos = False
    for seccion in urlsecciones:
        if seccion == "documentos":
            esDocumentos = True
            iterDocumentos = iter;
            
        url = url + seccion + '/'
        if primero:
            breadcrumb_list.append((normalizarEtiqueta(seccion),url+'panel'))
            #url = url + 'panel'
            primero = False
        else:
            #print iter
            #print breadcrumb_list
            if seccion.isdigit():
                lista = list(breadcrumb_list[iter-1])
                lista[1] = url
                tup = tuple(lista)
                breadcrumb_list.insert(iter-1, tup)
                breadcrumb_list = eliminarElementoTupla(breadcrumb_list, breadcrumb_list[iter])
                breadcrumb_list = list(breadcrumb_list)
                iter = iter -1 # se resta para no salir de rango debido a que se está eliminando un elemento del breadcrumb_list
            else:
                #breadcrumb_list = list(breadcrumb_list)        
                breadcrumb_list.append((normalizarEtiqueta(seccion),url))
                #breadcrumb_list = tuple(breadcrumb_list)
        iter = iter + 1
#         breadcrumb_list.append( ((urlsecciones[0]),"/%s/%s" %(urlsecciones[0],"panel") ))
#         if len(urlsecciones) > 1:
#             breadcrumb_list.append( ( (urlsecciones[1]),"/%s/%s/%s" %(urlsecciones[0],urlsecciones[1],"lista")) )
#         if len(urlsecciones) > 2:
#             breadcrumb_list.append(( (urlsecciones[2]),path ))

    if esDocumentos:
        breadcrumb_list = breadcrumbsDocumentos(breadcrumb_list,iterDocumentos)
        breadcrumb_list = list(breadcrumb_list)   
    print breadcrumb_list

    return breadcrumb_list


def normalizarSlash(path):
    pathNormalizado = []
    if path.startswith('/'):
        pathNormalizado =path[1:]
    if pathNormalizado.endswith('/'):
        pathNormalizado = pathNormalizado[:-1]
    print pathNormalizado
    return pathNormalizado
def eliminarElementoTupla(tupla, elemento):
    nueva_tupla = []
    for s in list(tupla):
        if not s == elemento:
            nueva_tupla.append(s)
    return tuple(nueva_tupla)

def breadcrumbsDocumentos(tupla,iterDocumento):
    nueva_tupla = []
    iter = 0
    esTratado = False
    for s in list(tupla):
        if iter == iterDocumento:
            esTratado = True
            print s
            print tupla[iter+1][1]
            lista = list(s)
            lista[1] = tupla[iter+1][1]
            tup = tuple(lista)
            nueva_tupla.insert(iter, tup)
            print nueva_tupla
            #s[1] = tupla[iter+1][1]
        else:
            if not esTratado: 
                nueva_tupla.append(s)
        iter = iter + 1     
    return tuple(nueva_tupla)

def normalizarEtiqueta(etiqueta):
    lista_etiquetas = {"panel":"Panel",
                       "appcc":"APPCC",
                       "manualautocontrol":"Manual de Auto Control",
                       "planautocontrol":"Plan de Auto Control",
                       "crear":"Crear",
                       "actualizar":"Actualizar",
                       "cabregistros": "Registros", # No se muy bien como debe ser esta etiqueta
                       "cabanaliticas":"Analíticas",
                       "detallesregistros":"Detalle de Registros",
                       "relacionesterceros":"Relación Terceros",
                       "relacionespersonal":"Relación Personal",
                       "auditorias":"Auditorías",
                       "gestorincidencias":"Gestor de Incidencias",
                       "cuadrosgestion":"Cuadro de Gestión",
                       "hijos":"Hijos",
                       # Maestros
                       "maestros":"Maestros",
                       "terceros":"Terceros",
                       "personal":"Personal",
                       "actividades":"Actividades",
                       "unidades":"Unidades",
                       "parametrosanalisis":"Parámetros Análisis",
                       "catalogoequipos":"Equipos",
                       "tipostemperaturas":"Tipos Temperaturas",
                       "zonas":"Zonas",
                       "tiposmedidasactuacion":"Tipos Medidas de Actuación",
                       "tiposmedidasvigilancia":"Tipos de Medidas Vigilancia",
                       "tiposlimitescriticos":"Tipos de Límites Críticos",
                       "tiposfrecuencias":"Tipos de Frecuencia",
                       "etapas":"Etapas de Gestión",
                       "peligros":"Peligros",
                       "tiposcursos":"Catálogo cursos",
                       "tiposlegislacion":"Legislación",
                       "tiposprocesos":"Tipos Procesos Producción",
                       "firmas":"Firmas",
                       "consumibles":"Consumibles",
                       "tiposturnos":"Tipos de Turnos",
                       # Maestros generales
                       "maestros_generales":"Maestros Generales",
                       "tiposimpuestos":"Tipos de Impuestos",
                       "tiposterceros":"Tipos de Terceros",
                       "paises":"Países",
                       "provincias":"Provincias",
                       "codigospostales":"Códigos Postales",
                       "municipios":"Municipios",
                       "empresas":"Empresas",
                       "marcas":"Marcas",
                       "tipoplancontrol":"Tipo de Plan de Control",
                       "tiposcatprofesional":"Tipo Categorías Profesional",
                       "zonasfao":"Zonas Fao",
                       "tiposdocumentos":"Tipos de Documentos",
                       "ingredientes":"Ingredientes",
                       "componentes":"Componentes Nutricionales",
                       # Productos
                       "productos":"Productos",
                       "canales":"Canales Comercialización",
                       "grupos":"Agrupaciones de Productos",
                       "tipos":"Tipos de Productos",
                       "familias":"Familias de Productos",
                       "denominacion":"Denominación Comercial",
                       "tiposenvases":"Tipos de envases",
                       "dimensiones":"Dimensiones",
                       #Trazabilidad
                       "trazabilidad":"Trazabilidad",
                       "documentos":"Documentos"}
    if etiqueta in lista_etiquetas: 
        return lista_etiquetas[etiqueta]
    else:
        return "Sin etiqueta"
    

def obtenerImagen(imagenes):

    imagen = imagenes
    aux = base64.b64encode(imagen.file)
    imagen.file = aux
    return imagen

def obtenerImagenes(imagenes):
    resImagenes = []
    for imagen in imagenes:
        aux = base64.b64encode(imagen.file)
        imagen.file = aux
        resImagenes.append(imagen)
    return resImagenes

   
    