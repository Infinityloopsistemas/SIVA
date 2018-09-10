# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from maestros_generales.models import Empresas
from django.core.mail import send_mail
from siva import settings
from siva.forms import ContactoForm
from siva.settings import PRODUCCION
from django.core.mail.message import EmailMessage
from maestros.models import Personal
from django.contrib import messages

__author__ = 'julian'

#@login_required(login_url='/')
@login_required(login_url='/')
def panelprincipal(request):
    template_name = "base/panel_principal.html"
    request.breadcrumbs(_("Principal"),request.path_info)
    return render_to_response(template_name,context_instance=RequestContext(request))

#@login_required(login_url='/')
@login_required(login_url='/')
def loginEmpresa(request,pk):
    usuarioname = request.user
    from django.contrib.auth import authenticate, login
    emp = get_object_or_404(Empresas,pk=pk)
    usuario  = emp.usuario.all().filter(username__contains=usuarioname)[0]
    usuario.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request,usuario)
    return HttpResponseRedirect("/panelprincipal/")

@login_required(login_url='/')
def contacto(request):
    template_name = "base/contacto.html"
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        asunto = form.cleaned_data['asunto']
        mensaje = form.cleaned_data['mensaje']
        usuario = request.user
        mes = 'Usuario : ' + usuario.username + '\n' + mensaje
        if not usuario.email:
            empresa = Empresas.objects.get(usuario=usuario)
            personals = Personal.objects.filter(empresa=empresa)
            email_personal = None
            for personal in personals:
                if personal.email and personal.email != 'josealzn@gmail.com':
                    email_personal = personal.email
                    break
            if not email_personal:
                mes_aux = 'Esta empresa no tiene e-mail de contacto'
                mes = mes_aux + '\n' + mes
                email = EmailMessage(asunto, mes, 'incidencias@givasl.com', ['incidencias@givasl.com','regcontrol@givasl.com',])
            else:
                mes_aux = 'Este usuario no tiene e-mail de contacto'
                mes = mes_aux + '\n' + mes
                email = EmailMessage(asunto, mes, 'incidencias@givasl.com', ['incidencias@givasl.com','regcontrol@givasl.com',],headers = {'Reply-To': email_personal})
                   
            
        else:
            email = EmailMessage(asunto, mes, 'incidencias@givasl.com', ['incidencias@givasl.com','regcontrol@givasl.com',],headers = {'Reply-To': usuario.email})
        try:
            email.send()
            messages.add_message(request, messages.SUCCESS, _(" Mensaje enviado con exito"))

        except Exception, a:
            print a
            messages.add_message(request, messages.ERROR,  _(" Su mensaje no ha podido ser enviado"))
    else:
        messages.add_message(request, messages.ERROR,  form.errors)
    return render_to_response(template_name,{'form':form},context_instance=RequestContext(request))

@login_required(login_url='/')
def graficas_sensores(request):
    usuario = request.user
    empid = get_object_or_404(Empresas,usuario=usuario).id
    token = get_object_or_404(Token,user=usuario).key
    return render_to_response("dojo/sensores/tempsensores.html",{'empresa': empid , 'url_server' : settings.URL_SERVER , 'token': token} ,context_instance=RequestContext(request) )


@login_required(login_url='/')
def gestion_maestros(request):
    usuario = request.user
    print usuario
    empid = get_object_or_404(Empresas,usuario=usuario).id
    token = get_object_or_404(Token,user=usuario).key
    return render_to_response("dojo/maestros/maestros.html",{'empresa': empid , 'url_server' : settings.URL_SER_REST , 'token': token} ,context_instance=RequestContext(request) )



@login_required(login_url='/')
def mapas_sensores(request):
    usuario = request.user
    print usuario
    empid = get_object_or_404(Empresas,usuario=usuario).id
    token = get_object_or_404(Token,user=usuario).key
    return render_to_response("dojo/sensores/mapsgps/mapasgps_leaf.html",{'empresa': empid , 'url_server' : settings.URL_SER_REST , 'token': token} ,context_instance=RequestContext(request) )

