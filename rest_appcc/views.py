from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from appcc.models import DetallesRegistros
from rest_framework import generics
from rest_appcc.serializers import DetallesRegistrosSerialize

__author__ = 'julian'

from rest_framework import permissions, filters, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_json_api.renderers import JsonApiRenderer
from rest_framework_jsonp.renderers import JSONPRenderer
from maestros.models import Terceros
from rest_maestros.serializers import TercerosSerializer



class DetallesRegistrosViewSet(viewsets.ViewSet):

    renderer_classes = (JSONRenderer,)
    authentication_classes = ( BasicAuthentication, TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


    def list(self,request):
        print request
        queryset = DetallesRegistros.objects.all().order_by('actividades')
        serializer = DetallesRegistrosSerialize(queryset,many=True)
        return Response(serializer.data)




class DetallesRegistrosViewSet(viewsets.ModelViewSet):

    renderer_classes = (JSONRenderer,)
    queryset = DetallesRegistros.objects.all().order_by('actividades')
    authentication_classes = ( BasicAuthentication, TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)



    def list(self,request):
        empid    = self.request.query_params.get('empid', None)
        queryset = self.queryset.filter(empresa__id=empid)
        serializer = DetallesRegistrosSerialize(queryset,many=True)
        return Response(serializer.data)

    def sensores(self, request):
        empid  = self.request.query_params.get('empid', None)
        detreg = self.queryset.filter(empresa__id=empid,tracksondas__isnull=False)
        serializer = DetallesRegistrosSerialize(detreg,many=True)
        return Response(serializer.data,headers={'Access-Control-Allow-Origin':'*',
                                                                           'Access-Control-Allow-Methods':'GET',
                                                                           'Access-Control-Allow-Headers':'Access-Control-Allow-Origin, x-requested-with, content-type',
                                                                           })





