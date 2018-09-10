from django.conf.urls import patterns, url, include
from landing_page.views import LandingPageSignIn,LandingPageSignInDefault
from landing_page.forms import AuthenticationForm

urlpatterns = patterns('',
    url (
        regex = '^crear_usuarios/$',
        view =  'gestion_usuarios.views.CrearUsuariosView',
        name = 'crear_usuarios_view'
    ),
    url (
        regex = '^borrar_usuarios/$',
        view =  'gestion_usuarios.views.BorrarUsuariosView',
        name = 'borrar_usuarios_view'
    ),
    url (
        regex = '^crear_usuario/$',
        view =  'gestion_usuarios.views.CrearUsuarioView',
        name = 'crear_usuario_view'
    ),
    url (
        regex = '^borrar_usuario/$',
        view =  'gestion_usuarios.views.BorrarUsuarioView',
        name = 'borrar_usuario_view'
    ),
    url (
        regex = '^modificar_usuario/$',
        view =  'gestion_usuarios.views.ModificarUsuarioView',
        name = 'Modificar_usuario_view'
    ),
    url (
        regex = '^comprobar_usuarios_empresas/$',
        view =  'gestion_usuarios.views.comprobar_usuarios_empresas',
        name = 'comprobar_usuarios_empresas'
    ),  

)