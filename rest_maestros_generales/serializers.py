# -*- coding: utf-8 -*-
from maestros_generales.models import TiposTerceros, Paises, Municipios, Provincias, CodigosPostales

__author__ = 'julian'
from rest_framework import routers, serializers, viewsets




class TiposTercerosSerializer(serializers.ModelSerializer):

    class Meta:
        model = TiposTerceros
        fields = ('id','descripcion','accion','fechaalta','fechabaja')

class PaisesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paises
        fields = ('id','nombre')

class ProvinciasSerializer(serializers.ModelSerializer):

     pais = PaisesSerializer()

     class Meta:
         model=Provincias
         fields = ('id','codprovincia','nombre','tipo','pais')



class MunicipiosSerializer(serializers.ModelSerializer):

     provincia  = ProvinciasSerializer()

     class Meta:
         model = Municipios
         fields = ('id','municipio','provincia')




class CodigosPostalesSerializer(serializers.ModelSerializer):

    provincia  = ProvinciasSerializer()

    class Meta:
        model=CodigosPostales
        fields =('id','codpostal','calle','provincia')


#token tec1: aeb251c825176a8351e447fe1f49c5b6353056a7

# pip install django-cors-headers
# pip install drf-json-api