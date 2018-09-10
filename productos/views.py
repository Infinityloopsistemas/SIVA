# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.utils.translation import gettext_lazy as _
from productos.forms import ProductosForms, ComposicionFormset
from productos.models import Canales, Grupos, Tipos, Familias, Denominacion, TiposEnvases, Dimensiones, Productos, Ingredientes
from siva.utils import *
from productos.forms import *


class ViewBase(object):
    extra_context={}
    model      =None
    form_class =None
    def __init__(self,modulo,etiqueta,tabla,form,pathprincipal):
        self.modulo= modulo
        self.acciones   = { "crear" : "/%s/%s/crear" % (pathprincipal,modulo), "eliminar": "/%s/%s/eliminar" % (pathprincipal,modulo) }
        auxiliar   = {"etiqueta" : etiqueta}
        self.cabezera   = [etiqueta]
        ViewBase.extra_context = {"acciones" : self.acciones, "auxiliar" : auxiliar, "cabezera" : self.cabezera}
        ViewBase.model = eval(tabla)
        ViewBase.form_class = eval(form)

    def get_context_data(self, **kwargs):
        context = super(ViewBase, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def form_valid(self, form):

        if User.objects.get(username=self.request.user).is_staff==True:
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.empresa = Empresas.objects.get(usuario=self.request.user)
            self.object.save()
        else:
            raise PermissionDenied

        return super(ModelFormMixin,self).form_valid(form)

    def form_invalid(self,form):
        print form.errors
        return self.render_to_response(self.get_context_data(form=form))


    def get_success_url(self):
        return reverse('%s_list' % self.modulo )

    def get_object(self, *args, **kwargs):
        obj = super(ViewBase, self).get_object(*args, **kwargs)
        if self.request.user.is_staff==False:
            raise PermissionDenied
        return obj

    @method_decorator(login_required(login_url="/"))
    def dispatch(self, *args, **kwargs):
        return super(ViewBase, self).dispatch(*args, **kwargs)

class CanalesMixin(ViewBase,BreadcrumbTemplateMixin):
    make_object_list=True
    allow_empty=True
    def __init__(self):
        super(CanalesMixin,self).__init__("canales",_("Canales Comercialización"),"Canales","CanalesForms","productos")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

    def get_queryset(self):
        return Canales.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista      ="CanalesMixin"
CanalesListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
CanalesDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
CanalesCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
CanalesEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
CanalesActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )


class GruposMixin(ViewBase,BreadcrumbTemplateMixin):
    make_object_list=True
    allow_empty=True
    def __init__(self):
        super(GruposMixin,self).__init__("grupos",_("Agrupaciones de Productos"),"Grupos","GruposForms","productos")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

    def get_queryset(self):
        return Grupos.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista      ="GruposMixin"
GruposListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
GruposDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
GruposCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
GruposEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
GruposActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )


class TiposMixin(ViewBase,BreadcrumbTemplateMixin):
    make_object_list=True
    allow_empty=True
    def __init__(self):
        super(TiposMixin,self).__init__("tipos",_("Tipos de Productos"),"Tipos","TiposForms","productos")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

    def get_queryset(self):
        return Tipos.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista      ="TiposMixin"
TiposListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
TiposDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
TiposCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
TiposEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
TiposActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )


class FamiliasMixin(ViewBase,BreadcrumbTemplateMixin):
    make_object_list=True
    allow_empty=True
    def __init__(self):
        super(FamiliasMixin,self).__init__("familias",_("Familias de Productos"),"Familias","FamiliasForms","productos")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

    def get_queryset(self):
        return Familias.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista      ="FamiliasMixin"
FamiliasListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
FamiliasDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
FamiliasCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
FamiliasEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
FamiliasActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )


class DenominacionMixin(ViewBase,BreadcrumbTemplateMixin):
    make_object_list=True
    allow_empty=True
    def __init__(self):
        super(DenominacionMixin,self).__init__("denominacion",_("Denominacion Comercial"),"Denominacion","DenominacionForms","productos")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

    def get_queryset(self):
        return Denominacion.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista      ="DenominacionMixin"
DenominacionListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
DenominacionDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
DenominacionCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
DenominacionEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
DenominacionActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )

class TiposEnvasesMixin(ViewBase,BreadcrumbTemplateMixin):
    make_object_list=True
    allow_empty=True
    def __init__(self):
        super(TiposEnvasesMixin,self).__init__("tiposenvases",_("Tipos de envases"),"TiposEnvases","TiposEnvasesForms","productos")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

    def get_queryset(self):
        return TiposEnvases.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista      ="TiposEnvasesMixin"
TiposenvasesListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
TiposenvasesDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
TiposenvasesCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
TiposenvasesEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
TiposenvasesActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )


class DimensionesMixin(ViewBase,BreadcrumbTemplateMixin):
    make_object_list=True
    allow_empty=True
    def __init__(self):
        super(DimensionesMixin,self).__init__("dimensiones",_("Dimensiones"),"Dimensiones","DimensionesForms","productos")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

    def get_queryset(self):
        return Dimensiones.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista      ="DimensionesMixin"
DimensionesListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
DimensionesDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
DimensionesCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
DimensionesEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
DimensionesActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )


class ProductosMixin(ViewBase,BreadcrumbTemplateMixin):
    make_object_list=True
    allow_empty=True
    def __init__(self):
        super(ProductosMixin,self).__init__("productos",_("Definición Producto"),"Productos","ProductosForms","productos")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

    def get_queryset(self):
        return Productos.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista      ="ProductosMixin"
ProductosListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
ProductosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
ProductosEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )





@login_required(login_url='/')
def ProductosCrearView(request):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/formset.html"

    form        = ProductosForms(request.POST or None, prefix="cabecera")
    form_detail = ComposicionFormset(request.POST or None, prefix="compo")
    if form.is_valid():
        mproductos       = form.save(commit=False)
        mproductos.user = request.user
        mproductos.empresa = get_object_or_404(Empresas,usuario=request.user)
        form_detail = ComposicionFormset( request.POST or None, instance = mproductos, prefix="compo")
        if form_detail.is_valid():

            mproductos.save()
            form_detail.save()
            messages.add_message(request, messages.SUCCESS, _("Producto creado con Exito"))
            return redirect(reverse('productos_list'))
        else:
            messages.add_message(request, messages.ERROR, form_detail.errors)
    else:
        messages.add_message(request, messages.ERROR, form.errors)



    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail },context_instance=RequestContext(request))



@login_required(login_url='/')
def ProductosActualizarView(request,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/formset.html"
    cabecera =   get_object_or_404(Productos, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form        = ProductosForms(request.POST or None,instance= cabecera, prefix="cabecera")
    if form.is_valid():
        mproductos       = form.save(commit=False)
        mproductos.user=request.user
        mproductos.empresa =  get_object_or_404(Empresas,usuario=request.user)
        form_detail = ComposicionFormset( request.POST, instance = mproductos, prefix="compo")
        if form_detail.is_valid():

            mproductos.save()
            form_detail.save()
            messages.add_message(request, messages.SUCCESS, _("Producto actualizado con Exito"))
            return redirect(reverse('productos_list'))
        else:
            messages.add_message(request, messages.ERROR, form_detail.errors)
    else:
        messages.add_message(request, messages.ERROR, form.errors)

    form_detail = ComposicionFormset( instance= cabecera, prefix="compo")
    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail },context_instance=RequestContext(request))





@login_required(login_url='/')
def productos(request):
    #objeto = ContentType.objects.filter(app_label='maestros', user=request.user);
    #Construimos el diccionario
    request.breadcrumbs(_("Productos"),request.path_info)
#     lista_objeto = {'titulobox' :"Tablas Productos", "contenido" : [
#                {"apartado" :" Agrupación" ,
#                "botones" :[
#                             { "href":"/productos/grupos/lista", "titulo" : "Grupos", "icon1" : "" , "icon2" : "icofont-asterisk" } ,
#                             { "href":"/productos/tipos/lista", "titulo" : "Tipos", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                             { "href":"/productos/familias/lista", "titulo" : "Familias", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                         ]
#                },
#                {"apartado" :"Propiedades",
#                 "botones"  : [
#                                { "href":"/productos/tiposenvases/lista", "titulo" : "Tipos Envases", "icon1" : "" , "icon2" : "icofont-asterisk color-red " },
#                                { "href":"/productos/dimensiones/lista", "titulo" : "Dimensiones", "icon1" : "" , "icon2" : "icofont-asterisk color-blue" },
#                              ]
#                 },
#                {"apartado": "Definición",
#                "botones" :
#                             [
#                                 { "href":"/productos/denominacion/lista", "titulo" : "Denominación", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                                 { "href":"/productos/productos/lista", "titulo" : "Productos", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                                 { "href":"/productos/canales/lista", "titulo" : "Canales", "icon1" : "" , "icon2" : "icofont-asterisk" } ,
#                             ]
#                }
#                    ],}
    lista_objeto = {'titulobox' :"Tablas Productos", "contenido" : [
               {"apartado" :" Agrupación" ,
               "botones" :[
                            { "href":"/productos/grupos", "titulo" : "Grupos", "icon1" : "" , "icon2" : "icofont-asterisk" } ,
                            { "href":"/productos/tipos", "titulo" : "Tipos", "icon1" : "" , "icon2" : "icofont-asterisk" },
                            { "href":"/productos/familias", "titulo" : "Familias", "icon1" : "" , "icon2" : "icofont-asterisk" },
                        ]
               },
               {"apartado" :"Propiedades",
                "botones"  : [
                               { "href":"/productos/tiposenvases", "titulo" : "Tipos Envases", "icon1" : "" , "icon2" : "icofont-asterisk color-red " },
                               { "href":"/productos/dimensiones", "titulo" : "Dimensiones", "icon1" : "" , "icon2" : "icofont-asterisk color-blue" },
                             ]
                },
               {"apartado": "Definición",
               "botones" :
                            [
                                { "href":"/productos/denominacion", "titulo" : "Denominación", "icon1" : "" , "icon2" : "icofont-asterisk" },
                                { "href":"/productos/productos", "titulo" : "Productos", "icon1" : "" , "icon2" : "icofont-asterisk" },
                                { "href":"/productos/canales", "titulo" : "Canales", "icon1" : "" , "icon2" : "icofont-asterisk" } ,
                            ]
               }
                   ],}

    return render_to_response("base/panel.html",{"lista_objeto" : lista_objeto },context_instance=RequestContext(request) )
