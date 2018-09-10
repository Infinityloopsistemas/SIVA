# -*- coding: utf-8 -*-
import time
from loaddata.models import LoadDataSensor

__author__ = 'julian'
from rest_framework import routers, serializers, viewsets



class LoadDataSensorSerialize(serializers.ModelSerializer):

    date = serializers.SerializerMethodField()

    class Meta:
        model  = LoadDataSensor
        fields = ("tracksonda","Temperature","date","Name","loadatadevice")

    def get_date(self, obj):
      #times 1000 for javascript.
      return time.mktime(obj.date.timetuple()) * 1000




#token tec1: aeb251c825176a8351e447fe1f49c5b6353056a7

# pip install django-cors-headers
# pip install drf-json-api