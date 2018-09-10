# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from maestros.models import Terceros

__author__ = 'julian'
from rest_framework import routers, serializers, viewsets


class TercerosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Terceros
        fields = ('id','denominacion','cif','direccion1','direccion2','telefono','email','paginaweb','percontacto','registrosani')





#token tec1: aeb251c825176a8351e447fe1f49c5b6353056a7

# pip install django-cors-headers
# pip install drf-json-api