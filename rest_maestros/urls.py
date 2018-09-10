from django import views
from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_maestros.views import TercerosViewSet, TercerosGenericView, TercerosDetail, TercerosListView

__author__ = 'julian'


# router = DefaultRouter()
# router.register(r'^terceros', TercerosListRest)
# urlpatterns = router.urls


urlpatterns = patterns('',
    url(r'^terceros/$', TercerosViewSet.as_view({'get':'list'})),
     url(r'^terceroseditar/$', TercerosViewSet.as_view({'get':'retrieve'})),
    url(r'^terceroslist/$', TercerosGenericView.as_view(), name='terceros-list'),
    url(r'^listaterceros/$', TercerosListView.as_view() ),
    url(r'^detailterceros/$', TercerosDetail.as_view() ),
)
