# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from siva.utils import make_url_list
from maestros.views import *

__author__ = 'julian'

#lista_urls=('terceros','personal','actividades','unidades','parametrosanalisis','catalogoequipos','tipostemperaturas','zonas','tiposmedidasactuacion','tiposmedidasvigilancia','tiposlimitescriticos','tiposfrecuencias','etapas','peligros','tiposcursos','tiposlegislacion','tiposprocesos','firmas')
lista_urls=('terceros','actividades','unidades','parametrosanalisis','catalogoequipos','tipostemperaturas','zonas','tiposmedidasactuacion','tiposmedidasvigilancia','tiposlimitescriticos','tiposfrecuencias','etapas','peligros','tiposcursos','tiposlegislacion','tiposprocesos','firmas')



tup =  tuple(make_url_list(lista_urls,'maestros'))
urlpatterns = patterns('', *tup)

urlpatterns += patterns('',
    url (
        #regex = '^consumibles/lista/$',
        regex = '^consumibles/$',
        view =  user_passes_test(is_allowed_see)(ConsumiblesListaView.as_view()),
        name = 'consumibles_list'
    ),

    url (
        regex = '^consumibles/detalle/(?P<pk>\d+)/$',
        view =  ConsumiblesDetalleView.as_view(),
        name = 'consumibles_detail'
    ),
    url (
        regex = '^consumibles/crear/$',
        view =  'maestros.views.ConsumiblesCrearView',
        name = 'consumibles_crear'
    ),

    url (
        regex = '^consumibles/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(ConsumiblesEliminarView.as_view()),
        name = 'consumibles_eliminar'
    ),
    url (
        regex = '^consumibles/actualizar/(?P<pk>\d+)/$',
        view =   'maestros.views.ConsumiblesActualizarView',
        name = 'consumibles_actualizar'
    ),
)
urlpatterns += patterns('',
    url (
        regex = '^personal/$',
        view =  user_passes_test(is_allowed_see)(PersonalListaView.as_view()),
        name = 'personal_list'
    ),

    url (
        regex = '^personal/detalle/(?P<pk>\d+)/$',
        view =  PersonalDetalleView.as_view(),
        name = 'personal_detail'
    ),
    url (
        regex = '^personal/crear/$',
        view =  user_passes_test(is_allowed_see)(PersonalCrearView.as_view()),
        name = 'personal_crear'
    ),

    url (
        regex = '^personal/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(PersonalEliminarView.as_view()),
        name = 'personal_eliminar'
    ),
    url (
        regex = '^personal/actualizar/(?P<pk>\d+)/$',
        view =   'maestros.views.PersonalActualizarView',
        name = 'personal_actualizar'
    ),
)

urlpatterns += patterns('',
    url (
        regex = '^documentos/lista/(?P<pmodelo>\w+)/(?P<pid>\d+)/$',
        view =  user_passes_test(is_allowed_see)(DocumentosListaView.as_view()),
        name = 'mdocumentos_list'
    ),

    url (
        regex = '^documentos/detalle/(?P<pk>\d+)/$',
        view =  DocumentosDetalleView.as_view(),
        name = 'mdocumentos_detail'
    ),
    url (
        regex = '^documentos/crear/(?P<pmodelo>\w+)/(?P<pid>\d+)/$',
        view =  'maestros.views.DocumentosCrearView',
        name = 'mdocumentos_crear'
    ),

    url (
        regex = '^documentos/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(DocumentosEliminarView.as_view()),
        name = 'mdocumentos_eliminar'
    ),
    url (
        regex = '^documentos/actualizar/(?P<pk>\d+)/$',
        view =   'maestros.views.DocumentosActualizarView',
        name = 'mdocumentos_actualizar'
    ),
)


urlpatterns += patterns('',
    url (
        #regex = '^tiposturnos/lista/$',
        regex = '^tiposturnos/$',
        view =  user_passes_test(is_allowed_see)(TiposturnosListaView.as_view()),
        name = 'tiposturnos_list'
    ),

    url (
        regex = '^tiposturnos/detalle/(?P<pk>\d+)/$',
        view =  TiposturnosDetalleView.as_view(),
        name = 'tiposturnos_detail'
    ),
    url (
        regex = '^tiposturnos/crear/$',
        view =  'maestros.views.TiposturnosCrearView',
        name = 'tiposturnos_crear'
    ),

    url (
        regex = '^tiposturnos/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(TiposturnosEliminarView.as_view()),
        name = 'tiposturnos_eliminar'
    ),
    url (
        regex = '^tiposturnos/actualizar/(?P<pk>\d+)/$',
        view =   'maestros.views.TiposturnosActualizarView',
        name = 'tiposturnos_actualizar'
    ),
)