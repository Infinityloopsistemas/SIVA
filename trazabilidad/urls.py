# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import user_passes_test
from django.conf.urls import patterns, url, include
from siva.utils import make_url_list
from trazabilidad.views import *
from gestion_usuarios.utils import is_allowed_edit
__author__ = 'julian'

#lista_urls=('albaran',)

#tup =  tuple(make_url_list(lista_urls,'trazabilidad'))
#urlpatterns = patterns('', *tup)


urlpatterns = patterns('',
    url (
        regex = 'albaranentrada/$',
        view =  AlbaranEntradaListaView.as_view(),
        name = 'albaranentrada_list'
    ),

    url (
        regex = '^albaranentrada/detalle/(?P<pk>\d+)/$',
        view =  AlbaranEntradaDetalleView.as_view(),
        name = 'albaranentrada_detail'
    ),
    url (
        regex = '^albaranentrada/crear/$',
        view =  'trazabilidad.views.AlbaranEntradaCrearView',
        name = 'albaranentrada_crear'
    ),

    url (
        regex = '^albaranentrada/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(AlbaranEntradaEliminarView.as_view()),
        name = 'albaranentrada_eliminar'
    ),
    url (
        regex = '^albaranentrada/actualizar/(?P<pk>\d+)/$',
        view =  'trazabilidad.views.AlbaranEntradaActualizarView',
        name = 'albaranentrada_actualizar'
    ),

)
urlpatterns += patterns('',
    url (
        regex = 'albaransalida/$',
        view =  AlbaranSalidaListaView.as_view(),
        name = 'albaransalida_list'
    ),

    url (
        regex = '^albaransalida/detalle/(?P<pk>\d+)/$',
        view =  AlbaranSalidaDetalleView.as_view(),
        name = 'albaransalida_detail'
    ),
    url (
        regex = '^albaransalida/crear/$',
        view =  'trazabilidad.views.AlbaranSalidaCrearView',
        name = 'albaransalida_crear'
    ),

    url (
        regex = '^albaransalida/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(AlbaranSalidaEliminarView.as_view()),
        name = 'albaransalida_eliminar'
    ),
    url (
        regex = '^albaransalida/actualizar/(?P<pk>\d+)/$',
        view =  'trazabilidad.views.AlbaranSalidaActualizarView',
        name = 'albaransalida_actualizar'
    ),

)

urlpatterns += patterns('',
    url (
        regex = '^documentos/lista/(?P<pmodelo>\w+)/(?P<pid>\d+)/$',
        view =  DocumentosListaView.as_view(),
        name = 'tdocumentos_list'
    ),

    url (
        regex = '^documentos/detalle/(?P<pk>\d+)/$',
        view =  DocumentosDetalleView.as_view(),
        name = 'tdocumentos_detail'
    ),
    url (
        regex = '^documentos/crear/(?P<pmodelo>\w+)/(?P<pid>\d+)/$',
        view =  'trazabilidad.views.DocumentosCrearView',
        name = 'tdocumentos_crear'
    ),
    url (
        regex = '^documentos/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(DocumentosEliminarView.as_view()),
        name = 'tdocumentos_eliminar'
    ),
    url (
        regex = '^documentos/actualizar/(?P<pk>\d+)/$',
        view =   'trazabilidad.views.DocumentosActualizarView',
        name = 'tdocumentos_actualizar'
    ),
)



urlpatterns += patterns('',
    url (
        regex = 'lotes/$',
        view =  LotesListaView.as_view(),
        name = 'lotes_list'
    ),

    url (
        regex = '^lotes/detalle/(?P<pk>\d+)/$',
        view =  LotesDetalleView.as_view(),
        name = 'lotes_detail'
    ),
    url (
        regex = '^lotes/crear/$',
        view =  'trazabilidad.views.LotesCrearView',
        name = 'lotes_crear'
    ),

    url (
        regex = '^lotes/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(LotesEliminarView.as_view()),
        name = 'lotes_eliminar'
    ),
    url (
        regex = '^lotes/actualizar/(?P<pk>\d+)/$',
        view =  'trazabilidad.views.LotesActualizarView',
        name = 'lotes_actualizar'
    ),

)

urlpatterns += patterns('',
    url (
        regex = 'existencias/$',
        view =  'trazabilidad.views.ConsultaExistenciasView',
        name = 'existencias_list'
    )

)
