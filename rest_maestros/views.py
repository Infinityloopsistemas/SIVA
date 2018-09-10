from django.core.paginator import Paginator
from rest_framework.generics import get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

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
from rest_framework import generics, mixins

#Devuelve paginada la informacion
class TercerosListView(generics.ListAPIView):
    renderer_classes = (JSONPRenderer,)
    paginate_by = 5
    paginate_by_param = 'page_size'
    max_paginate_by = 10
    queryset = Terceros.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = TercerosSerializer



class TercerosGenericView(generics.ListAPIView):
    renderer_classes = (JSONPRenderer,)
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Terceros.objects.all()
        pid = self.request.query_params.get('pid', None)
        if pid is not None:
            queryset = queryset.filter(pk=pid)
        return queryset


    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TercerosSerializer(queryset,many=True)
        return Response(serializer.data)

    def get_paginate_by(self):
        """
        Use smaller pagination for HTML representations.
        """
        if self.request.accepted_renderer.format == 'html':
            return 20
        return 10




class TercerosViewSet(viewsets.ModelViewSet):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    renderer_classes = (JSONPRenderer,)
    paginate_by = 5
    paginate_by_param = 'page_size'
    max_paginate_by = 10


    def list(self,request):
        queryset = Terceros.objects.all()
        empid = self.request.query_params.get('empid', None)
        queryset = queryset.filter(empresa_id=empid)
        serializer = TercerosSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request):
        queryset = Terceros.objects.all()
        pk = self.request.query_params.get('pk', None)
        terceros = get_object_or_404(queryset, pk=pk)
        serializer = TercerosSerializer(terceros)
        return Response(serializer.data)



    def create(self, request):
        pass

class TercerosDetail(RetrieveUpdateDestroyAPIView):

    authentication_classes = ( BasicAuthentication, TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


    #queryset = Terceros.objects.all()
    serializer_class = TercerosSerializer
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 10
    pagination_class = PageNumberPagination
    renderer_classes = (JSONPRenderer,)

    def list(self, request):
        queryset =  Terceros.objects.all()
        serializer = TercerosSerializer(queryset, many=True)
        return Response(serializer.data)
    #
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
    #
    def retrieve(self, request, pk=None):
        queryset = Terceros.objects.all()
        terceros = get_object_or_404(queryset, pk=pk)
        serializer = TercerosSerializer(terceros)
        return Response(serializer.data)




#/rest_maestros/terceros/ -H 'Authorization: Token ec4d249d7aab14672ded96ae821f236c6c018014'