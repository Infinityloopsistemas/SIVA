# # -*- coding: utf-8 -*-
# __author__ = 'julian'
# from django.core.serializers import json
# from django.utils import simplejson
# from tastypie.authentication import BasicAuthentication, Authentication, ApiKeyAuthentication
# from tastypie.cache import SimpleCache
# from tastypie.paginator import Paginator
# from django.contrib.auth.models import User
# from tastypie.authorization import Authorization, DjangoAuthorization
# from tastypie import fields
# from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
# from maestros.models import Terceros, Personal, CatalogoEquipos, Rutas
# from tastypie.serializers import Serializer
#
#
# #Test acceso a las api desde linea de comandos
# # curl -i  -H "Content-Type: application/json"  -H "Authorization: Apikey julian:0da9276452681040a7b9f703ef8f9fc9e1254b74"  http://virtual.orthidal.infinityloop.es/maestros/api/recursos/rutas/
# from productos.models import Denominacion
#
#
# class LoadData(ModelResource):
#      class Meta:
#         #authentication  = ApiKeyAuthentication()
#         #authorization   = DjangoAuthorization()
#         paginator_class = Paginator
#         #excludes = ['user_id','empresa_id','fechabaja','fechaalta','dcientifico','descripcion']
#         #queryset = Denominacion.objects.filter(fechabaja=None)
#         resource_name = 'loadata'
