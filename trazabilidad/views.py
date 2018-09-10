# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import DatabaseError
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin
from django.utils.translation import gettext_lazy as _
from maestros_generales.models import Empresas
from siva.utils import genericaview, detalle_template, eliminar_template, form_template,lista_template
from trazabilidad.models import Lotes, StockActual
from trazabilidad.forms import *
from django.http.response import HttpResponse, HttpResponseRedirect
from context_processors.empresa import nombre_empresa

__author__ = 'julian'

#lista_template    =  {'template_name' : "trazabilidad/list_trazabilidad.html",}
CREADO =_("creado")
ACTUA  =_("actualizado")


@login_required(login_url='/')
def trazabilidad(request):
    request.breadcrumbs(_("Trazabilidad"),request.path_info)
    lista_objeto = {'titulobox' : _("Gestión de Trazabiliad"), "contenido" : [
        {"apartado" :"Gestión" ,
         "botones" :[
             { "href":"/trazabilidad/lotes/", "titulo" : "Lotes", "icon1" : "" , "icon2" : "" } ,
             { "href":"/trazabilidad/albaranentrada/", "titulo" : "Albaranes Entrada", "icon1" : "" , "icon2" : "" },
             { "href":"/trazabilidad/albaransalida/", "titulo" : "Albaranes Salida", "icon1" : "" , "icon2" : "" },
         ]
        },
        {"apartado" :"Consultas" ,
         "botones" :[
             { "href":"/trazabilidad/existencias/", "titulo" : "Existencias / Trazabilidad", "icon1" : "" , "icon2" : "" } ,
         ]
        },

        ],}

    return render_to_response("base/panel.html",{"lista_objeto" : lista_objeto },context_instance=RequestContext(request) )



class ViewBase(object):
    extra_context={}
    model      =None
    form_class =None
    def __init__(self,modulo,etiqueta,tabla,form):
        self.modulo= modulo
        self.acciones   = { "crear" : "/trazabilidad/%s/crear" % modulo, "eliminar": "/trazabilidad/%s/eliminar" % modulo, 'ira':"/trazabilidad/detprocesos/lista" }
        self.auxiliar   = {"etiqueta" : etiqueta}
        self.cabezera   = [ etiqueta ]
        ViewBase.extra_context = {"acciones" : self.acciones, "auxiliar" : self.auxiliar, "cabezera" : self.cabezera}
        ViewBase.model = eval(tabla)
        ViewBase.form_class = eval(form)

    def get_context_data(self, **kwargs):
        context = super(ViewBase, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.empresa = Empresas.objects.get(usuario=self.request.user)
        self.object.save()
        return super(ModelFormMixin,self).form_valid(form)

    def form_invalid(self,form):
        return self.render_to_response(self.get_context_data(form=form))


    def get_success_url(self):
        return reverse('%s_list' % self.modulo )

    def get_object(self, *args, **kwargs):
        obj = super(ViewBase, self).get_object(*args, **kwargs)
        return obj

    @method_decorator(login_required(login_url="/"))
    def dispatch(self, *args, **kwargs):
        return super(ViewBase, self).dispatch(*args, **kwargs)

    def delete(self,request,*args,**kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
        except ProtectedError, error:
            messages.add_message(request, messages.ERROR, _("No se elimina, se encuentra referenciado"))
            return HttpResponseRedirect(self.get_success_url())

        return HttpResponseRedirect(self.get_success_url())


class AlbaranEntradaMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(AlbaranEntradaMixin,self).__init__("albaranentrada",_("Albaranes Entrada"),"Albaran","AlbaranEntradaForms")
        self.acciones['iradoc']='trazabilidad/documentos/lista/albaran_id/'
        self.cabezera.append("Ver")
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return Albaran.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user),tpdoc =TiposDocumentos.objects.filter(abrv="ALBIN") )

baselista            = "AlbaranEntradaMixin"
AlbaranEntradaListaView     = type(genericaview,(eval(baselista),ListView,),   {'template_name' : "trazabilidad/list_albaran_entrada.html",} )
AlbaranEntradaDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )

@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def AlbaranEntradaCrearView(request):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    #template_name = "trazabilidad/detalleslotes.html"
    template_name = "trazabilidad/albaranentrada.html"
    form        =  AlbaranEntradaForms(request.POST or None, prefix="cabecera")
    form_detail =  DetalleAlbaranEntradaFormset(request.POST or None, prefix="detalbaran")


    if form.is_valid():
        malbaran       = form.save(commit=False)
        form_detail  = DetalleAlbaranEntradaFormset( request.POST or None, instance = malbaran, prefix="detalbaran")
        print form_detail
        if form_detail.is_valid():
            print "Entro aqui"
            malbaran.save(user=request.user)
            empresa= Empresas.objects.get(usuario=request.user)
            sfset   = form_detail.save(commit=False)
            for instance in sfset:
                instance.user_id      = request.user.id
                instance.empresa      = empresa
                instance.fechaalta    = datetime.datetime.today()
                instance.albaran_id   = malbaran.id
                instance.save()

            messages.add_message(request, messages.SUCCESS, _("Albaran creado con Exito"))
            return redirect(reverse('albaranentrada_list'))
        else:
            messages.add_message(request, messages.ERROR, form_detail.errors)
    else:
        print form.errors
        messages.add_message(request, messages.ERROR, form.errors)



    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail },context_instance=RequestContext(request))


AlbaranEntradaEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )



@login_required(login_url='/')
def AlbaranEntradaActualizarView(request,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    error="N"
    template_name = "trazabilidad/albaranentrada.html"
    cabecera =   get_object_or_404(Albaran, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form        = AlbaranEntradaForms(request.POST or None,instance= cabecera, prefix="cabecera")
    print cabecera.fecha
    print form
    if form.is_valid():
        malbaran       = form.save(commit=False)
        form_detail  = DetalleAlbaranEntradaFormset( request.POST, instance = malbaran, prefix="detalbaran")
        if form_detail.is_valid():
            try:
                malbaran.save(user=request.user)
                empresa= Empresas.objects.get(usuario=request.user)
                sfset   = form_detail.save(commit=False)
                for instance in sfset:
                    instance.user_id      = request.user.id
                    instance.empresa      = empresa
                    instance.fechaalta    = datetime.datetime.today()
                    instance.albaran_id  = malbaran.id
                    try:
                        instance.save()
                    except DatabaseError, detmensaje:
                        error ="S"
                        messages.add_message(request, messages.ERROR, detmensaje[1])
                for obj in form_detail.deleted_objects:
                    obj.delete()
                if error=="N":
                    messages.add_message(request, messages.SUCCESS, _("Albaranactualizado con Exito"))
            except DatabaseError, mensaje :
                messages.add_message(request, messages.ERROR, mensaje[1])
            return redirect(reverse('albaranentrada_list'))
        else:
            messages.add_message(request, messages.ERROR, form_detail.errors)
    else:
        messages.add_message(request, messages.ERROR, form.errors)

    form_detail = DetalleAlbaranEntradaFormset( instance= cabecera, prefix="detalbaran")
    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail },context_instance=RequestContext(request))

class AlbaranSalidaMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(AlbaranSalidaMixin,self).__init__("albaransalida",_("Albaranes Salida"),"Albaran","AlbaranSalidaForms")
        self.acciones['iradoc']='trazabilidad/documentos/lista/albaran_id/'
        self.cabezera.append("Ver")
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return Albaran.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user),tpdoc =TiposDocumentos.objects.filter(abrv="ALBOUT"))

baselista            = "AlbaranSalidaMixin"
AlbaranSalidaListaView     = type(genericaview,(eval(baselista),ListView,),   {'template_name' : "trazabilidad/list_albaran_salida.html",}  )
AlbaranSalidaDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )

@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def AlbaranSalidaCrearView(request):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    #template_name = "trazabilidad/detalleslotes.html"
    template_name = "trazabilidad/albaransalida.html"
    form        =  AlbaranSalidaForms(request.POST or None, prefix="cabecera")
    form_detail =  DetalleAlbaranSalidaFormset(request.POST or None, prefix="detalbaran")
    stock = StockActual.objects.all()
    urlImpresion = None
    print "stock"
    print stock
    if form.is_valid():
        malbaran       = form.save(commit=False)
        form_detail  = DetalleAlbaranSalidaFormset( request.POST or None, instance = malbaran, prefix="detalbaran")
        if form_detail.is_valid():            
            empresa= Empresas.objects.get(usuario=request.user)
            malbaran.empresa = empresa
            malbaran.save(user=request.user)
            sfset   = form_detail.save(commit=False)
            for instance in sfset:
                instance.user_id      = request.user.id
                instance.empresa      = empresa
                instance.fechaalta    = datetime.datetime.today()
                instance.albaran_id  = malbaran.id
                instance.save()

            messages.add_message(request, messages.SUCCESS, _("Albaran creado con Exito"))
            return redirect(reverse('albaransalida_list'))
        else:
            messages.add_message(request, messages.ERROR, form_detail.errors)
    else:
        print form.errors
        messages.add_message(request, messages.ERROR, form.errors)



    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail,'urlImpresion':urlImpresion },context_instance=RequestContext(request))


AlbaranSalidaEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )



@login_required(login_url='/')
def AlbaranSalidaActualizarView(request,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    error="N"
    template_name = "trazabilidad/albaransalida.html"
    cabecera =   get_object_or_404(Albaran, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form        = AlbaranSalidaForms(request.POST or None,instance= cabecera, prefix="cabecera")
    form_detail  = DetalleAlbaranSalidaFormset( request.POST or None, instance = cabecera, prefix="detalbaran")
    informe = Informes.objects.get(descripcion = "ALBARAN SALIDA")
    urlImpresion = '/reportes/impresion/%s/%s' % (informe.pk,cabecera.pk)
    if form.is_valid():
        print "Entro en el form"
        malbaran       = form.save(commit=False)
        form_detail  = DetalleAlbaranSalidaFormset( request.POST or None, instance = malbaran, prefix="detalbaran")
        print form_detail
        if form_detail.is_valid():
            try:
                empresa= Empresas.objects.get(usuario=request.user)
                malbaran.empresa = empresa
                malbaran.save(user=request.user)
                sfset = form_detail.save(commit=False)
                for instance in sfset:
                    instance.user_id      = request.user.id
                    instance.empresa      = empresa
                    instance.fechaalta    = datetime.datetime.today()
                    try:
                        instance.save()
                    except DatabaseError, detmensaje:
                        error ="S"
                        messages.add_message(request, messages.ERROR, detmensaje[1])
                for obj in form_detail.deleted_objects:
                    obj.delete()
                if error=="N":
                    messages.add_message(request, messages.SUCCESS, _("Albaran actualizado con Exito"))
            except DatabaseError, mensaje :
                messages.add_message(request, messages.ERROR, mensaje[1])
            return redirect(reverse('albaransalida_list'))
        else:
            messages.add_message(request, messages.ERROR, form_detail.errors)
    else:
        messages.add_message(request, messages.ERROR, form.errors)

    form_detail = DetalleAlbaranSalidaFormset( instance= cabecera, prefix="detalbaran")
    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail,'urlImpresion':urlImpresion },context_instance=RequestContext(request))





#--------------------------------Documentos ------------------------------------------------------------------------------  #


def idModelotrazabilidad(modelo=None):
    if modelo.albaran_id is not None:
        return {'modelo' : 'albaran_id' , 'id': modelo.albaran_id, 'cabecera' : Albaran.objects.get(pk=modelo.albaran_id)}
    if modelo.lotes_id is not None:
        return { 'modelo' : 'lotes_id' , 'id': modelo.lotes_id, 'cabecera' : Lotes.objects.get(pk=modelo.lotes_id)}


class DocumentosMixin(ViewBase):
    def __init__(self):
        super(DocumentosMixin,self).__init__("documentos",_("Documentos"),"Documentos","DocumentosForms")
        self.cabezera.append("Abrir")
        self.cabezera.append("Acciones")

baselista      ="DocumentosMixin"


class DocumentosListaView(DocumentosMixin,ListView):

    template_name = "base/listmodal_documentos.html"

    def get_queryset(self):
        id     = self.kwargs['pid']
        modelo = self.kwargs['pmodelo']
        self.acciones['modelo']= modelo
        self.acciones ['id']   = id
        q = { "%s" % modelo : id}
        return Documentos.objects.filter(**q)


DocumentosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )


def seleccionFormDocumentos(pmodelo,pid,post,files):
    if pmodelo=='albaran_id':
        cabecera = Albaran.objects.get(pk=pid)
        return AlbaranDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo=='lotes_id':
        cabecera= Lotes.objects.get(pk=pid)
        return LotesDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")



@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def DocumentosCrearView(request,pmodelo,pid):
    template_name = "base/modal_formset.html"
    auxiliar   = {"etiqueta" : "Adjuntar Documento"}
    form_detail  = seleccionFormDocumentos(pmodelo,pid,request.POST,request.FILES)
    if form_detail.is_valid():
        guarda =form_detail.save()
        messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Documento"),CREADO) )
        return redirect(reverse('tdocumentos_list', args=(pmodelo,pid,) ))
    else:
        messages.add_message(request, messages.ERROR,  form_detail.errors)


    return render_to_response(template_name, {'form_detail' : form_detail, 'auxiliar': auxiliar },context_instance=RequestContext(request))


class  DocumentosElimina(DocumentosMixin):
    def get_success_url(self):
        parametros = idModelotrazabilidad(self.object)
        return reverse('%s_list' % self.modulo,args=(parametros['modelo'],parametros['id'],))

DocumentosEliminarView  = type(genericaview,(DocumentosElimina,DeleteView,), eliminar_template )


@login_required(login_url='/')
def DocumentosActualizarView(request,pk):
    template_name = "base/modal_formset.html"
    auxiliar   = {"etiqueta" : "Editar Documentos"}
    parametros   = idModelotrazabilidad(Documentos.objects.get(pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user)))
    form_detail  = seleccionFormDocumentos(parametros['modelo'],parametros['id'],request.POST,request.FILES)
    if form_detail.is_valid():
        guarda =form_detail.save()
        messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Documento"),ACTUA) )
        return redirect(reverse('tdocumentos_list', args=(parametros['modelo'],parametros['id'],)))
    else:
        messages.add_message(request, messages.ERROR,  form_detail.errors)


    return render_to_response(template_name, {'form_detail' : form_detail, 'auxiliar': auxiliar },context_instance=RequestContext(request))


class LotesMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(LotesMixin,self).__init__("lotes",_("Gestion Lotes"),"Lotes","LotesForms")
        self.cabezera.append("Ver")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return Lotes.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista                      ="LotesMixin"
LotesListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
LotesDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
#LotesCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template  )
#LotesCrearView     = type(genericaview,(eval(baselista),CreateView,), {'template_name' : "trazabilidad/detalleslotes.html",}  )
LotesEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
#LotesActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )
@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def LotesCrearView(request):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    #template_name = "trazabilidad/detalleslotes.html"
    template_name = "base/form.html"
    form        =  LotesForms(request.POST or None, prefix="cabecera")
    #form_detail =  DetalleAlbaranFormset(request.POST or None, prefix="detalbaran")
  
    if form.is_valid():
        print request.user.username
        mlote      = form.save(request=request)        
  
        messages.add_message(request, messages.SUCCESS, _("Lote creado con Exito"))
        return redirect(reverse('lotes_list'))
  
    else:
        print form.errors
        messages.add_message(request, messages.ERROR, form.errors)
  
  
  
    return render_to_response(template_name, {'form' : form},context_instance=RequestContext(request))


@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def LotesActualizarView(request,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    #template_name = "trazabilidad/detalleslotes.html"
    template_name = "base/form.html"
    cabecera =   get_object_or_404(Lotes, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form        = LotesForms(request.POST or None,instance= cabecera, prefix="cabecera")
    #form_detail =  DetalleAlbaranFormset(request.POST or None, prefix="detalbaran")
  
    if form.is_valid():
        print request.user.username
        mlote      = form.save(request=request)        
  
        messages.add_message(request, messages.SUCCESS, _("Lote actualizado con Exito"))
        return redirect(reverse('lotes_list'))
  
    else:
        print form.errors
        messages.add_message(request, messages.ERROR, form.errors)
  
  
  
    return render_to_response(template_name, {'form' : form},context_instance=RequestContext(request))

@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def ConsultaExistenciasView(request):
    
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    #template_name = "trazabilidad/detalleslotes.html"
    template_name = "trazabilidad/consulta_existencias.html"
    auxiliar   = {"etiqueta" : "Existencias/Trazabilidad"}
    busqueda = None
    formulario = None
    stockConsumido = 0
    stockCon = ""
    stockCantidad = 0
    stockCan = ""
    stockPeso = 0
    stockPes = ""
    urlImpresion = None
    form1 = ConsultaExistenciasForm()
    formdetail2=None
    formdetail1=None
    if 'limpiar' in request.POST:
        return HttpResponseRedirect('/trazabilidad/existencias')
    
    if 'FindAll' in request.POST:
        formulario = 'productoExistencias'
        empresa = nombre_empresa(request)['nombre_empresa']
        informe = Informes.objects.get(descripcion = "CONTROL DE EXISTENCIAS TOTAL")
        urlImpresion = '/reportes/impresion/%s/%s' % (informe.pk,empresa.pk)
        empresa = nombre_empresa(request)['nombre_empresa']
        stockActual = StockActual.objects.filter(empresa_id=empresa.pk)
        for stock in stockActual:
            if stock.peso == None:
                stockCantidad = stockCantidad + stock.cant
                if stockCantidad != 1:
                    stockCan = ("%s unidades") % stockCantidad
                else:
                    stockCan = ("%s unidad") % stockCantidad
            else:
                stockPeso = stockPeso + stock.peso
                stockPes = ("%s Kg.") % stockPeso
        formdetail2=None
        formdetail1=None
        return render_to_response(template_name, {'form1' : form1,'formdetail2' : formdetail2,'formdetail1': formdetail1,
                                              'auxiliar' :auxiliar, 'busqueda' : busqueda,'formulario': formulario,
                                               'stockConsumido': stockCon, 'stockCantidad':stockCan,'stockPeso':stockPes,
                                               'urlImpresion':urlImpresion,'stockActual':stockActual},context_instance=RequestContext(request))
            
    if request.method == 'POST':
        form1        = ConsultaExistenciasForm(request.POST or None)
        if form1.is_valid():            
            lote = form1.cleaned_data['lote']
            if lote:
                busqueda = lote
                informe = Informes.objects.get(descripcion = "CONTROL DE TRAZABILIDAD")
                urlImpresion = '/reportes/impresion/%s/%s' % (informe.pk,lote.pk)
                formulario = 'lote'                     
                detalbsal = DetalleAlbaran.objects.filter(lote=lote,albaran__tpdoc__abrv="ALBOUT")
                for det in detalbsal:
                    if det.cantidad == None:
                        stockConsumido = stockConsumido + det.peso
                        stockCon = ("%s Kg.") % stockConsumido
                    else:
                        stockConsumido = stockConsumido + det.cantidad
                        if stockConsumido != 1:
                            stockCon = ("%s unidades") % stockConsumido
                        else:
                            stockCon = ("%s unidad") % stockConsumido
                                                    
                formdetail2 = LotesDetAlbFormset(initial=detalbsal.values('referencia','id'))
                detalbent = DetalleAlbaran.objects.filter(lote=lote,albaran__tpdoc__abrv="ALBIN")
                formdetail1 = LotesDetAlbFormset(initial=detalbent.values('referencia','id'))

            producto = form1.cleaned_data['producto']
            if producto:
                formulario = 'producto'
                busqueda = producto
                informe = Informes.objects.get(descripcion = "CONTROL DE EXISTENCIAS")
                urlImpresion = '/reportes/impresion/%s/%s' % (informe.pk,producto.pk)
                lotes = Lotes.objects.filter(producto=producto)
                formdetail2 = LotesFormset(initial=lotes.values('referencia','id'))
                formdetail1 = None
                for lot in lotes:                    
                    stockActual = StockActual.objects.get(id=lot.id)
                    if stockActual.peso == None:
                        stockCantidad = stockCantidad + stockActual.cant
                        if stockCantidad != 1:
                            stockCan = ("%s unidades") % stockCantidad
                        else:
                            stockCan = ("%s unidad") % stockCantidad
                    else:
                        stockPeso = stockPeso + stockActual.peso
                        stockPes = ("%s Kg.") % stockPeso
    
    else:
        form1        = ConsultaExistenciasForm()
        formdetail1 = None
        formdetail2 = None
   
   
   
    return render_to_response(template_name, {'form1' : form1,'formdetail2' : formdetail2,'formdetail1': formdetail1,
                                              'auxiliar' :auxiliar, 'busqueda' : busqueda,'formulario': formulario,
                                               'stockConsumido': stockCon, 'stockCantidad':stockCan,'stockPeso':stockPes,
                                               'urlImpresion':urlImpresion},context_instance=RequestContext(request))

