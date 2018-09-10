from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_waspmote.views import LoadWaspMoteViewSet

__author__ = 'julian'



waspmote_urls = patterns('',
    url(r'^gpstrack', LoadWaspMoteViewSet.as_view()),

)



urlpatterns = format_suffix_patterns(waspmote_urls)