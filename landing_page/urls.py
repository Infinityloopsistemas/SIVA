from django.conf.urls import patterns, url, include
from landing_page.views import LandingPageSignIn,LandingPageSignInDefault
from landing_page.forms import AuthenticationForm
from gestion_usuarios.utils import is_allowed_edit
from django.contrib.auth.decorators import user_passes_test

urlpatterns = patterns('',
    url (
        regex = '^convertir/$',
        view =  'landing_page.views.convertir',
        name = 'convertir'
    ),
    url (
        regex = '^(?P<url>\w+)$',
        view =  'landing_page.views.LandingPageView',
        name = 'landing_page_view'
    ),
    url (
        regex = '^$',
        view =  'landing_page.views.LandingPageViewDefault',
        name = 'landing_page_view_default'
    ),
    url (
        r'^sign_in/$',
        LandingPageSignInDefault,
        {'authentication_form':AuthenticationForm},
    ),   
#     url (
#         regex = '^landing_page/add$',
#         view =  'landing_page.views.LandingPageCrear',
#         name = 'landing_page_add'
#     ),
    url (
        r'^sign_in/(?P<url>\w+)$',
        #regex = '^sign_in/$',
        #view =  'landing_page.views.LandingPageSignIn',
        LandingPageSignIn,
        {'authentication_form':AuthenticationForm},
        #view = 'django.contrib.auth.views.login',
        #name = 'landing_page_sign_in',
        #template = 'landing_page/sign_in.html'
        
    ),

    #url(r'^sign_in/(?P<pk>\d+)$', 'django.contrib.auth.views.login', {'template_name': 'landingPage/sign_in.html'}
        
    #),     
)