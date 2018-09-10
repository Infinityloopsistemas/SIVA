# -*- coding: utf-8 -*-
# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.context_processors import request
from django.core.urlresolvers import reverse
from django.db.models import ProtectedError
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext, Context
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from pyjasperclient import JasperClient
from appcc.forms import  *
from appcc.models import *
from reportes.models import Informes
from siva.utils import *
from imagen.forms import ImagenReportForms


CREADO =_("creado")
ACTUA  =_("actualizado")


class ViewBase(object):
    extra_context={}
    model      =None
    form_class =None
    def __init__(self,modulo,etiqueta,tabla,form):
        self.modulo= modulo
        self.acciones   = { "crear" : "/appcc/%s/crear" % modulo, "eliminar": "/appcc/%s/eliminar" % modulo, 'ira':"" }
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
        self.object = form.save(commit=False,user=self.request.user)
        self.object.save(user=self.request.user)
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

# ----------------------------------------------Definicion Panel Principal ------------------------------------------------------------------
@login_required(login_url='/')
def appcc(request):
    #objeto = ContentType.objects.filter(app_label='maestros', user=request.user);
    #Construimos el diccionario
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    #request.breadcrumbs(_("APPCC"),request.path_info)
    lista_objeto = {'titulobox' : _("Gestion del APPCC"), "contenido" : [
        {"apartado" :"APPCC" ,
         "botones" :[
             #{ "href":"/appcc/appcc/lista", "titulo" : "APPCC", "icon1" : "" , "icon2" : "" } ,
             { "href":"/appcc/appcc", "titulo" : "APPCC", "icon1" : "" , "icon2" : "" } ,
             #                            { "href":"/appcc/manualautocontrol/lista", "titulo" : "Manual de Auto Control", "icon1" : "icofont-chevron-up" , "icon2" : "icon-adjust" },
             #                            { "href":"/appcc/planautocontrol/lista", "titulo" : "Plan de Auto Control", "icon1" : "icofont-chevron-up" , "icon2" : "icon-adjust" },
         ]
        },

        ],}


    return render_to_response("base/panel.html",{"lista_objeto" : lista_objeto },context_instance=RequestContext(request) )




#--------------------------------------------------- APPCC -----------------------------------------------------------------------------------#

lista_template    =  {'template_name' : "appcc/list_appcc.html",}

class APPCCMixin(ViewBase,BreadcrumbTemplateMixin):
    
    def __init__(self):
        super(APPCCMixin,self).__init__("appcc",_("APPCC"),"APPCC","APPCCForms")
        #self.acciones['ira']='/appcc/manualautocontrol/lista' #Sobrescribimos para pasar el id de APPC para filtrar o crear un nuevo Manual de AutoControl
        self.acciones['ira']='/appcc/appcc/manualautocontrol' #Sobrescribimos para pasar el id de APPC para filtrar o crear un nuevo Manual de AutoControl
        self.acciones['iradoc']='appcc/documentos/lista/appcc_id/'
        #self.acciones['ira1']='/appcc/auditorias/lista'
        self.acciones['ira1']='/appcc/appcc/auditorias'
        self.cabezera.append(_(u'Auditorias'))
        self.cabezera.append(_(u'Manual AutoControl'))
        self.cabezera.append(_(u'Cuadro Gestion'))
        self.cabezera.append(_(u'Incidencias'))
        self.cabezera.append(_(u'Ver'))
        self.cabezera.append(_(u'Impresion'))
        self.cabezera.append(_(u"Acciones"))
    def get_queryset(self):
        return APPCC.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=self.request.user))

baselista          = "APPCCMixin"
AppccListaView     = type(genericaview,(eval(baselista),ListView,),   lista_template )
AppccDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  ) # ¿Donde se usa esto?

@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def AppccCrearView(request):

    
    #request.breadcrumbs(_("Nuevo"),request.path_info)
    request.breadcrumbs(generarBreadCrumb(request.path_info))

    template_name = "base/formset.html"
    auxiliar   = {"etiqueta" : "Crear APPCC",}
    form        = APPCCForms(request.POST or None)
    form_detail = HistorialRevisionesFormset(request.POST or None, prefix="dappcc")
    if form.is_valid():
        padre       = form.save(commit=False,request=request)
        form_detail = HistorialRevisionesFormset( request.POST or None, instance = padre, prefix="dappcc")
        if form_detail.is_valid():
            padre.save(user=request.user)
            form_detail.save()
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %("APPCC",CREADO) )
            return redirect(reverse('appcc_list'))
        else:
            messages.add_message(request, messages.ERROR,  form_detail.errors)
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail, 'auxiliar' : auxiliar },context_instance=RequestContext(request))


AppccEliminarView  = type(genericaview,(eval(baselista),DeleteView,), eliminar_template  )


@login_required(login_url='/')
def AppccActualizarView(request,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/formset.html"
    auxiliar   = {"etiqueta" : "Editar APPCC"}
    cabecera =   get_object_or_404(APPCC, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form           = APPCCForms( request.POST or None,instance= cabecera)
    if form.is_valid():
        padre       = form.save(commit=False, request=request)
        form_detail = HistorialRevisionesFormset( request.POST, instance = padre, prefix="dappcc")
        if form_detail.is_valid():
            padre.save(user=request.user)
            form_detail.save()
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %("APPCC",ACTUA ))
            return redirect(reverse('appcc_list'))
        else:
            messages.add_message(request, messages.ERROR,  form_detail.errors)
    else:
        messages.add_message(request, messages.ERROR,  form.errors)

    form_detail = HistorialRevisionesFormset( instance= cabecera, prefix="dappcc")
    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail, 'auxiliar' : auxiliar },context_instance=RequestContext(request))


#---------------------------------------Manual Auto Control -------------------------------------------------------------------------------------#

class ManualAutoControlMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(ManualAutoControlMixin,self).__init__("manualautocontrol",_("Manual de Auto Control"),"ManualAutoControl","ManualAutoControlForms")
        #self.acciones['ira']='/appcc/planautocontrol/lista' #Sobrescribimos para pasar el id de APPC para filtrar o crear un nuevo Manual de AutoControl
        #print self.modulo
        #self.acciones['crear']='/appcc/appcc/manualautocontrol/80/crear' hay que mirar esto
        #self.acciones['ira1']='/appcc/cabregistros/lista'
        self.cabezera.append('Ir a Plan')
        self.cabezera.append("Ir a Registro")
        self.cabezera.append("Ver")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

baselista      ="ManualAutoControlMixin"

class ManualautocontrolListaView(ManualAutoControlMixin,ListView):
    template_name = "appcc/list_manualautocontrol.html"

    def get_queryset(self): #filtramos el id del appc mostramos solo sus hijos
        id = self.kwargs['pappccid']
        self.acciones["appccid"] = id
        return ManualAutoControl.objects.filter(appcc = id, empresa__in=Empresas.objects.filter(usuario=self.request.user))


ManualautocontrolDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )


@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def ManualautocontrolCrearView(request,pappccid):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/form.html"
    auxiliar   = {"etiqueta" : "Crear Manual Auto Control"}
    form           = ManualAutoControlForms(request.POST or None)
    form.appcc_id = pappccid
    if form.is_valid():
        padre          = form.save(commit=False,request=request)
        padre.appcc_id = pappccid
        padre.save(user=request.user)
        messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Manual Autocontrol"),CREADO) )
        return redirect(reverse('manualautocontrol_list', args=(pappccid,) ))
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))


class  ManualAutoElimina(ManualAutoControlMixin):
    def get_success_url(self):
        return reverse('%s_list' % self.modulo,args=(self.object.appcc_id,))

ManualautocontrolEliminarView  = type(genericaview,(ManualAutoElimina,DeleteView,), eliminar_template )


@login_required(login_url='/')
def ManualautocontrolActualizarView(request,pappccid,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/form.html"
    auxiliar   = {"etiqueta" : "Editar Plan Auto Control"}
    cabecera =   get_object_or_404(ManualAutoControl, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form           = ManualAutoControlForms(request.POST or None, instance=cabecera)
    if form.is_valid():
        padre           = form.save(commit=False,request=request)
        padre.save(user=request.user)
        messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Manual Acutocontrol"),ACTUA) )
        return redirect(reverse('manualautocontrol_list', args=(padre.appcc_id,) ))
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))



#-------------------------------------Plan Auto Control ---------------------------------------------------------------------------------------------

class PlanAutoControlMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        print 'model0'
        
        super(PlanAutoControlMixin,self).__init__("planautocontrol",_("Plan de auto Control"),"PlanAutoControl","PlanAutoControlForms")
        self.cabezera.append("Ver")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

baselista   ="PlanAutoControlMixin"



class PlanautocontrolListaView(PlanAutoControlMixin,ListView):
    template_name = "appcc/list_planautocontrol.html"
    print 'model1'
    def get_queryset(self): #filtramos el id del appc mostramos solo sus hijos
        id = self.kwargs['pmanuctrid']
        manual = ManualAutoControl.objects.filter(pk=id)
        self.auxiliar['padre']= manual.first().tpplancontrol.denominacion
        self.acciones['manautctrlid']=id   #Guardamos para añadir en la creacion button
        self.acciones["appccid"] = self.kwargs['pappccid']
        return PlanAutoControl.objects.filter( manautctrl = id,empresa__in=Empresas.objects.filter(usuario=self.request.user))


PlanautocontrolDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )

@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def PlanautocontrolCrearView(request,pappccid,pmanuctrid):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "appcc/planautocontrol.html"
    auxiliar   = {"etiqueta" : "Crear Plan Auto Control"}
    objmanu    = get_object_or_404(ManualAutoControl,pk=pmanuctrid,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    etiq       = ( "" if objmanu.etiquetasTemplate() is None else objmanu.etiquetasTemplate())
    if len(etiq) !=0:
        etiquetas = eval(etiq)
    else:
        etiquetas= None
    form           = PlanAutoControlForms(request.POST or None)
    form_detail_cd = ConsumiblesDosisFormset(request.POST or None, prefix="dcd")
    form_detail_va = ValoresAnaliticasFormset(request.POST or None, prefix="dva")
    form.manautctrl_id = pmanuctrid
    if form.is_valid():
        padre           = form.save(commit=False,request=request)
        padre.manautctrl_id = pmanuctrid
        form_detail_cd = ConsumiblesDosisFormset( request.POST or None, instance = padre, prefix="dcd")
        form_detail_va = ValoresAnaliticasFormset( request.POST or None, instance = padre, prefix="dva")
        if form_detail_cd.is_valid() and form_detail_va.is_valid():
            padre.save(user=request.user)
            form_detail_cd.save()
            form_detail_va.save()
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Plan Acutocontrol"),CREADO) )
            #return redirect(reverse('planautocontrol_list', args=(pmanuctrid,) ))
            return redirect(reverse('planautocontrol_list', args=(pappccid,pmanuctrid,) ))
        else:
            messages.add_message(request, messages.ERROR,  form_detail_cd.errors)
            messages.add_message(request, messages.ERROR,  form_detail_va.errors)

    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'form_detail_cd' : form_detail_cd, 'form_detail_va' : form_detail_va, 'auxiliar': auxiliar, 'etiquetas' : etiquetas },context_instance=RequestContext(request))


class  PlanAutoElimina(PlanAutoControlMixin):
    def get_success_url(self):
        #return reverse('%s_list' % self.modulo,args=(self.object.manautctrl_id,))
        return reverse('%s_list' % self.modulo,args=(self.object.manautctrl.appcc.id,self.object.manautctrl_id,))

PlanautocontrolEliminarView  = type(genericaview,(PlanAutoElimina,DeleteView,), eliminar_template  )


@login_required(login_url='/')
def PlanautocontrolActualizarView(request,pappccid,pmanuctrid,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "appcc/planautocontrol.html"
    auxiliar   = {"etiqueta" : "Editar Plan Auto Control"}
    cabecera   =   get_object_or_404(PlanAutoControl, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    etiq       = ( "" if  cabecera.manautctrl.etiquetasTemplate() is None else cabecera.manautctrl.etiquetasTemplate())
    if len(etiq) !=0:
        etiquetas = eval(etiq)
    else:
        etiquetas= None
    form           = PlanAutoControlForms(request.POST or None,instance= cabecera)
    form_detail_cd = ConsumiblesDosisFormset(request.POST or None, instance=cabecera, prefix="dcd")
    form_detail_va = ValoresAnaliticasFormset(request.POST or None,instance=cabecera, prefix="dva")
    if form.is_valid():
        padre       = form.save(commit=False,request=request)
        pmanuctrid  = get_object_or_404(ManualAutoControl,pk=pmanuctrid)

        form_detail_cd = ConsumiblesDosisFormset( request.POST or None, instance= pmanuctrid, prefix="dcd")
        form_detail_va = ValoresAnaliticasFormset( request.POST or None, instance = pmanuctrid, prefix="dva")
        if form_detail_cd.is_valid() and form_detail_va.is_valid():
            padre.save(user=request.user)
            form_detail_cd.save()
            form_detail_va.save()
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Plan Acutocontrol"),ACTUA) )
            return redirect(reverse('planautocontrol_list', args=(pappccid,pmanuctrid.id,) ))
        else:
            messages.add_message(request, messages.ERROR,  form_detail_cd.errors)
            messages.add_message(request, messages.ERROR,  form_detail_va.errors)

    else:
        messages.add_message(request, messages.ERROR,  form.errors)



    return render_to_response(template_name, {'form' : form, 'form_detail_cd' : form_detail_cd, 'form_detail_va' : form_detail_va, 'auxiliar': auxiliar, 'etiquetas' : etiquetas },context_instance=RequestContext(request))



# --------------------------------------------------- Cabecera de Inicio REGISTROS -----------------------------------------------------------------

class CabRegistrosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(CabRegistrosMixin,self).__init__("cabregistros",_("Configuracion Registros"),"CabRegistros","CabRegistrosForms")
        #self.acciones['ira']='/appcc/detallesregistros/lista' #Sobrescribimos para pasar el id filtrar o crear un nuevo Manual de AutoControl
        self.cabezera.append('Fecha')
        self.cabezera.append('Analiticas')
        self.cabezera.append('Registros')
        self.cabezera.append("Ver")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

baselista      ="CabRegistrosMixin"

class CabRegistrosListaView(CabRegistrosMixin,ListView):
    template_name = "appcc/list_cabregistros.html"

    def get_queryset(self): #filtramos el id del appc mostramos solo sus hijos
        id = self.kwargs['pmanautctrid']
        manual = ManualAutoControl.objects.filter(pk=id)
        self.auxiliar['padre']= manual.first().tpplancontrol.denominacion
        self.acciones['manautctrlid']=id
        self.acciones["appccid"] = self.kwargs['pappccid']
        return CabRegistros.objects.filter(manautctrl = id,empresa__in=Empresas.objects.filter(usuario=self.request.user))


CabRegistrosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )


@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def CabRegistrosCrearView(request,pappccid,pmanautctrid):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/form.html"
    auxiliar   = {"etiqueta" : "Crear Configuración Registros"}
    form           = CabRegistrosForms(request.POST or None)
    form.appcc_id = pmanautctrid
    if form.is_valid():
        padre          = form.save(commit=False,request=request)
        padre.manautctrl_id = pmanautctrid
        padre.save(user=request.user)
        messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Definición de Registro"),CREADO) )
        return redirect(reverse('cabregistros_list', args=(pappccid,pmanautctrid,) ))
    else:
        print "Error en cabecera %s" % form.errors.as_text


    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))



class  CabregistroElimina(CabRegistrosMixin):
    def get_success_url(self):
        #return reverse('%s_list' % self.modulo,args=(self.object.manautctrl_id,))
        return reverse('%s_list' % self.modulo,args=(self.object.manautctrl.appcc.id,self.object.manautctrl_id,))

CabRegistrosEliminarView  = type(genericaview,(CabregistroElimina,DeleteView,), eliminar_template )

@login_required(login_url='/')
def CabRegistrosActualizarView(request,pappccid,pmanautctrid,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/form.html"
    auxiliar   = {"etiqueta" : "Editar Configuración Registros"}
    cabecera =   get_object_or_404(CabRegistros, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form           = CabRegistrosForms(request.POST or None, instance=cabecera)
    if form.is_valid():
        padre           = form.save(commit=False,request=request)
        padre.save(user=request.user)
        messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Definción Registro"),ACTUA) )
        #return redirect(reverse('cabregistros_list', args=(padre.manautctrl_id,) ))
        return redirect(reverse('cabregistros_list', args=(pappccid,pmanautctrid,) ))
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))

#--------------------------------------Detalles Registros -----------------------------------------------------


#class DetallesRegistrosMixin(ViewBase):
class DetallesRegistrosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(DetallesRegistrosMixin,self).__init__("detallesregistros",_("Detalle de registros"),"DetallesRegistros","DetallesRegistrosForms")
        self.cabezera.append("Ver")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")


baselista   ="DetallesRegistrosMixin"



class DetallesRegistrosListaView(DetallesRegistrosMixin,ListView):
    template_name = "appcc/list_detallesregistro.html"

    def get_queryset(self): #filtramos el id del appc mostramos solo sus hijos
        id = self.kwargs['pcabregid']
        self.acciones['cabregid']=id   #Guardamos para añadir en la creacion button
        
        
        self.acciones['manautctrlid']=self.kwargs['pmanautctrid']   #Guardamos para añadir en la creacion button
        self.acciones["appccid"] = self.kwargs['pappccid']
        return DetallesRegistros.objects.filter( cabreg_id = id,empresa__in=Empresas.objects.filter(usuario=self.request.user))


DetallesRegistrosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )

@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def DetallesRegistrosCrearView(request,pappccid,pmanautctrid,pcabregid):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "appcc/detallesregistro.html"
    auxiliar   = {"etiqueta" : "Crear Registros"}
    cabecera        = get_object_or_404(CabRegistros, pk=pcabregid,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form            = DetallesRegistrosForms(request.POST or None, idmanctrl = cabecera.manautctrl_id, iduser=request.user)
    form_detail_reg = RegistrosFormset(request.POST or None, prefix="registro")
    if cabecera.frecuencia.nounidades <= 24:
        form.helper.layout = Layout( Fieldset(
                Div('id',css_class="control-group hidden"),
                Div('cabreg_id',css_class="control-group hidden"),
                Div( Div(Field('actividades'), css_class=s6 ),Div(Field('fechaalta',template=fecha,css_class=small),css_class=s6) ,css_class=s12 ),
                    Div( Div('tplimitcrit', css_class=s4),Div('valanali',css_class=s4 ),Div(Field('ordagenda',css_class=mini),css_class=s4 ),css_class=s12 ),
                Div(Div(Field('equipos',css_class=xlarge),css_class=s3) , Div(Field('zonas',css_class=xlarge),css_class=s3) ,Div(Field('diaejecuta'),css_class=s3 ),Div(Field('tpturnos',css_class=small),css_class=s3),css_class=s12),))
    form.cabreg_id = pcabregid
    if form.is_valid():
        padre           = form.save(commit=False,request=request)
        padre.cabreg_id = pcabregid
        form_detail_reg = RegistrosFormset( request.POST or None, instance = padre, prefix="registro")
        if form_detail_reg.is_valid():
            nunidades = cabecera.frecuencia.nounidades
            if nunidades<168 and padre.diaejecuta is not None:
                messages.add_message(request, messages.ERROR, _("Error dia ejecución, frecuencia incorrecta"))
            elif padre.actividades.agenda == True and (padre.zonas_id is None or padre.equipos is None ):
                if padre.zonas_id is None:
                    messages.add_message(request, messages.ERROR, _("Zona requerida, actividad en agenda"))
                if padre.equipos is None:
                    messages.add_message(request, messages.ERROR, _("Equipo requerido, actividad en agenda"))
            else:
                padre.save(user=request.user)
                form_detail_reg.save()
                messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Detalle de Registro"),CREADO) )
                #return redirect(reverse('detallesregistros_list', args=(pcabregid,) ))
                return redirect(reverse('detallesregistros_list', args=(pappccid,pmanautctrid,pcabregid,) ))
        else:
            messages.add_message(request, messages.ERROR,  form_detail_reg.errors)
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail_reg,  'auxiliar': auxiliar },context_instance=RequestContext(request))


class  DRegistroElimina(DetallesRegistrosMixin):
    def get_success_url(self):
        #return reverse('%s_list' % self.modulo,args=(self.object.cabreg_id,))
        return reverse('%s_list' % self.modulo,args=(self.object.cabreg.manautctrl.appcc.id,self.object.cabreg.manautctrl.id,self.object.cabreg_id,))

DetallesRegistrosEliminarView  = type(genericaview,(DRegistroElimina,DeleteView,), eliminar_template  )


@login_required(login_url='/')
def DetallesRegistrosActualizarView(request,pappccid,pmanautctrid,pcabregid,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name   = "appcc/detallesregistro.html"
    auxiliar        = {"etiqueta" : "Editar Registros"}
    cabecera        =   get_object_or_404(DetallesRegistros, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form            = DetallesRegistrosForms( request.POST or None,instance= cabecera, idmanctrl = cabecera.cabreg.manautctrl_id, iduser=request.user)
    form_detail_reg = RegistrosFormset(request.POST or None, instance=cabecera, prefix="registro")
    if cabecera.cabreg.frecuencia.nounidades <= 24:
        form.helper.layout = Layout( Fieldset(
                Div('id',css_class="control-group hidden"),
                Div('cabreg_id',css_class="control-group hidden"),
                Div( Div(Field('actividades'), css_class=s4 ),Div(Field('fechaalta',template=fecha,css_class=small),css_class=s4),Div(Field('tracksondas'),css_class=s4) ,css_class=s12 ),
                    Div( Div('tplimitcrit', css_class=s4),Div('valanali',css_class=s4 ),Div(Field('ordagenda',css_class=mini),css_class=s4 ),css_class=s12 ),
                Div(Div(Field('equipos',css_class=xlarge),css_class=s3) , Div(Field('zonas',css_class=xlarge),css_class=s3) ,Div(Field('diaejecuta'),css_class=s3),Div(Field('tpturnos'),css_class=s3), css_class=s12),))
    if form.is_valid():
        padre       = form.save(commit=False,request=request)
        pcabregid   = padre.cabreg_id
        form_detail_reg = RegistrosFormset( request.POST or None, instance = padre, prefix="registro")
        if form_detail_reg.is_valid():
            nunidades = cabecera.cabreg.frecuencia.nounidades
            if nunidades<168 and padre.diaejecuta is None:
                messages.add_message(request, messages.ERROR, _("Error dia ejecución, frecuencia incorrecta"))
            elif padre.actividades.agenda ==True and (padre.zonas_id is None or padre.equipos is None ):
                if padre.zonas_id is None:
                    messages.add_message(request, messages.ERROR, _("Zona requerida, actividad en agenda"))
                if padre.equipos is None:
                    messages.add_message(request, messages.ERROR, _("Equipo requeridd, actividad en agenda"))
            else:
                padre.save(user=request.user)
                form_detail_reg.save()
                messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Detalle de Registro"),ACTUA) )
                #return redirect(reverse('detallesregistros_list', args=(pcabregid,)))
                return redirect(reverse('detallesregistros_list', args=(pappccid,pmanautctrid,pcabregid,)))
        else:
            messages.add_message(request, messages.ERROR,  form_detail_reg.errors)
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail_reg, 'auxiliar': auxiliar },context_instance=RequestContext(request))

#---------------------------------------------------- INFORMES TECNICOS -------------------------------------------------------------------------------------------------#


#class CabInfTecnicosMixin(ViewBase):
class CabInfTecnicosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(CabInfTecnicosMixin,self).__init__("auditorias",_("Cabecera de Informes"),"CabInformesTecnicos","CabInfTecnicosForms")
        self.cabezera.append("Ver")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")


baselista   ="CabInfTecnicosMixin"



class CabInfTecnicosListaView(CabInfTecnicosMixin,ListView):
    template_name = "appcc/list_cabinftecnicol.html"

    def get_queryset(self): #filtramos el id del appc mostramos solo sus hijos
        id = self.kwargs['pappccid']
        self.acciones["appccid"] = id
        return CabInformesTecnicos.objects.filter(appcc = id, empresa__in=Empresas.objects.filter(usuario=self.request.user))


CabInfTecnicosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )

@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def CabInfTecnicosCrearView(request,pappccid):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    print request.FILES
    template_name      = "appcc/detinformestecnicos.html"
    auxiliar           = {"etiqueta" : "Crear Informe"}
    form               = CabInfTecnicosForms(request.POST or None)
    form_detail_inftec = DetInfTecnicosFormset(request.POST or None, prefix="detinftec")
    print form
    #form_imagen = ImagenReportForms(request.FILES or None)
    if form.is_valid():
        padre           = form.save(commit=False)
        padre.appcc_id  = pappccid
        form_detail_inftec = DetInfTecnicosFormset( request.POST or None, instance = padre, prefix="detinftec")
        if form_detail_inftec.is_valid():
            padre.save(user=request.user)
            details = form_detail_inftec.save(commit=False)
            iter1 = 0
            for detail in details:
                iter2 = 0
                detail.save()
                for fichero in request.FILES:                    
                    if iter1 == iter2:
                        #ct = ContentType.objects.get(model=detail.__class__.__name__.lower())
                        ct = get_object_or_404(ContentType,model=detail.__class__.__name__.lower())
                        detail.imagen.create(denominacion=request.FILES[fichero].name,file=request.FILES[fichero].read(),content_type_file=request.FILES[fichero].content_type,object_id=detail.pk,content_type=ct.pk)
                    iter2 = iter2 + 1
                iter1 = iter1 + 1
                
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Informe Tecnico"),CREADO) )
            return redirect(reverse('cabinftecnicos_list', args=(pappccid,) ))
        else:
            messages.add_message(request, messages.ERROR, form_detail_inftec.errors)
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail_inftec,  'auxiliar': auxiliar },context_instance=RequestContext(request))


class  CabInfTecnicosElimina(CabInfTecnicosMixin):
    def get_success_url(self):
        return reverse('cabinftecnicos_list', args=(self.object.appcc_id,))

CabInfTecnicosEliminarView  = type(genericaview,(CabInfTecnicosElimina,DeleteView,), eliminar_template  )


@login_required(login_url='/')
#def CabInfTecnicosActualizarView(request,pk):
def CabInfTecnicosActualizarView(request,pappccid,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name   = "appcc/detinformestecnicos.html"
    auxiliar        = {"etiqueta" : "Editar Informe"}
    cabecera        = get_object_or_404(CabInformesTecnicos, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form            = CabInfTecnicosForms( request.POST or None,instance= cabecera)
    form_detail_inftec = DetInfTecnicosFormset(request.POST or None, instance=cabecera,prefix="detinftec")
    if form.is_valid():
        padre              = form.save(commit=False)
        pappcc_id          = padre.appcc_id
        form_detail_inftec = DetInfTecnicosFormset( request.POST or None, instance = padre, prefix="detinftec")
        if form_detail_inftec.is_valid():
#                 padre.save(user=request.user)
#                 form_detail_inftec.save()

            padre.save(user=request.user)

            details = form_detail_inftec.save()
            iter1 = 0
            for detail in details:
                iter2 = 0
                detail.save()
                for fichero in request.FILES:                    
                    if iter1 == iter2:                        
                        #ct = ContentType.objects.get(model=detail.__class__.__name__.lower())
                        ct = get_object_or_404(ContentType,model=detail.__class__.__name__.lower())
                        try:                            
                            imagen = Imagen.objects.get(content_type=ct,object_id=detail.pk)
                            #detail.imagen.update_or_create(pk=imagen.pk,denominacion=request.FILES[fichero].name,file=request.FILES[fichero].read(),content_type_file=request.FILES[fichero].content_type,object_id=detail.pk,content_type=ct.pk)
                            imagen.file = request.FILES[fichero].read()
                            imagen.content_type_file=request.FILES[fichero].content_type
                            imagen.save()
                        except Imagen.DoesNotExist:   
                        # Se accede a las imagenes del detail y se cambia
                            detail.imagen.create(denominacion=request.FILES[fichero].name,file=request.FILES[fichero].read(),content_type_file=request.FILES[fichero].content_type,object_id=detail.pk,content_type=ct.pk)
                    iter2 = iter2 + 1
                iter1 = iter1 + 1
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Informe Tecnico"),ACTUA) )
            return redirect(reverse('cabinftecnicos_list', args=(pappcc_id,)))
        else:
            messages.add_message(request, messages.ERROR,  form_detail_inftec.errors)
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail_inftec, 'auxiliar': auxiliar },context_instance=RequestContext(request))




#------------------------------------------ANALITICAS ----------------------------------------------#

#class CabAnaliticasMixin(ViewBase):
class CabAnaliticasMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(CabAnaliticasMixin,self).__init__("cabanaliticas",_("Analiticas"),"CabAnaliticas","CabAnaliticasForms")
        self.cabezera.append("Ver")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")


baselista   ="CabAnaliticasMixin"



class CabAnaliticasListaView(CabAnaliticasMixin,ListView):
    template_name = "appcc/list_cabanaliticas.html"

    def get_queryset(self): #filtramos el id del appc mostramos solo sus hijos
        id = self.kwargs['pcabregid']
        self.acciones['cabregid']=id   #Guardamos para añadir en la creacion button
        
        self.acciones['manautctrlid']=self.kwargs['pmanautctrid']   #Guardamos para añadir en la creacion button
        self.acciones["appccid"] = self.kwargs['pappccid']
        return CabAnaliticas.objects.filter( cabreg_id = id,empresa__in=Empresas.objects.filter(usuario=self.request.user)).order_by('-fecha')

CabAnaliticasDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template  )

@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def CabAnaliticasCrearView(request,pappccid,pmanautctrid,pcabregid):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "appcc/detallesanaliticas.html"
    auxiliar   = {"etiqueta" : _("Crear Analitica")}
    form            = CabAnaliticasForms(request.POST or None)
    form_detail_reg = DetAnaliticasFormset(request.POST or None, prefix="detanaliticas")
    form.cabreg_id = pcabregid
    if form.is_valid():
        padre           = form.save(commit=False,request=request)
        padre.cabreg_id = pcabregid
        form_detail_reg = DetAnaliticasFormset( request.POST or None, instance = padre, prefix="detanaliticas")
        if form_detail_reg.is_valid():
            padre.save(user=request.user)
            form_detail_reg.save()
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Analitica"),CREADO) )
            #return redirect(reverse('cabanaliticas_list', args=(pcabregid,) ))
            return redirect(reverse('cabanaliticas_list', args=(pappccid,pmanautctrid,pcabregid,) ))
        else:

            messages.add_message(request, messages.ERROR,  form_detail_reg.errors)
    else:

        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail_reg,  'auxiliar': auxiliar },context_instance=RequestContext(request))


class  CabAnaliticasElimina(DetallesRegistrosMixin):
    def get_success_url(self):
        #return reverse('%s_list' % self.modulo,args=(self.object.cabreg_id,))
        return reverse('%s_list' % self.modulo,args=(self.object.cabreg.manautctrl.appcc.id,self.object.cabreg.manautctrl.id,self.object.cabreg_id,))

CabAnaliticasEliminarView  = type(genericaview,(CabAnaliticasElimina,DeleteView,), eliminar_template  )


@login_required(login_url='/')
def CabAnaliticasActualizarView(request,pappccid,pmanautctrid,pcabregid,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "appcc/detallesanaliticas.html"
    auxiliar        = {"etiqueta" : _("Editar Analiticas")}
    cabecera        =   get_object_or_404(CabAnaliticas, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form            = CabAnaliticasForms( request.POST or None,instance= cabecera)
    form_detail_reg = DetAnaliticasFormset(request.POST or None, instance=cabecera, prefix="detanaliticas")
    if form.is_valid():
        padre       = form.save(commit=False,request=request)
        pcabregid   = padre.cabreg_id
        form_detail_reg = DetAnaliticasFormset( request.POST or None, instance = padre, prefix="detanaliticas")
        if form_detail_reg.is_valid():
           padre.save(user=request.user)
           form_detail_reg.save()
           messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Analiticas"),ACTUA) )
           #return redirect(reverse('cabanaliticas_list', args=(pcabregid,)))
           return redirect(reverse('cabanaliticas_list', args=(pappccid,pmanautctrid,pcabregid,) ))
        else:

            messages.add_message(request, messages.ERROR,  form_detail_reg.errors)
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'form_detail' : form_detail_reg, 'auxiliar': auxiliar },context_instance=RequestContext(request))





#------------------------------------------Documentos ----------------------------------------------#

def idModeloappcc(modelo=None):
    if modelo.appcc_id is not None:
        #return {'modelo' : 'appcc_id', 'id': modelo.appcc_id, 'cabecera': APPCC.objects.get(pk=modelo.appcc_id), 'url': 'appcc/'}
        return {'modelo' : 'appcc_id', 'id': modelo.appcc_id, 'cabecera': get_object_or_404(APPCC,pk=modelo.appcc_id), 'url': 'appcc/'}
    if modelo.manautctrl_id is not None:
        #return {'modelo' : 'manautctrl_id' , 'id': modelo.manautctrl_id, 'cabecera' :ManualAutoControl.objects.get(pk=modelo.manautctrl_id),
        return {'modelo' : 'manautctrl_id' , 'id': modelo.manautctrl_id, 'cabecera' : get_object_or_404(ManualAutoControl,pk=modelo.manautctrl_id),
                'url': 'appcc/manualautocontrol/%s' % modelo.manautctrl.appcc.id}
    if modelo.planautoctrl_id is not None:
        #return { 'modelo' : 'planautoctrl_id' , 'id': modelo.planautoctrl_id, 'cabecera' : PlanAutoControl.objects.get(pk=modelo.planautoctrl_id),
        return { 'modelo' : 'planautoctrl_id' , 'id': modelo.planautoctrl_id, 'cabecera' : get_object_or_404(PlanAutoControl,pk=modelo.planautoctrl_id),
                'url': 'appcc/manualautocontrol/%s/planautocontrol/%s' % (modelo.planautoctrl.manautctrl.appcc.id,modelo.planautoctrl.manautctrl.id)}
    if modelo.cabreg_id is not None:
        #return {'modelo' : 'cabreg_id' , 'id': modelo.cabreg_id ,'cabecera' : CabRegistros.objects.get(pk=modelo.cabreg_id),
        return {'modelo' : 'cabreg_id' , 'id': modelo.cabreg_id ,'cabecera' : get_object_or_404(CabRegistros,pk=modelo.cabreg_id),
                'url': 'appcc/manualautocontrol/%s/cabregistros/%s' % (modelo.cabreg.manautctrl.appcc.id,modelo.cabreg.manautctrl.id)}
    if modelo.detreg_id is not None:
        #return {'modelo': 'detreg_id', 'id' :modelo.detreg_id, 'cabecera' : DetallesRegistros.objects.get(pk= modelo.detreg_id),
        return {'modelo': 'detreg_id', 'id' :modelo.detreg_id, 'cabecera' : get_object_or_404(DetallesRegistros,pk= modelo.detreg_id),
                'url': 'appcc/manualautocontrol/%s/cabregistros/%s/detallesregistros/%s' % (modelo.detreg.cabreg.manautctrl.appcc.id,modelo.detreg.cabreg.manautctrl.id,modelo.detreg.cabreg.id)}
    if modelo.cabanali_id is not None:
        #return {'modelo': 'cabanali_id', 'id':modelo.cabanali_id ,' cabecera' : CabAnaliticas.objects.get(pk=modelo.cabanali_id),
        return {'modelo': 'cabanali_id', 'id':modelo.cabanali_id ,' cabecera' : get_object_or_404(CabAnaliticas,pk=modelo.cabanali_id),
                'url': 'appcc/manualautocontrol/%s/cabregistros/%s/detallesregistros/%s' % (modelo.cabanali.cabreg.manautctrl.appcc.id,modelo.cabanali.cabreg.manautctrl.id,modelo.cabanali.cabreg.id)}
    ############### NO ENTIENDO##################
    if modelo.registros_id is not None:
        #return {'modelo': 'registros_id', 'id':modelo.registros_id ,' cabecera' : Registros.objects.get(pk=modelo.registros_id)}
        return {'modelo': 'registros_id', 'id':modelo.registros_id ,' cabecera' : get_object_or_404(Registros,pk=modelo.registros_id)}
    
    
    if modelo.cuadgest_id is not None:
        return {'modelo': 'cuadgest_id', 'id':modelo.cuadgest_id ,' cabecera' : get_object_or_404(CuadrosGestion,pk=modelo.cuadgest_id),
                'url': 'appcc/cuadrosgestion/%s' % modelo.cuadgest.appcc.id}
    if modelo.relentes_id is not None:
        if modelo.relentes.manautctrl.tpplancontrol.campoprimario == "RELACION_FORMACION":            
            rel = "relacionespersonal"            
        else:
            rel = "relacionesterceros"
        #return {'modelo': 'relentes_id', 'id':modelo.relentes_id ,' cabecera' : RelacionesEntes.objects.get(pk=modelo.relentes_id),
        return {'modelo': 'relentes_id', 'id':modelo.relentes_id ,' cabecera' : get_object_or_404(RelacionesEntes,pk=modelo.relentes_id),
                'url': 'appcc/manualautocontrol/%s/%s/%s' % (modelo.relentes.manautctrl.appcc.id,rel,modelo.relentes.manautctrl.id)}
    if modelo.gestincid_id is not None:
        #return {'modelo': 'gestincid_id', 'id':modelo.gestincid_id ,' cabecera' : GestorIncidencias.objects.get(pk=modelo.gestincid_id),
        return {'modelo': 'gestincid_id', 'id':modelo.gestincid_id ,' cabecera' : get_object_or_404(GestorIncidencias,pk=modelo.gestincid_id),
                'url': 'appcc/gestorincidencias/%s' % modelo.gestincid.appcc.id}    
    if modelo.cabinftec_id is not None:
        #return {'modelo': 'cabinftec_id', 'id':modelo.cabinftec_id ,' cabecera' : CabInformesTecnicos.objects.get(pk=modelo.cabinftec_id),
        return {'modelo': 'cabinftec_id', 'id':modelo.cabinftec_id ,' cabecera' : get_object_or_404(CabInformesTecnicos,pk=modelo.cabinftec_id),
                'url': 'appcc/auditorias/%s' % modelo.cabinftec.appcc.id}


class DocumentosMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(DocumentosMixin,self).__init__("documentos",_("Documentos"),"Documentos","DocumentosForms")
        self.cabezera.append("Abrir")
        self.cabezera.append("Acciones")

baselista      ="DocumentosMixin"


class DocumentosListaView(DocumentosMixin,ListView):

    #template_name = "base/listmodal_documentos.html"
    template_name = "base/list_documentos.html"

    def get_queryset(self):
        id     = self.kwargs['pid']
        modelo = self.kwargs['pmodelo']
        self.acciones['modelo']= modelo
        self.acciones ['id']   = id
        q = { "%s" % modelo : id}
        self.acciones['urlAux'] = self.kwargs['purl']
        print self.acciones['urlAux']
        return Documentos.objects.filter(**q)


DocumentosDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )


def seleccionFormDocumentos(pmodelo,pid,post,files):
    if pmodelo=='appcc_id':
        #cabecera= APPCC.objects.get(pk=pid)
        cabecera= get_object_or_404(APPCC,pk=pid)
        return AppccDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo=='manautctrl_id':
        #cabecera = ManualAutoControl.objects.get(pk=pid)
        cabecera = get_object_or_404(ManualAutoControl,pk=pid)
        return ManualDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo=='planautoctrl_id':
        #cabecera= PlanAutoControl.objects.get(pk=pid)
        cabecera= get_object_or_404(PlanAutoControl,pk=pid)
        return PlanDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo=='cabreg_id':
        #cabecera=CabRegistros.objects.get(pk=pid)
        cabecera= get_object_or_404(CabRegistros,pk=pid)
        return CabRegDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo =='detreg_id':
        #cabecera= DetallesRegistros.objects.get(pk=pid)
        cabecera= get_object_or_404(DetallesRegistros,pk=pid)
        return DetRegDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo == 'registros_id':
       #cabecera= Registros.objects.get(pk=pid)
       cabecera= get_object_or_404(Registros,pk=pid)
       return RegistrosDocFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo == 'cuadgest_id':
        #cabecera= CuadrosGestion.objects.get(pk=pid)
        cabecera= get_object_or_404(CuadrosGestion,pk=pid)
        return CuadGestFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo == 'relentes_id':
        #cabecera= RelacionesEntes.objects.get(pk=pid)
        cabecera= get_object_or_404(RelacionesEntes,pk=pid)
        return RelEntesFormset(post or None,files  or None, instance=cabecera, prefix="documentos")
    if pmodelo == 'gestincid_id':
        #cabecera= GestorIncidencias.objects.get(pk=pid)
        cabecera= get_object_or_404(GestorIncidencias,pk=pid)
        return GestorIncidenciasFormset(post or None,files or None, instance=cabecera, prefix="documentos")
    if pmodelo == 'cabanali_id':
        #cabecera= CabAnaliticas.objects.get(pk=pid)
        cabecera= get_object_or_404(CabAnaliticas,pk=pid)
        return CabAnaliticasFormset(post or None,files or None, instance=cabecera, prefix="documentos")
    if pmodelo == 'cabinftec_id':
        #cabecera= CabInformesTecnicos.objects.get(pk=pid)
        cabecera= get_object_or_404(CabInformesTecnicos,pk=pid)
        return  CabInfTecnicosFormset(post or None,files or None, instance=cabecera, prefix="documentos")




@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
#def DocumentosCrearView(request,pmodelo,pid):
def DocumentosCrearView(request,purl,pmodelo,pid):
    #template_name = "base/modal_formset.html"
    template_name = "base/modal_formset_attach.html"
    auxiliar   = {"etiqueta" : "Adjuntar Documento"}    
    #form_detail  = seleccionFormDocumentos(pmodelo,pid,request.POST,request.FILES)
    if request.method == 'POST':
        if 'terminar' in request.POST:
            return redirect(reverse('documentos_list', args=(purl,pmodelo,pid,) ))
        else:
            form_detail = UploadForm(request.POST,request.FILES)
            print request.method
            print pmodelo
            print pid
            if form_detail.is_valid():
                #form_detail.appcc_id= pid
                if pmodelo=='appcc_id':
                    form_detail.appcc_id= pid
                    newdoc = Documentos(appcc_id= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today(),contenido="")
                if pmodelo=='manautctrl_id':
                    form_detail.manautctrl_id= pid
                    newdoc = Documentos(manautctrl_id= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today())
                    
                if pmodelo=='planautoctrl_id':
                    form_detail.planautoctrl_id= pid
                    newdoc = Documentos(planautoctrl_id= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today())
                if pmodelo=='cabreg_id':
                    form_detail.cabreg_id= pid
                    newdoc = Documentos(cabreg_id= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today())
                if pmodelo =='detreg_id':
                    form_detail.detreg_id= pid
                    newdoc = Documentos(detreg_id= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today())
                if pmodelo == 'registros_id':
                    form_detail.registros_id= pid
                    newdoc = Documentos(registros_id= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today())
                if pmodelo == 'cuadgest_id':
                    form_detail.cuadgest_id= pid
                    newdoc = Documentos(cuadgest_id= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today())
                if pmodelo == 'relentes_id':
                    form_detail.relentes_id= pid
                    newdoc = Documentos(relentes_id= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today())
                if pmodelo == 'gestincid_id':
                    form_detail.gestincid_id= pid
                    newdoc = Documentos(gestincid_id= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today())
                if pmodelo == 'cabanali_id':
                    form_detail.cabanali_id= pid
                    newdoc = Documentos(cabanali_id= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today())
                if pmodelo == 'cabinftec_id':
                    form_detail.cabinftec_id= pid
                    newdoc = Documentos(cabinftec_id= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today())
                #form_detail.pmodelo= pid
                #print form_detail
                #newdoc = Documentos(appcc_id= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today())
                #newdoc = Documentos(pmodelo= pid,denominacion = request.FILES['file'].name,archivos = request.FILES['file'],fecha=datetime.date.today())
                newdoc.save(form_detail)
                #documento = Documentos
                messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Documento"),CREADO) )
                #return redirect(reverse('documentos_list', args=(pmodelo,pid,) ))
            else:
                messages.add_message(request, messages.ERROR,  form_detail.errors)
    else:
        form_detail = UploadForm()       

    return render_to_response(template_name, {'form_detail' : form_detail, 'auxiliar': auxiliar },context_instance=RequestContext(request))


class  DocumentosElimina(DocumentosMixin):
    def get_success_url(self):
        parametros = idModeloappcc(self.object)
        #return reverse('%s_list' % self.modulo,args=(parametros['modelo'],parametros['id'],))
        return reverse('%s_list' % self.modulo,args=(parametros['url'],parametros['modelo'],parametros['id'],))

DocumentosEliminarView  = type(genericaview,(DocumentosElimina,DeleteView,), eliminar_template )


@login_required(login_url='/')
def DocumentosActualizarView(request,pk):
    print pk
    #template_name = "base/modal_formset.html"
    template_name = "base/edit_formDocumentos.html"
    auxiliar      = {"etiqueta" : "Editar Documentos"}
    #parametros   = idModeloappcc(Documentos.objects.get(pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user)))
    
    #parametros    = idModeloappcc(Documentos.objects.get(pk=pk))
    parametros    = idModeloappcc(get_object_or_404(Documentos,pk=pk))
    if request.method == 'POST':
        #parametros    = idModeloappcc(Documentos.objects.get(pk=pk))
        #form_detail   = seleccionFormDocumentos(parametros['modelo'],parametros['id'],request.POST,request.FILES)
        form_detail = UploadForm(request.POST,request.FILES)
        if form_detail.is_valid():
            #doc = Documentos.objects.get(id=pk)
            doc = get_object_or_404(Documentos,id=pk)
            doc.denominacion = request.POST['denominacion']
            #print request.POST['fecha']
            doc.fecha = datetime.date.today()
            if 'archivos' in request.FILES:
                doc.archivos = request.FILES['archivos']
            doc.save()
            #guarda =form_detail.save()
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Documento"),ACTUA) )
            #return redirect(reverse('documentos_list', args=(parametros['modelo'],parametros['id'],)))
            return redirect(reverse('documentos_list', args=(parametros['url'],parametros['modelo'],parametros['id'],)))
        else:
            messages.add_message(request, messages.ERROR,  form_detail.errors)
    else:
        #documento = Documentos.objects.get(id=pk)
        documento = get_object_or_404(Documentos,id=pk)
        form_detail = UploadForm(initial={'id' : documento.id,'denominacion' : documento.denominacion, 'fecha' : documento.fecha,'archivos' : documento.archivos})
    

    return render_to_response(template_name, {'form_detail' : form_detail, 'auxiliar': auxiliar },context_instance=RequestContext(request))

#-------------------------------------------------------Relaciones Personal y Terceros --------------------------------------------


#class RelacionesEntesMixin(ViewBase):
class RelacionesEntesMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(RelacionesEntesMixin,self).__init__("relaciones",_("Relaciones"),"RelacionesEntes","RelacionPersonalForms")
        self.cabezera.append(_("Documentos"))
        self.cabezera.append(_("Impresión"))
        self.cabezera.append(_("Acciones"))

baselista      ="RelacionesEntesMixin"

class RelacionesEntesListaView(RelacionesEntesMixin,ListView):

    def get_queryset(self):
        id = self.kwargs['pmanautctrid']
        self.acciones['manautctrlid']=id   #Guardamos para añadir en la creacion button
        self.acciones["appccid"] = self.kwargs['pappccid']
        self.acciones["relacion"] = self.kwargs['prelacion']
        return RelacionesEntes.objects.filter(manautctrl = id,empresa__in=Empresas.objects.filter(usuario=self.request.user))


class RelacionPersonalListaView(RelacionesEntesListaView):
    template_name = "appcc/list_relacionespersonal.html"


class RelacionTercerosListaView(RelacionesEntesListaView):
    template_name = "appcc/list_relacionesterceros.html"

RelacionesEntesDetallelView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )

@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
#def RelacionesEntesCrearView(request,pmanautctrid):
def RelacionesEntesCrearView(request,pappccid,prelacion,pmanautctrid):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/form.html"
    manual        =  get_object_or_404(ManualAutoControl, pk=pmanautctrid,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    if manual.tpplancontrol.campoprimario == "RELACION_FORMACION":
        titulo="Relación Formación"
        form  = RelacionPersonalForms(request.POST or None)
    else:
        titulo="Relación Control Proveedores"
        form   = RelacionTercerosForms(request.POST or None)

    auxiliar   = {"etiqueta" : titulo}
    form.manautctrl_id = pmanautctrid
    if form.is_valid():
        padre              = form.save(commit=False,request=request)
        padre.manautctrl_id = pmanautctrid
        padre.save(user=request.user)

        if  titulo=="Relación Formación":
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Formación"),CREADO) )
            #return redirect(reverse('relacionpersonal_list', args=(pmanautctrid,) ))
            return redirect(reverse('relacionpersonal_list', args=(pappccid,pmanautctrid,) ))
        else:
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Proveedores"),CREADO) )
            #return redirect(reverse('relacionterceros_list', args=(pmanautctrid,) ))
            return redirect(reverse('relacionterceros_list', args=(pappccid,pmanautctrid,) ))
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))



class  RelacionesEntesElimina(RelacionesEntesMixin):
    def get_success_url(self):
        #return reverse('%s_list' % self.modulo,args=(self.object.manautctrl_id,))
        
        if self.object.manautctrl.tpplancontrol.campoprimario == "RELACION_FORMACION":            
            lis = "relacionpersonal"
        else:            
            lis = "relacionterceros"
            
        return reverse('%s_list' % lis,args=(self.object.manautctrl.appcc.id,self.object.manautctrl_id,))

RelacionesEntesEliminarView  = type(genericaview,(RelacionesEntesElimina,DeleteView,), eliminar_template )

@login_required(login_url='/')
def RelacionesEntesActualizarView(request,pappccid,prelacion,pmanautctrid,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/form.html"
    
    relentes =   get_object_or_404(RelacionesEntes, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    if relentes.personal is not None:
        form   = RelacionPersonalForms(request.POST or None, instance=relentes )
        titulo="Relación Formación"
    else:
        form   = RelacionTercerosForms(request.POST or None, instance=relentes)
        titulo="Relación Control Proveedores"

    auxiliar   = {"etiqueta" : titulo}
    if form.is_valid():
        padre           = form.save(commit=False,request=request)
        padre.save(user=request.user)
        if  titulo=="Relación Formación":
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Formación"),ACTUA) )
            #return redirect(reverse('relacionpersonal_list', args=(padre.manautctrl_id,) ))
            return redirect(reverse('relacionpersonal_list', args=(pappccid,pmanautctrid,) ))
        else:
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Proveedores"),ACTUA) )
            #return redirect(reverse('relacionterceros_list', args=(padre.manautctrl_id,) ))
            return redirect(reverse('relacionterceros_list', args=(pappccid,pmanautctrid,) ))
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))


#------------------------------------------Cuadros Gestion -------------------------------------------------------------------------------------


#class CuadrosGestionMixin(ViewBase):
class CuadrosGestionMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(CuadrosGestionMixin,self).__init__("cuadrosgestion",_("Cuadro de Gestión"),"CuadrosGestion","CuadrosGestionForms")
        self.cabezera.append("Ver")
        self.cabezera.append('Impresion')
        self.cabezera.append("Acciones")

baselista      ="CuadrosGestionMixin"

class CuadrosgestionListaView(CuadrosGestionMixin,ListView):
    template_name = "appcc/list_cuadgestion.html"
    #template_name = "trazabilidad/listarbol_tiposubicaciones.html"

    def get_queryset(self): #filtramos el id del appc mostramos solo sus hijos
        id = self.kwargs['pappccid']
        self.acciones["appccid"] = id
        objetos = CuadrosGestion.objects.filter(appcc = id,empresa__in=Empresas.objects.filter(usuario=self.request.user)).order_by('orden')
        for objeto in objetos:
            if objeto.is_child_node():
                print 'es hijo'
        return CuadrosGestion.objects.filter(appcc = id,empresa__in=Empresas.objects.filter(usuario=self.request.user)).order_by('orden')


CuadrosgestionDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )


@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def CuadrosgestionCrearView(request,pappccid):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/form.html"
    auxiliar   = {"etiqueta" : "Crear Cuadros de Gestion"}
    form           = CuadrosGestionForms(request.POST or None)
    if form.is_valid():
        padre          = form.save(commit=False,request=request)
        padre.appcc_id = pappccid
        padre.save(user=request.user)
        ReordenarCuadrosGestion(usuario=request.user).reordenar()
        #Si queremos crear un hijo ---
        if 'subetapa' in request.POST:
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Item padre cuadro gestión"),CREADO) )
            return redirect(reverse('cuadrosgestion_crearhijo', args=(padre.appcc_id,padre.id,) ))
        else:
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Item cuadro gestión"),CREADO) )
            return redirect(reverse('cuadrosgestion_list', args=(pappccid,) ))
    else:
        messages.add_message(request, messages.ERROR,  form.errors)

    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))

@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def CuadrogestionHijoCrear(request,pappcid,padreid):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/form.html"
    cabecera       =  get_object_or_404(CuadrosGestion, pk=padreid,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    auxiliar   = {"etiqueta" : " viene de Etapa -> %s (%s) " % (cabecera.etapa,cabecera.peligro) }
    form           = CuadrosGestionForms(request.POST or None)
    if form.is_valid():
        padre          = form.save(commit=False,request=request)
        padre.appcc_id = pappcid
        #Verificamos si es un hijo el que graba
        #padre.parent = CuadrosGestion.objects.get(id=padreid)
        padre.parent = get_object_or_404(CuadrosGestion,id=padreid)
        padre.save(user=request.user)
        ReordenarCuadrosGestion(usuario=request.user).reordenar()
        #Si queremos crear un hijo ---
        if 'subetapa' in request.POST:
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Item hijo cuadro gestión"),CREADO) )
            return redirect(reverse('cuadrosgestion_crearhijo', args=(pappcid,padre.id,) ))
        else:
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Item hijo cuadro gestión"),CREADO) )
            return redirect(reverse('cuadrosgestion_list', args=(pappcid,) ))
    else:
        messages.add_message(request, messages.ERROR,  form.errors)

    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))


class  CuadrosgestionElimina(CuadrosGestionMixin):
    def get_success_url(self):
        ReordenarCuadrosGestion(usuario=self.request.user).reordenar()
        return reverse('%s_list' % self.modulo,args=(self.object.appcc_id,))

CuadrosgestionEliminarView  = type(genericaview,(CuadrosgestionElimina,DeleteView,), eliminar_template )


@login_required(login_url='/')
#def CuadrosgestionActualizarView(request,pk):
def CuadrosgestionActualizarView(request,pappccid,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/form.html"
    auxiliar       = {"etiqueta" : "Editar Cuadros Gestión"}
    cabecera       =  get_object_or_404(CuadrosGestion, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form           =  CuadrosGestionForms(request.POST or None, instance=cabecera)
    if form.is_valid():
        padre           = form.save(commit=False,request=request)
        padre.save(user=request.user)
        #Si queremos crear un hijo ---
        if 'subetapa' in request.POST:
            messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Item padre cuadro gestión"),ACTUA) )
            return redirect(reverse('cuadrosgestion_crearhijo', args=(padre.appcc_id,padre.id,) ))
        else:
           messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Item cuadro gestión"),ACTUA) )
           return redirect(reverse('cuadrosgestion_list', args=(padre.appcc_id,) ))
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))



########################################### GESTOR DE INCIDENCIAS ####################################################################

class GestorIncidenciasMixin(ViewBase,BreadcrumbTemplateMixin):
    def __init__(self):
        super(GestorIncidenciasMixin,self).__init__("gestorincidencias",_("Gestor de Incidencias"),"GestorIncidencias","GestorIncidenciasForms")
        self.cabezera.append(_(u"Ver"))
        self.cabezera.append(_(u"Impresion"))
        self.cabezera.append(_(u"Acciones"))

baselista      ="GestorIncidenciasMixin"

class GestorincidenciasListaView(GestorIncidenciasMixin,ListView):
    template_name = "appcc/list_gestorincidencias.html"

    def get_queryset(self): #filtramos el id del appc mostramos solo sus hijos
        id = self.kwargs['pappccid']
        self.acciones["appccid"] = id
        return GestorIncidencias.objects.filter(appcc = id,empresa__in=Empresas.objects.filter(usuario=self.request.user)).order_by('-fincidencia')


GestorincidenciasDetalleView   = type(genericaview,(eval(baselista),DetailView,), detalle_template )

@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def GestorincidenciasCrearView(request,pappccid):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/form.html"
    auxiliar   = {"etiqueta" : _(u"Crear Incidencia")}
    form           = GestorIncidenciasForms(request.POST or None)
    if form.is_valid():
        padre          = form.save(commit=False,request=request)
        padre.appcc_id = pappccid
        padre.save(user=request.user)
        messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Incidencia"),CREADO) )
        return redirect(reverse('gestorincidencias_list', args=(pappccid,) ))
    else:
        messages.add_message(request, messages.ERROR,  form.errors)

    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))


class  GestorincidenciasElimina(GestorIncidenciasMixin):
    def get_success_url(self):
        return reverse('%s_list' % self.modulo,args=(self.object.appcc_id,))

GestorincidenciasEliminarView  = type(genericaview,(GestorincidenciasElimina,DeleteView,), eliminar_template )


@login_required(login_url='/')
#def GestorincidenciasActualizarView(request,pk):
def GestorincidenciasActualizarView(request,pappccid,pk):
    request.breadcrumbs(generarBreadCrumb(request.path_info))
    template_name = "base/form.html"
    auxiliar       = {"etiqueta" : _(u"Editar Incidencias")}
    cabecera       =  get_object_or_404(GestorIncidencias, pk=pk,empresa__in=Empresas.objects.filter(usuario__username=request.user))
    form           =  GestorIncidenciasForms(request.POST or None, instance=cabecera)
    if form.is_valid():
        padre           = form.save(commit=False,request=request)
        padre.save(user=request.user)
        #Si queremos crear un hijo ---
        messages.add_message(request, messages.SUCCESS, _(" %s %s con exito") %(_("Incidencia"),ACTUA) )
        return redirect(reverse('gestorincidencias_list', args=(padre.appcc_id,) ))
    else:
        messages.add_message(request, messages.ERROR,  form.errors)


    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))



@login_required(login_url='/')
def ImprimirListaTareas(request,empresaid):
    hoy             = datetime.datetime.now().date()
    fecha           = str(hoy.year)+str(hoy.month).zfill(2)+str(hoy.day).zfill(2)
    appccid         = get_object_or_404(APPCC,empresa_id=int(empresaid)).id
    #informe         = Informes.objects.get(pk= 25 )
    informe         = get_object_or_404(Informes,pk= 25 )
    j = JasperClient(informe.url,settings.USUARIO_JASPER,settings.PASSWD_JASPER)
    ret = j.runReport(informe.nombrereport,"PDF",params={"pid": str(appccid), "pfinicio":fecha })
    return HttpResponse(ret['data'], content_type='application/pdf')

@login_required(login_url='/')
def ImprimirRegistrosEmpresas(request,empresaid):
    informe         = get_object_or_404(Informes,pk= 76 )
    j = JasperClient(informe.url,settings.USUARIO_JASPER,settings.PASSWD_JASPER)
    ret = j.runReport(informe.nombrereport,"PDF",params={"pempresaid": str(empresaid)})
    return HttpResponse(ret['data'], content_type='application/pdf')

@login_required(login_url='/')
def CuadrosGestionArbol(request,empresaid):
    arbol = JsonCuadrosGestion(empresaid)
    listarbol = arbol.generar()
    resjson = simplejson.dumps(listarbol,cls=JSONEncoder)
    return HttpResponse(resjson,content_type="application/json")




    #############################################Registros Rapidos ###################################################################

#@login_required(login_url='/')
#def RegistrosRapidosCrearView(request,pk,year,month,day):
#    template_name  = "base/modal_registros.html"
#    fechadesde     = datetime.datetime.strptime( "%s-%s-%s" %(day,month,year), '%d-%m-%Y')
#    cabecera       = get_object_or_404(DetallesRegistros, pk=pk)
#    auxiliar       = {"etiqueta" : cabecera.actividades, 'zona': cabecera.zonas, 'equipos' : cabecera.equipos }
#    form           =  RegistrosRapidosForms(request.POST or None, initial={'fechadesde': fechadesde})
#    #Ocultamos los campos a completar dependiendo del tipo de actividad
#    if cabecera.actividades.tipo == 'C':
#        form.helper['valor'].wrap(Div,css_class="control-group hidden")
#    else:
#        form.helper['estado'].wrap(Div,css_class="control-group hidden")
#    if form.is_valid():
#        padre            = form.save(commit=False)
#        padre.detreg     = cabecera
#        padre.fechahasta = padre.fechadesde
#        padre.save()
#        return redirect('/panelprincipal/')
#    else:
#        messages.add_message(request, messages.ERROR,  form.errors)
#
#
#    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))
#
#
#@login_required(login_url='/')
#def RegistrosRapidosActualizarView(request,pk,detregid):
#    template_name  = "base/modal_registros.html"
#    cabecera       = get_object_or_404(DetallesRegistros, pk=detregid)
#    detalle        = get_object_or_404(Registros, pk=pk)
#    auxiliar       = {"etiqueta" : cabecera.actividades, 'zona': cabecera.zonas, 'equipos' : cabecera.equipos }
#    form           =  RegistrosRapidosForms(request.POST or None, instance=detalle)
#    #Ocultamos los campos a completar dependiendo del tipo de actividad
#    if cabecera.actividades.tipo == 'C':
#        form.helper['valor'].wrap(Div,css_class="control-group hidden")
#    else:
#        form.helper['estado'].wrap(Div,css_class="control-group hidden")
#    if form.is_valid():
#        padre            = form.save(commit=False)
#        padre.detreg     = cabecera
#        padre.fechahasta = padre.fechadesde
#        padre.save()
#        return redirect('/panelprincipal/')
#    else:
#        messages.add_message(request, messages.ERROR,  form.errors)
#
#
#    return render_to_response(template_name, {'form' : form, 'auxiliar': auxiliar },context_instance=RequestContext(request))