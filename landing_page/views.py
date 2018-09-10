from django.shortcuts import render, render_to_response, HttpResponseRedirect
from landing_page.forms import addLandingPage
from imagen.forms import addImagenForms
from django.core.context_processors import request
from django.template import RequestContext, Context
from django.contrib.contenttypes.models import ContentType

from landing_page.models import CabLandingPage
from imagen.models import Imagen
from siva.utils import obtenerImagenes,obtenerImagen
from appcc.models import APPCC
from siva.views import loginEmpresa
from maestros_generales.models import Empresas

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from gestion_usuarios.utils import is_allowed_edit

# Create your views here.

def LandingPageView(request,url):
    template_name = "landingPage/landing_page.html"

    empresa = Empresas.objects.get(url=url)
    landingPage = CabLandingPage.objects.get(empresa_id=empresa.pk)
    ct = ContentType.objects.get(model=landingPage.get_model())
    cabecera = Imagen.objects.filter(content_type=ct,object_id=landingPage.pk,lugar='2').first()
    logo = Imagen.objects.filter(content_type=ct,object_id=landingPage.pk,lugar='1').first()

    logo = obtenerImagen(logo)
    cabecera = obtenerImagen(cabecera)

    imagenCabecera = "data:{ct};base64,{fi}".format(ct=cabecera.content_type_file, fi=cabecera.file)
    

    direccion = empresa.direccion
   
    latitud = str(landingPage.geolocalizacion.latitude)
    longitud = str(landingPage.geolocalizacion.longitude)
    latitud.replace(',','.')
    longitud.replace(',','.')
    return render_to_response(template_name,{'cabecera' : imagenCabecera,'logo':logo,'lp':landingPage,
                                             'direccion':direccion,'lat':latitud,'lon':longitud,
                                             'id':empresa.url},context_instance=RequestContext(request))
def LandingPageViewDefault(request):
    template_name = "landingPage/default.html"
    
    return render_to_response(template_name,context_instance=RequestContext(request))
        
def LandingPageSignIn(request,url,authentication_form):
    template_name = "landingPage/sign_in.html"
    empresa = Empresas.objects.get(url=url)
    print request.method
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)        
        print user
        if user is not None:
            empresa_usuario = Empresas.objects.get(usuario=user)
            if empresa_usuario == empresa:
                login(request,user)
                return HttpResponseRedirect("/panelprincipal/")
        
    landingPage = CabLandingPage.objects.get(empresa_id=empresa.pk)
    ct = ContentType.objects.get(model=landingPage.get_model())
    galeria = Imagen.objects.filter(content_type=ct,object_id=landingPage.pk,lugar='3')
    logo = Imagen.objects.filter(content_type=ct,object_id=landingPage.pk,lugar='1').first()
    cabecera = Imagen.objects.filter(content_type=ct,object_id=landingPage.pk,lugar='2').first()
    cabecera = obtenerImagen(cabecera)
    logo = obtenerImagen(logo)
    galeria = obtenerImagenes(galeria)
    #print cabecera.file
    #imagenCabecera = "data:{ct};base64,{fi}".format(ct=cabecera.content_type_file, fi=cabecera.file)
    
    contenido = APPCC.objects.get(empresa_id=empresa.pk)
    #print imagenCabecera
    #propiedades = Propiedades.objects.filter(modelo=landingPage.get_model(),modelo_id=landingPage.pk).values_list('destino_id')
    #print propiedades
    #imagenes = Imagen.objects.filter(pk__in=propiedades)
    #ct = ContentType.objects.filter(model=landingPage.get_model())
    #imagenes = Imagen.objects.filter(content_type=ct.first(),object_id=landingPage.pk)
    #print imagenes
    #print landingPage.get_model()
    #return render_to_response(template_name, {'objeto' : landingPage, 'auxiliar' : auxiliar,'imagenes' : obtenerImagenes(imagenes) },context_instance=RequestContext(request))
    #print type(landingPage.geolocalizacion.latitude)
    latitud = str(landingPage.geolocalizacion.latitude)
    longitud = str(landingPage.geolocalizacion.longitude)
    latitud.replace(',','.')
    longitud.replace(',','.')
    return render_to_response(template_name,{'galeria' : galeria,'logo':logo,
                                             'cabecera' : cabecera,'id':empresa.url,'form':authentication_form},context_instance=RequestContext(request))

def LandingPageSignInDefault(request,authentication_form):
    template_name = "landingPage/default_sign_in.html"
    #auxiliar   = {"etiqueta" : "Crear Landing Page",}
    #print pk
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/panelprincipal/")
    
    return render_to_response(template_name,{'form':authentication_form},context_instance=RequestContext(request))
    
@login_required
@user_passes_test(is_allowed_edit)
def convertir(request):
    template_name = "landingPage/landing_page.html"
    empresas = Empresas.objects.all()
    for empresa in empresas:
        aux = empresa.descripcion.lower()
        aux = aux.replace(" ","")
        aux = aux.replace("_","")
        empresa.url = aux
        empresa.nombrecomercial = empresa.descripcion.lower()
        empresa.save()

