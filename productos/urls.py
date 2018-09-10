# -*- coding: utf-8 -*-
from productos.views import ProductosListaView, ProductosDetalleView, ProductosEliminarView

__author__ = 'julian'
from django.conf.urls import patterns, url, include
from siva.utils import make_url_list
from productos.views import *

__author__ = 'julian'

lista_urls=('canales','grupos','tipos','familias','denominacion','tiposenvases','dimensiones',)


tup =  tuple(make_url_list(lista_urls,'productos'))
urlpatterns = patterns('', *tup)

urlpatterns += patterns('',
    url (
        #regex = '^productos/lista/$',
        regex = '^productos/$',
        view =  user_passes_test(is_allowed_see)(ProductosListaView.as_view()),
        name = 'productos_list'
    ),

    url (
        regex = '^productos/detalle/(?P<pk>\d+)/$',
        view =  ProductosDetalleView.as_view(),
        name = 'productos_detail'
    ),
    url (
        regex = '^productos/crear/$',
        view =  user_passes_test(is_allowed_edit)('productos.views.ProductosCrearView'),
        name = 'productos_crear'
    ),

    url (
        regex = '^productos/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(ProductosEliminarView.as_view()),
        name = 'productos_eliminar'
    ),
    url (
        regex = '^productos/actualizar/(?P<pk>\d+)/$',
        view  =  'productos.views.ProductosActualizarView',
        name  = 'productos_actualizar'
    ),
)