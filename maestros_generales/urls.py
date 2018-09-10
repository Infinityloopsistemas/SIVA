# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from siva.utils import make_url_list
from maestros_generales.views import *

__author__ = 'julian'

lista_urls=('tiposimpuestos','tiposterceros','paises','provincias','codigospostales','municipios','empresas','marcas','tipoplancontrol','tiposcatprofesional','zonasfao','tiposdocumentos','ingredientes','componentes')


tup =  tuple(make_url_list(lista_urls,'maestros_generales'))
urlpatterns = patterns('', *tup)


