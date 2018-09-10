# -*- coding: utf-8 -*-
from logging import exception
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.context_processors import request
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.db.backends.mysql.base import IntegrityError
from django.db.models import ProtectedError
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from maestros.forms import *
from maestros.models import *
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext, Context
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from siva.utils import *
import codecs




class ViewBase(object):
    extra_context={}
    model      =None
    form_class =None
    def __init__(self,modulo,etiqueta,tabla,form):
        self.modulo= modulo
        self.acciones   = { "crear" : "/maestros/%s/crear" % modulo, "eliminar": "/maestros/%s/eliminar" % modulo }
        auxiliar   = {"etiqueta" : etiqueta}
        self.cabezera    = [etiqueta]
        ViewBase.extra_context = {"acciones" : self.acciones, "auxiliar" : auxiliar, "cabezera" : self.cabezera}
        ViewBase.model = eval(tabla)
        ViewBase.form_class = eval(form)

    def get_context_data(self, **kwargs):
        context = super(ViewBase, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def delete(self,request,*args,**kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
        except ProtectedError, error:
            messages.add_message(request, messages.ERROR, _("No se elimina, se encuentra referenciado"))
            return HttpResponseRedirect(self.get_success_url())

        return HttpResponseRedirect(self.get_success_url())

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


class TercerosMixin(ViewBase,BreadcrumbTemplateMixin):
    make_object_list=True
    allow_empty=True
    def __init__(self):
        super(TercerosMixin,self).__init__("terceros",_("Terceros"),"Terceros","TercerosForms")
        self.cabezera.append("Ver")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

    def get_queryset(self):
        return Terceros.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user),fechabaja=None)

baselista      ="TercerosMixin"
TercerosListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
TercerosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
TercerosCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
TercerosEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
TercerosActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )



class PersonalMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(PersonalMixin,self).__init__("personal",_("Personal"),"Personal","PersonalForms")
        self.cabezera.append('Ver')
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return Personal.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user),fechabaja=None)

baselista      ="PersonalMixin"
PersonalListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
PersonalDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
PersonalCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )

PersonalEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def PersonalActualizarView(request,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    print request.FILES
    template_name      = "maestros/personalForm.html"
    pers = get_object_or_404(Personal,pk=pk)
    form               = PersonalForms(request.POST or None,instance = pers)
    if form.is_valid():
        if request.FILES:
            personal = form.save(user=request.user)            
            for fichero in request.FILES:                    
                ct = get_object_or_404(ContentType,model=personal.__class__.__name__.lower())
                try:                            
                    imagen = Imagen.objects.get(content_type=ct,object_id=personal.pk)                            
                    imagen.file =  request.FILES[fichero].read()
                    imagen.content_type_file= request.FILES[fichero].content_type
                    imagen.save()
                except Imagen.DoesNotExist:                        
                    personal.imagen.create(denominacion=request.FILES[fichero].name, file=request.FILES[fichero].read(),content_type_file=request.FILES[fichero].content_type,object_id=personal.pk,content_type=ct.pk)
              
        else:
            personal = form.save(user=request.user)
                   
        return redirect(reverse('personal_list'))
    else:
        messages.add_message(request, messages.ERROR,  form.errors)
    return render_to_response(template_name, {'form' : form},context_instance=RequestContext(request))
#PersonalActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )


class FirmasMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(FirmasMixin,self).__init__("firmas",_("Personal Autorizado"),"Firmas","FirmasForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return Firmas.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user),fechabaja=None)

baselista           ="FirmasMixin"
FirmasListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
FirmasDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
FirmasCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
FirmasEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
FirmasActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )






class ActividadesMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(ActividadesMixin,self).__init__("actividades",_("Actividades"),"Actividades","ActividadesForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return Actividades.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista      ="ActividadesMixin"
ActividadesListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
ActividadesDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
ActividadesCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
ActividadesEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
ActividadesActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )



class UnidadesMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(UnidadesMixin,self).__init__("unidades",_("Unidades"),"Unidades","UnidadesForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

    def get_queryset(self):
        return Unidades.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista      ="UnidadesMixin"
UnidadesListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
UnidadesDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
UnidadesCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
UnidadesEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
UnidadesActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )

class ParametrosAnalisisMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(ParametrosAnalisisMixin,self).__init__("parametrosanalisis",_("Parametros Analisis"),"ParametrosAnalisis","ParametrosAnalisisForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return ParametrosAnalisis.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista                      ="ParametrosAnalisisMixin"
ParametrosanalisisListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
ParametrosanalisisDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
ParametrosanalisisCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
ParametrosanalisisEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
ParametrosanalisisActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )


class CatalgoequiposMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(CatalgoequiposMixin,self).__init__("catalogoequipos",_("Equipos"),"CatalogoEquipos","CatalogoEquiposForms")
        self.cabezera.append("Ver")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return CatalogoEquipos.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista      ="CatalgoequiposMixin"
CatalogoequiposListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template)
CatalogoequiposDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
CatalogoequiposCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
CatalogoequiposEliminarView  = type(genericaview,(eval(baselista),DeleteView,),  eliminar_template )
CatalogoequiposActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template )





class TiposTemperaturasMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposTemperaturasMixin,self).__init__("tipostemperaturas",_("Tipos Temperaturas"),"TiposTemperaturas","TiposTemperaturasForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return TiposTemperaturas.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista                      ="TiposTemperaturasMixin"
TipostemperaturasListaView     = type(genericaview,(eval(baselista),ListView,),    lista_template )
TipostemperaturasDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )
TipostemperaturasCrearView     = type(genericaview,(eval(baselista),CreateView,), form_template )
TipostemperaturasEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template )
TipostemperaturasActualizarView= type(genericaview,(eval(baselista),UpdateView,), form_template)



class ZonasMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(ZonasMixin,self).__init__("zonas",_("Zonas"),"Zonas","ZonasForms")
        self.cabezera.append("Ver")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return Zonas.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista                      ="ZonasMixin"
ZonasListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
ZonasDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
ZonasCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
ZonasEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
ZonasActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )



class TiposMedidasActuacionMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposMedidasActuacionMixin,self).__init__("tiposmedidasactuacion",_("Tipos Medidas de Actuacion"),"TiposMedidasActuacion","TiposMedidasActuacionForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return TiposMedidasActuacion.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista                      ="TiposMedidasActuacionMixin"
TiposmedidasactuacionListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
TiposmedidasactuacionDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
TiposmedidasactuacionCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
TiposmedidasactuacionEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
TiposmedidasactuacionActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )


class TiposMedidasVigilanciaMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposMedidasVigilanciaMixin,self).__init__("tiposmedidasvigilancia",_("Tipos de Medidas Vigilancia"),"TiposMedidasVigilancia","TiposMedidasVigilanciaForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return TiposMedidasVigilancia.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista                      ="TiposMedidasVigilanciaMixin"
TiposmedidasvigilanciaListaView      = type(genericaview,(eval(baselista),ListView,),   lista_template )
TiposmedidasvigilanciaDetalleView    = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
TiposmedidasvigilanciaCrearView      = type(genericaview,(eval(baselista),CreateView,),form_template  )
TiposmedidasvigilanciaEliminarView   = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
TiposmedidasvigilanciaActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )



class TiposLimitesCriticosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposLimitesCriticosMixin,self).__init__("tiposlimitescriticos",_("Tipos de Limites Criticos"),"TiposLimitesCriticos","TiposLimitesCriticosForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return TiposLimitesCriticos.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista                            ="TiposLimitesCriticosMixin"
TiposlimitescriticosListaView      = type(genericaview,(eval(baselista),ListView,),   lista_template )
TiposlimitescriticosDetalleView    = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
TiposlimitescriticosCrearView      = type(genericaview,(eval(baselista),CreateView,),form_template  )
TiposlimitescriticosEliminarView   = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
TiposlimitescriticosActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )



class ConsumiblesMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(ConsumiblesMixin,self).__init__("consumibles",_("Consumibles"),"Consumibles","ConsumiblesForms")
        self.cabezera.append("Ver")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return Consumibles.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista                      ="ConsumiblesMixin"
ConsumiblesListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
ConsumiblesDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )


@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def ConsumiblesCrearView(request):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/formset.html"
    form        = ConsumiblesForms(request.POST or None, prefix="cabecera")
    form_detail = ConsumEspeciFormset(request.POST or None, prefix="conespeci")
    if form.is_valid():
        mconsumibles       = form.save(commit=False)
        form_detail = ConsumEspeciFormset( request.POST or None, instance = mconsumibles, prefix="conespeci")
        if form_detail.is_valid():
            mconsumibles.save(user=request.user)
            form_detail.save()
            messages.add_message(request, messages.SUCCESS, _("Consumible creado con Exito"))
            return redirect(reverse('consumibles_list'))
        else:
            messages.add_message(request, messages.ERROR, form_detail.errors)
    else:
        messages.add_message(request, messages.ERROR, form.errors)



    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail },context_instance=RequestContext(request))


ConsumiblesEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )



@login_required(login_url='/')
def ConsumiblesActualizarView(request,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/formset.html"
    cabecera =   get_object_or_404(Consumibles, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form        = ConsumiblesForms(request.POST or None,instance= cabecera, prefix="cabecera")
    if form.is_valid():
        mconsumibles       = form.save(commit=False)
        form_detail = ConsumEspeciFormset( request.POST, instance = mconsumibles, prefix="conespeci")
        if form_detail.is_valid():
            mconsumibles.save(user=request.user)
            form_detail.save()
            messages.add_message(request, messages.SUCCESS, _("Consumible actualizado con Exito"))
            return redirect(reverse('consumibles_list'))
        else:
            messages.add_message(request, messages.ERROR, form_detail.errors)
    else:
        messages.add_message(request, messages.ERROR, form.errors)

    form_detail = ConsumEspeciFormset( instance= cabecera, prefix="conespeci")
    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail },context_instance=RequestContext(request))



####################################################### TIPOS TURNOS ##############################################################################

class TiposTurnosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposTurnosMixin,self).__init__("tiposturnos",_("Tipos de Turnos"),"TiposTurnos","TiposTurnosForms")
        self.cabezera.append("Ver")
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return TiposTurnos.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista                = "TiposTurnosMixin"
TiposturnosListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
TiposturnosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )


@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def TiposturnosCrearView(request):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/formset.html"
    head_detail =['Hora Inicio','Hora Fin']
    form        = TiposTurnosForms(request.POST or None, prefix="cabecera")
    form_detail = HorarioTurnosFormset(request.POST or None, prefix="horariostur")
    if form.is_valid():
        mcabecera       = form.save(commit=False)
        form_detail = HorarioTurnosFormset( request.POST or None, instance = mcabecera, prefix="horariostur")
        if form_detail.is_valid():
            mcabecera.save(user=request.user)
            form_detail.save()
            messages.add_message(request, messages.SUCCESS, _("Turno creado con Exito"))
            return redirect(reverse('tiposturnos_list'))
        else:
            messages.add_message(request, messages.ERROR, form_detail.errors)
    else:
        messages.add_message(request, messages.ERROR, form.errors)

    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail , 'head_detail' : head_detail },context_instance=RequestContext(request))


TiposturnosEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )


@login_required(login_url='/')
def TiposturnosActualizarView(request,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/formset.html"
    head_detail =['Hora Inicio','Hora Fin']
    cabecera =   get_object_or_404(TiposTurnos, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form        = TiposTurnosForms(request.POST or None,instance= cabecera, prefix="cabecera")
    if form.is_valid():
        mcabecera       = form.save(commit=False)
        form_detail = HorarioTurnosFormset( request.POST, instance = mcabecera, prefix="horariostur")
        if form_detail.is_valid():
            mcabecera.save(user=request.user)
            form_detail.save()
            messages.add_message(request, messages.SUCCESS, _("Tipos Turnos actualizado con Exito"))
            return redirect(reverse('tiposturnos_list'))
        else:
            messages.add_message(request, messages.ERROR, form_detail.errors)
    else:
        messages.add_message(request, messages.ERROR, form.errors)

    form_detail = HorarioTurnosFormset( instance= cabecera, prefix="horariostur")
    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail, 'head_detail' : head_detail },context_instance=RequestContext(request))







##################################################### FIN TIPOS TURNOS ############################################################################




class TiposFrecuenciasMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposFrecuenciasMixin,self).__init__("tiposfrecuencias",_("Tipos de Frecuencia"),"TiposFrecuencias","TiposFrecuenciasForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return TiposFrecuencias.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))



baselista                      ="TiposFrecuenciasMixin"
TiposfrecuenciasListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
TiposfrecuenciasDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
TiposfrecuenciasCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
TiposfrecuenciasEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
TiposfrecuenciasActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )



class TiposProcesosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposProcesosMixin,self).__init__("tiposprocesos",_("Tipos Procesos Producción"),"TiposProcesos","TiposProcesosForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return TiposProcesos.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))



baselista                      ="TiposProcesosMixin"
TiposprocesosListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
TiposprocesosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
TiposprocesosCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
TiposprocesosEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
TiposprocesosActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )


class EtapasMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(EtapasMixin,self).__init__("etapas",_("Etapas de Gestión"),"Etapas","EtapasForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return Etapas.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))
baselista                      ="EtapasMixin"
EtapasListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
EtapasDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
EtapasCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
EtapasEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
EtapasActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )


class PeligrosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(PeligrosMixin,self).__init__("peligros",_("Peligros"),"Peligros","PeligrosForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return Peligros.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))
baselista                      ="PeligrosMixin"
PeligrosListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
PeligrosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
PeligrosCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
PeligrosEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
PeligrosActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )


class TiposCursosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposCursosMixin,self).__init__("tiposcursos",_("Catalogo Cursos"),"TiposCursos","TiposCursosForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return TiposCursos.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista                      ="TiposCursosMixin"
TiposcursosListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
TiposcursosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
TiposcursosCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
TiposcursosEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
TiposcursosActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )


class TiposLegislaMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(TiposLegislaMixin,self).__init__("tiposlegislacion",_("Legislación"),"TiposLegislacion","TiposLegislacionForms")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")
    def get_queryset(self):
        return TiposLegislacion.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista                      ="TiposLegislaMixin"
TiposlegislacionListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
TiposlegislacionDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )
TiposlegislacionCrearView     = type(genericaview,(eval(baselista),CreateView,),form_template  )
TiposlegislacionEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )
TiposlegislacionActualizarView= type(genericaview,(eval(baselista),UpdateView,),form_template )




@login_required(login_url='/')
def maestros(request):
    #objeto = ContentType.objects.filter(app_label='maestros', user=request.user);
    #Construimos el diccionario
    request.breadcrumbs(_("Maestros"),request.path_info)
#     lista_objeto = {'titulobox' :"Tablas Maestras", "contenido" : [
#                {"apartado" :" Tipos" ,
#                "botones" :[
#                             { "href":"/maestros/tiposmedidasactuacion/lista", "titulo" : "Tipos medidas de Actuacion", "icon1" : "" , "icon2" : "icofont-asterisk" } ,
#                             { "href":"/maestros/tiposlimitescriticos/lista", "titulo" : "Tipos medidas de Limites Criticos", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                             { "href":"/maestros/tiposmedidasvigilancia/lista", "titulo" : "Tipos medidas de Vigilancia", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                             { "href":"/maestros/actividades/lista", "titulo" : "Actividades", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                             { "href":"/maestros/etapas/lista", "titulo"   : "Etapas", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                             { "href":"/maestros/peligros/lista", "titulo" : "Peligros", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                             { "href":"/maestros/tiposcursos/lista", "titulo" : "Catalogo Cursos", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                             { "href":"/maestros/tiposlegislacion/lista", "titulo" : "Tipos Legislación", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                         ]
#                },
#                {"apartado" :"Inventariables",
#                 "botones"  : [
#                                { "href":"/maestros/catalogoequipos/lista", "titulo" : "Catalogo de Equipos", "icon1" : "" , "icon2" : "icofont-asterisk color-red " },
#                                { "href":"/maestros/consumibles/lista", "titulo" : "Consumibles", "icon1" : "" , "icon2" : "icofont-asterisk color-blue" },
#                                { "href":"/maestros/zonas/lista", "titulo" : "Zonas", "icon1" : "" , "icon2" : "icofont-asterisk color-red" },
#                              ]
#                 },
#                {"apartado": "Parametros",
#                "botones" :
#                             [
#                                 { "href":"/maestros/tiposfrecuencias/lista", "titulo" : "Tipos Frecuencia", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                                 { "href":"/maestros/tipostemperaturas/lista", "titulo" : "Tipos Temperaturas", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                                 { "href":"/maestros/parametrosanalisis/lista", "titulo" : "Parametros Analisis", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                                 { "href":"/maestros/unidades/lista", "titulo" : "Unidades", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                                 { "href":"/maestros/tiposprocesos/lista", "titulo" : "Tipos Procesos", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                                  { "href":"/maestros/tiposturnos/lista", "titulo" : "Tipos Turnos", "icon1" : "" , "icon2" : "icofont-asterisk" }
#                             ]
#                },
#                {"apartado": "Entes",
#                "botones" :
#                             [
#                                 { "href":"/maestros/terceros/lista", "titulo" : "Terceros", "icon1" : "" , "icon2" : "icofont-asterisk" },
#                                 { "href":"/maestros/personal/lista", "titulo" : "Datos Personas", "icon1" : "" , "icon2" : "socialico-aim" },
#                                 { "href":"/maestros/firmas/lista", "titulo" :   "Personal Autorizado", "icon1" : "" , "icon2" : "socialico-aim" }
#                             ]
#                }
#                    ],}

    lista_objeto = {'titulobox' :"Tablas Maestras", "contenido" : [
               {"apartado" :" Tipos" ,
               "botones" :[
                            { "href":"/maestros/tiposmedidasactuacion", "titulo" : "Tipos medidas de Actuacion", "icon1" : "" , "icon2" : "icofont-asterisk" } ,
                            { "href":"/maestros/tiposlimitescriticos", "titulo" : "Tipos medidas de Limites Criticos", "icon1" : "" , "icon2" : "icofont-asterisk" },
                            { "href":"/maestros/tiposmedidasvigilancia", "titulo" : "Tipos medidas de Vigilancia", "icon1" : "" , "icon2" : "icofont-asterisk" },
                            { "href":"/maestros/actividades", "titulo" : "Actividades", "icon1" : "" , "icon2" : "icofont-asterisk" },
                            { "href":"/maestros/etapas", "titulo"   : "Etapas", "icon1" : "" , "icon2" : "icofont-asterisk" },
                            { "href":"/maestros/peligros", "titulo" : "Peligros", "icon1" : "" , "icon2" : "icofont-asterisk" },
                            { "href":"/maestros/tiposcursos", "titulo" : "Catalogo Cursos", "icon1" : "" , "icon2" : "icofont-asterisk" },
                            { "href":"/maestros/tiposlegislacion", "titulo" : "Tipos Legislación", "icon1" : "" , "icon2" : "icofont-asterisk" },
                        ]
               },
               {"apartado" :"Inventariables",
                "botones"  : [
                               { "href":"/maestros/catalogoequipos", "titulo" : "Catalogo de Equipos", "icon1" : "" , "icon2" : "icofont-asterisk color-red " },
                               { "href":"/maestros/consumibles", "titulo" : "Consumibles", "icon1" : "" , "icon2" : "icofont-asterisk color-blue" },
                               { "href":"/maestros/zonas", "titulo" : "Zonas", "icon1" : "" , "icon2" : "icofont-asterisk color-red" },
                             ]
                },
               {"apartado": "Parametros",
               "botones" :
                            [
                                { "href":"/maestros/tiposfrecuencias", "titulo" : "Tipos Frecuencia", "icon1" : "" , "icon2" : "icofont-asterisk" },
                                { "href":"/maestros/tipostemperaturas", "titulo" : "Tipos Temperaturas", "icon1" : "" , "icon2" : "icofont-asterisk" },
                                { "href":"/maestros/parametrosanalisis", "titulo" : "Parametros Analisis", "icon1" : "" , "icon2" : "icofont-asterisk" },
                                { "href":"/maestros/unidades", "titulo" : "Unidades", "icon1" : "" , "icon2" : "icofont-asterisk" },
                                { "href":"/maestros/tiposprocesos", "titulo" : "Tipos Procesos", "icon1" : "" , "icon2" : "icofont-asterisk" },
                                 { "href":"/maestros/tiposturnos", "titulo" : "Tipos Turnos", "icon1" : "" , "icon2" : "icofont-asterisk" }
                            ]
               },
               {"apartado": "Entes",
               "botones" :
                            [
                                { "href":"/maestros/terceros", "titulo" : "Terceros", "icon1" : "" , "icon2" : "icofont-asterisk" },
                                { "href":"/maestros/personal", "titulo" : "Datos Personas", "icon1" : "" , "icon2" : "socialico-aim" },
                                { "href":"/maestros/firmas", "titulo" :   "Personal Autorizado", "icon1" : "" , "icon2" : "socialico-aim" }
                            ]
               }
                   ],}
    return render_to_response("base/panel.html",{"lista_objeto" : lista_objeto },context_instance=RequestContext(request) )



#------------------------------------------Documentos ----------------------------------------------#

def idModelomaestros(modelo=None):
    if modelo.terceros_id is not None:
        return {'modelo' : 'terceros_id',    'id': modelo.terceros_id}
    if modelo.personal_id is not None:
        return {'modelo' : 'personal_id' ,   'id': modelo.personal_id}
    if modelo.zonas_id is not None:
        return { 'modelo' : 'zonas_id' ,     'id': modelo.zonas_id}
    if modelo.catequipos_id is not None:
        return {'modelo' : 'catequipos_id' , 'id': modelo.catequipos_id }
    if modelo.consumibles_id is not None:
        return {'modelo': 'consumibles_id',  'id' :modelo.consumibles_id }


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
        q = { "%s" % modelo : id }
        return Documentos.objects.filter(**q)


DocumentosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )


def seleccionFormDocumentos(pmodelo,pid,post,files):
    if pmodelo=='terceros_id':
        cabecera= Terceros.objects.get(pk=pid)
        return TercerosDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo =='personal_id':
        cabecera = Personal.objects.get(pk=pid)
        return PersonalDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo =='zonas_id':
        cabecera= Zonas.objects.get(pk=pid)
        return ZonasDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo =='catequipos_id':
        cabecera=CatalogoEquipos.objects.get(pk=pid)
        return CatEquiposDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo =='consumibles_id':
        cabecera= Consumibles.objects.get(pk=pid)
        return ConsumiblesDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")




@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def DocumentosCrearView(request,pmodelo,pid):
    template_name = "base/modal_formset.html"
    auxiliar   = {"etiqueta" : "Adjuntar Documento"}
    form_detail  = seleccionFormDocumentos(pmodelo,pid,request.POST,request.FILES)
    if form_detail.is_valid():
        guarda =form_detail.save()
        messages.add_message(request, messages.SUCCESS, _("Documentos creado con Exito"))
        return redirect(reverse('mdocumentos_list', args=(pmodelo,pid,) ))
    else:
        messages.add_message(request, messages.ERROR, form_detail.errors)


    return render_to_response(template_name, {'form_detail' : form_detail, 'auxiliar': auxiliar },context_instance=RequestContext(request))


class  DocumentosElimina(DocumentosMixin):
    def get_success_url(self):
        parametros = idModelomaestros(self.object)
        return reverse('m%s_list' % self.modulo,args=(parametros['modelo'],parametros['id'],))

DocumentosEliminarView  = type(genericaview,(DocumentosElimina,DeleteView,), eliminar_template )


@login_required(login_url='/')
def DocumentosActualizarView(request,pk):
    template_name = "base/modal_formset.html"
    auxiliar   = {"etiqueta" : "Editar Documentos"}
    #parametros   = idModelomaestros(Documentos.objects.get(pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user)))
    parametros   = idModelomaestros(Documentos.objects.get(pk=pk))
    form_detail  = seleccionFormDocumentos(parametros['modelo'],parametros['id'],request.POST,request.FILES)
    if form_detail.is_valid():
        guarda =form_detail.save()
        messages.add_message(request, messages.SUCCESS, _("Documentos actualizado con Exito"))
        return redirect(reverse('mdocumentos_list', args=(parametros['modelo'],parametros['id'],)))
    else:
        messages.add_message(request, messages.ERROR, form_detail.errors)


    return render_to_response(template_name, {'form_detail' : form_detail, 'auxiliar': auxiliar },context_instance=RequestContext(request))


