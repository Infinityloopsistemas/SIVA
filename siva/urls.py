from dajaxice.core import dajaxice_config, dajaxice_autodiscover
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
#from rest_framework import routers
from filebrowser.sites import *
from ajax_select import urls as ajax_select_urls
from loaddata import views
from siva import settings
import appcc
import maestros
import maestros_generales
import productos
from siva.views import panelprincipal, contacto
from trazabilidad.views import trazabilidad
from siva.views import *


# router = routers.DefaultRouter()
# router.register(r'device', views.LoadDataDeviceViewSet)


admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^adminempresa/(?P<pk>\d+)/$', loginEmpresa),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^selectable/', include('selectable.urls')),
    
    #url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^desconectar/$', 'django.contrib.auth.views.logout',{'next_page':'/'}),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^maestros/', include('maestros.urls')),
    url(r'^maestros_generales/', include('maestros_generales.urls')),
    url(r'^maestros/panel', maestros.views.maestros),
    url(r'^maestros_generales/panel', maestros_generales.views.maestros_generales),
    url(r'^appcc/', include('appcc.urls')),
    url(r'^productos/', include('productos.urls')),
    url(r'^productos/panel', productos.views.productos),
    url(r'^trazabilidad/panel',trazabilidad),
    url(r'^trazabilidad/', include('trazabilidad.urls')),
    url(r'^reportes/', include('reportes.urls')),
    url(r'^appcc/panel', appcc.views.appcc),
    url(r'^panelprincipal', panelprincipal),
    url(r'^contacto/', contacto),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^documental/', include('private_files.urls')),
    url(r'^', include('landing_page.urls')),
    #url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^loaddata/device/$', views.LoadDataDeviceViewSet.as_view(), name='device'),
    url(r'^loaddata/device/(?P<pk>\d+)/$', views.LoadDataDeviceViewSet.as_view(), name='device'),
    #url(r'^landing_page/', include('landing_page.urls'))
    url(r'^gestion_usuarios/',include('gestion_usuarios.urls')),
    url(r'^rest_maestros/',include('rest_maestros.urls')),
    url(r'^rest_loaddata/',include('rest_loaddata.urls')),
    url(r'^rest_appcc/',include('rest_appcc.urls')),
    url(r'^grafsensores/', graficas_sensores),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$','serve'),
    )
