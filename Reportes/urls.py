# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from reportes.views import ReportesListaView

__author__ = 'julian'


urlpatterns = patterns('',
    url (
        regex = '^lista/(?P<pmodelo>\w+)/(?P<ptpid>\d+)/(?P<pid>\d+)/$',
        view =  ReportesListaView.as_view(),
        name = 'reportes_list'
    ),
    url (
        regex = '^impresion/(?P<pid>\d+)/(?P<id>\d+)/$',
        #regex = '^impresion/(?P<pid>\d+)/(?P<id>\d+)/$',
        view =  'reportes.views.impresion',
        name = 'reportes_impresion'
    ),


)