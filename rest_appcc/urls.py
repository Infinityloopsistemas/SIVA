from django.conf.urls import patterns, url
from rest_appcc.views import DetallesRegistrosViewSet

__author__ = 'julian'


urlpatterns = patterns('',
    url(r'^detreglist/$', DetallesRegistrosViewSet.as_view({'get':'list'})),
     url(r'^detregsensor/$', DetallesRegistrosViewSet.as_view({'get':'sensores'})),
     )