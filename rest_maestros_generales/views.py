from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer
from maestros_generales.models import TiposTerceros, Provincias, Paises, Municipios, CodigosPostales
from rest_maestros_generales.serializers import TiposTercerosSerializer, PaisesSerializer, ProvinciasSerializer, \
    MunicipiosSerializer, CodigosPostalesSerializer

__author__ = 'julian'

from rest_framework import permissions, filters, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import generics, mixins

#Devuelve paginada la informacion
# class TercerosListView(generics.ListAPIView):
#     renderer_classes = (JSONRenderer,)
#     paginate_by = 5
#     paginate_by_param = 'page_size'
#     max_paginate_by = 10
#     queryset = Terceros.objects.all()
#     pagination_class = PageNumberPagination
#     serializer_class = TercerosSerializer

class MaestrosGeneralesMixin(object):
    authentication_classes = ( BasicAuthentication, TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (JSONRenderer,)


#####TIPOS TERCEROS ###

class TiposTercerosMixin(MaestrosGeneralesMixin):
    model= TiposTerceros
    serializer_class = TiposTercerosSerializer
    queryset= TiposTerceros.objects.all()


class TiposTercerosList(TiposTercerosMixin,generics.ListCreateAPIView):
   pass

class TiposTercerosDetail(TiposTercerosMixin,generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'descripcion'
    pass

##### PROVINCIAS ######

class ProvinciasMixin(MaestrosGeneralesMixin):
    model= Provincias
    serializer_class = ProvinciasSerializer
    queryset= Provincias.objects.all()

class ProvinciasList(ProvinciasMixin,generics.ListCreateAPIView):
   pass

class ProvinciasDetail(ProvinciasMixin,generics.RetrieveUpdateDestroyAPIView):
    pass

#### PAISES #########

class PaisesMixin(MaestrosGeneralesMixin):
    model= Paises
    serializer_class = PaisesSerializer
    pagination_class = None
    queryset= Paises.objects.all()

class PaisesList(PaisesMixin,generics.ListCreateAPIView):

   pass

class PaisesDetail(PaisesMixin,generics.RetrieveUpdateDestroyAPIView):
    pass

#### MUNICIPIOS ######

class MunicipiosMixin(MaestrosGeneralesMixin):
    model= Municipios
    serializer_class = MunicipiosSerializer
    queryset= Municipios.objects.all()

class MunicipiosList(PaisesMixin,generics.ListCreateAPIView):
   pass

class MunicipiosDetail(MunicipiosMixin,generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'municipio'
    #lookup_field = 'pk'
    pass

#### CODIGOS POSTAELS ####

class CodigosPostalesMixin(MaestrosGeneralesMixin):
    model= CodigosPostales
    serializer_class = CodigosPostalesSerializer
    queryset= CodigosPostales.objects.all()

class CodigosPostalesList(PaisesMixin,generics.ListCreateAPIView):
   pass

class CodigosPostalesDetail(PaisesMixin,generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'municipio'
    lookup_field = 'pk'
    pass




#/rest_maestros/terceros/ -H 'Authorization: Token ec4d249d7aab14672ded96ae821f236c6c018014'