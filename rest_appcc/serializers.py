# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from appcc.models import DetallesRegistros
from maestros.models import CatalogoEquipos, Zonas

__author__ = 'julian'
from rest_framework import routers, serializers, viewsets


class DetallesRegistrosSerialize(serializers.ModelSerializer):

    equipos = serializers.SerializerMethodField()
    zonas  = serializers.SerializerMethodField()


    class Meta:
        model = DetallesRegistros
        fields = ("cabreg","tplimitcrit","zonas","equipos","valanali","ordagenda","diaejecuta","tpturnos","tracksondas")


    def get_zonas(self, obj):
      #times 1000 for javascript.
      nombre = Zonas.objects.get(pk=obj.zonas.id).denominacion
      return nombre

    def get_equipos(self,obj):
        nombre = CatalogoEquipos.objects.get(pk=obj.equipos.id).denominacion
        return nombre



#token tec1: aeb251c825176a8351e447fe1f49c5b6353056a7

# pip install django-cors-headers
# pip install drf-json-api