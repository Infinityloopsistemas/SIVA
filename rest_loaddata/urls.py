from django.conf.urls import url, patterns
from rest_loaddata.views import LoadDataSensorViewSet

__author__ = 'julian'


urlpatterns = patterns('',
    url(r'^sensorlist/$', LoadDataSensorViewSet.as_view({'get':'list'})),
     url(r'^sensorfecha/$', LoadDataSensorViewSet.as_view({'get':'retrieve'})),
     )