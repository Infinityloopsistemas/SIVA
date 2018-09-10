# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.context_processors import request
from django.core.urlresolvers import reverse
from django.db.models import ProtectedError
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from maestros_generales.forms import *
from maestros_generales.models import *
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext, Context
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from siva.utils import *


class ViewBase(object):
    extra_context={}
    model      =None
    form_class =None
    def __init__(self,modulo,etiqueta,tabla,form):
        self.modulo= modulo
        acciones   = { "crear" : "/maestros_generales/%s/crear" % modulo, "eliminar": "/maestros_generales/%s/eliminar" % modulo }
        auxiliar   = {"etiqueta" : etiqueta}
        cabezera   = { etiqueta, "Acciones"}
        ViewBase.extra_context = {"acciones" : acciones, "auxiliar" : auxiliar, "cabezera" : cabezera}
        ViewBase.model = eval(tabla)
        ViewBase.form_class = eval(form)

    def get_context_data(self, **kwargs):
        context = super(ViewBase, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def form_valid(self, form):
        if User.objects.get(username=self.request.user).is_staff==True:
            self.success_message = "Actualizado Correctamente"
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
        else:
            raise PermissionDenied
        return super(ModelFormMixin,self).form_valid(form)

    def form_invalid(self,form):
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

    def delete(self,request,*args,**kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
        except ProtectedError, error:
            messages.add_message(request, messages.ERROR, _("No se elimina, se encuentra referenciado"))
            return HttpResponseRedirect(self.get_success_url())

        return HttpResponseRedirect(self.get_success_url())





class TiposDocumentosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposDocumentosMixin,self).__init__("tiposdocumentos",_("Tipos de Documentos"),"TiposDocumentos","TiposDocumentosForms")


baselista      ="TiposDocumentosMixin"
TiposdocumentosListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
TiposdocumentosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
TiposdocumentosCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
TiposdocumentosEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
TiposdocumentosActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )


class TiposImpuestosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposImpuestosMixin,self).__init__("tiposimpuestos",_("Tipos de Impuestos"),"TiposImpuestos","TiposImpuestosForms")



baselista      ="TiposImpuestosMixin"
TiposimpuestosListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
TiposimpuestosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
TiposimpuestosCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
TiposimpuestosEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
TiposimpuestosActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )



class TiposTercerosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposTercerosMixin,self).__init__("tiposterceros",_("Tipos de Terceros"),"TiposTerceros","TiposTercerosForms")


baselista      ="TiposTercerosMixin"
TipostercerosListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
TipostercerosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
TipostercerosCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
TipostercerosEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
TipostercerosActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )





class PaisesMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(PaisesMixin,self).__init__("paises",_("Paises"),"Paises","PaisesForms")


baselista      ="PaisesMixin"
PaisesListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
PaisesDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
PaisesCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
PaisesEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
PaisesActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )



class ProvinciasMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(ProvinciasMixin,self).__init__("provincias",_("Provincias"),"Provincias","ProvinciasForms")

baselista      ="ProvinciasMixin"
ProvinciasListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
ProvinciasDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
ProvinciasCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
ProvinciasEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
ProvinciasActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )

class CodigosPostalesMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(CodigosPostalesMixin,self).__init__("codigospostales",_("Códigos Postales"),"CodigosPostales","CodigosPostalesForms")

baselista                      ="CodigosPostalesMixin"
CodigospostalesListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
CodigospostalesDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
CodigospostalesCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
CodigospostalesEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
CodigospostalesActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )


class MunicipiosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(MunicipiosMixin,self).__init__("municipios",_("Municipios"),"Municipios","MunicipiosForms")


baselista      ="MunicipiosMixin"
MunicipiosListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
MunicipiosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
MunicipiosCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
MunicipiosEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
MunicipiosActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )





class EmpresasMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(EmpresasMixin,self).__init__("empresas",_("Empresas"),"Empresas","EmpresasForms")

baselista                      ="EmpresasMixin"
EmpresasListaView     = type(genericaview,(eval(baselista),ListView,),    lista_template )
EmpresasDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
EmpresasCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
EmpresasEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
EmpresasActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template)



class MarcasMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(MarcasMixin,self).__init__("marcas",_("Marcas"),"Marcas","MarcasForms")

baselista           ="MarcasMixin"
MarcasListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
MarcasDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
MarcasCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
MarcasEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
MarcasActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )



class TipoPlanControlMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TipoPlanControlMixin,self).__init__("tipoplancontrol",_("Tipo de Plan de Control"),"TipoPlanControl","TipoPlanControlForms")

baselista                      ="TipoPlanControlMixin"
TipoplancontrolListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
TipoplancontrolDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
TipoplancontrolCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
TipoplancontrolEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
TipoplancontrolActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )



class TiposCatProfesionalMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposCatProfesionalMixin,self).__init__("tiposcatprofesional",_("Tipo Categorias Profesional"),"TiposCatProfesional","TiposCatProfesionalForms")

baselista                      ="TiposCatProfesionalMixin"
TiposcatprofesionalListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
TiposcatprofesionalDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
TiposcatprofesionalCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
TiposcatprofesionalEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
TiposcatprofesionalActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )



class ZonasFaoMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(ZonasFaoMixin,self).__init__("zonasfao",_("Zonas Fao"),"ZonasFao","ZonasFaoForms")

baselista                      ="ZonasFaoMixin"
ZonasfaoListaView     = type(genericaview,(eval(baselista),ListView,), lista_template )
ZonasfaoDetalleView   = type(genericaview,(eval(baselista),DetailView,),detalle_template  )
ZonasfaoCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
ZonasfaoEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
ZonasfaoActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )


class IngredientesMixin(ViewBase,BreadcrumbTemplateMixin):
    make_object_list=True
    allow_empty=True
    def __init__(self):
        super(IngredientesMixin,self).__init__("ingredientes",_("Ingredientes"),"Ingredientes","IngredientesForms")


baselista      ="IngredientesMixin"
IngredientesListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
IngredientesDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
IngredientesCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
IngredientesEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
IngredientesActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )


class ComponentesMixin(ViewBase,BreadcrumbTemplateMixin):
    make_object_list=True
    allow_empty=True
    def __init__(self):
        super(ComponentesMixin,self).__init__("componentes",_("Componentes Nutricionales"),"Componentes","ComponentesForms")


baselista      ="ComponentesMixin"
ComponentesListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
ComponentesDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
ComponentesCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
ComponentesEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
ComponentesActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )


@login_required(login_url='/')
def maestros_generales(request):
    #objeto = ContentType.objects.filter(app_label='maestros', user=request.user);
    #Construimos el diccionario
    request.breadcrumbs(_("Maestros Generales"),request.path_info)
#     lista_objeto = {'titulobox' :"Tablas Maestras Generales", "contenido" : [
#                {"apartado" :" Tipos" ,
#                "botones" :[
#                             { "href":"/maestros_generales/tipoplancontrol/lista", "titulo" : "Tipo Plan de Control", "icon1" : "icon-list-alt" , "icon2" : "icon-list-alt color-red" } ,
#                             { "href":"/maestros_generales/tiposterceros/lista", "titulo" : "Tipos de Terceros", "icon1" : "" , "icon2" : "" },
#                             { "href":"/maestros_generales/tiposimpuestos/lista", "titulo" : "Tipos de Impuestos", "icon1" : "" , "icon2" : "" },
#                             { "href":"/maestros_generales/tiposcatprofesional/lista", "titulo" : "Tipos Categorias Profesionales", "icon1" : "" , "icon2" : "" },
#                             { "href":"/maestros_generales/tiposdocumentos/lista", "titulo" : "Tipos Documentos", "icon1" : "" , "icon2" : "" },
#                         ]
#                },
#                {"apartado" :"Geograficos",
#                 "botones"  : [
#                                { "href":"/maestros_generales/paises/lista", "titulo" : "Paises", "icon1" : "icon-map-marker" , "icon2" : "icon-repeat color-tea" },
#                                { "href":"/maestros_generales/provincias/lista", "titulo" : "Provincias", "icon1" : "iconfont-picture" , "icon2" : "icon-adjust color-yellow" },
#                                { "href":"/maestros_generales/municipios/lista", "titulo" : "Municipios", "icon1" : "" , "icon2" : "" },
#                                { "href":"/maestros_generales/codigospostales/lista", "titulo" : "Codigos Postales", "icon1" : "" , "icon2" : "" },
#                                { "href":"/maestros_generales/zonasfao/lista", "titulo" : "Zonas Fao", "icon1" : "" , "icon2" : "icon-adjust color-red" },
# 
#                              ]
#                 },
#                {"apartado": "Alimentos",
#                "botones" :
#                             [
#                                { "href":"/maestros_generales/ingredientes/lista", "titulo" : "Ingredientes", "icon1" : "" , "icon2" : "icofont-asterisk color-red" },
#                                { "href":"/maestros_generales/componentes/lista", "titulo" : "Componenetes Nutricionales", "icon1" : "" , "icon2" : "icofont-asterisk color-red" },
#                             ]
#                },
#                {"apartado": "Negocios",
#                "botones" :
#                             [
#                                 { "href":"/maestros_generales/marcas/lista", "titulo" : "Marcas", "icon1" : "" , "icon2" : "" },
#                                # { "href":"/maestros_generales/empresas/lista", "titulo" : "Empresas", "icon1" : "icofont-chevron-up" , "icon2" : "icon-adjust" },
#                             ]
#                }
#                    ],}
    lista_objeto = {'titulobox' :"Tablas Maestras Generales", "contenido" : [
               {"apartado" :" Tipos" ,
               "botones" :[
                            { "href":"/maestros_generales/tipoplancontrol", "titulo" : "Tipo Plan de Control", "icon1" : "icon-list-alt" , "icon2" : "icon-list-alt color-red" } ,
                            { "href":"/maestros_generales/tiposterceros", "titulo" : "Tipos de Terceros", "icon1" : "" , "icon2" : "" },
                            { "href":"/maestros_generales/tiposimpuestos", "titulo" : "Tipos de Impuestos", "icon1" : "" , "icon2" : "" },
                            { "href":"/maestros_generales/tiposcatprofesional", "titulo" : "Tipos Categorias Profesionales", "icon1" : "" , "icon2" : "" },
                            { "href":"/maestros_generales/tiposdocumentos", "titulo" : "Tipos Documentos", "icon1" : "" , "icon2" : "" },
                        ]
               },
               {"apartado" :"Geograficos",
                "botones"  : [
                               { "href":"/maestros_generales/paises", "titulo" : "Paises", "icon1" : "icon-map-marker" , "icon2" : "icon-repeat color-tea" },
                               { "href":"/maestros_generales/provincias", "titulo" : "Provincias", "icon1" : "iconfont-picture" , "icon2" : "icon-adjust color-yellow" },
                               { "href":"/maestros_generales/municipios", "titulo" : "Municipios", "icon1" : "" , "icon2" : "" },
                               { "href":"/maestros_generales/codigospostales", "titulo" : "Codigos Postales", "icon1" : "" , "icon2" : "" },
                               { "href":"/maestros_generales/zonasfao", "titulo" : "Zonas Fao", "icon1" : "" , "icon2" : "icon-adjust color-red" },

                             ]
                },
               {"apartado": "Alimentos",
               "botones" :
                            [
                               { "href":"/maestros_generales/ingredientes", "titulo" : "Ingredientes", "icon1" : "" , "icon2" : "icofont-asterisk color-red" },
                               { "href":"/maestros_generales/componentes", "titulo" : "Componenetes Nutricionales", "icon1" : "" , "icon2" : "icofont-asterisk color-red" },
                            ]
               },
               {"apartado": "Negocios",
               "botones" :
                            [
                                { "href":"/maestros_generales/marcas", "titulo" : "Marcas", "icon1" : "" , "icon2" : "" },
                               # { "href":"/maestros_generales/empresas/lista", "titulo" : "Empresas", "icon1" : "icofont-chevron-up" , "icon2" : "icon-adjust" },
                            ]
               }
                   ],}


    return render_to_response("base/panel.html",{"lista_objeto" : lista_objeto },context_instance=RequestContext(request) )
