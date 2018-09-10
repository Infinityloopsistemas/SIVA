# -*- coding: utf-8 -*-
from selectable.base import ModelLookup
from selectable.decorators import login_required
from selectable.registry import registry
from appcc.models import CabRegistros, ValoresAnaliticas, CuadrosGestion
from loaddata.models import TrackTemperaturas
from maestros.models import ParametrosAnalisis
from maestros_generales.models import Empresas

@login_required
class TrackTemperaturasLookup(ModelLookup):
    model = TrackTemperaturas
    search_fields = ('DeviceName__icontains',)

    def get_query(self, request, term):
        results = super(TrackTemperaturasLookup, self).get_query(request, term)
        usuario = request.user
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
         return "%s -%s" % (item.DeviceName,item.HostName)

    def get_item_label(self, item):
        return "%s -%s" % (item.DeviceName,item.HostName)

registry.register(TrackTemperaturasLookup)

@login_required
class CuadrosGestionLookup(ModelLookup):
    model = CuadrosGestion
    search_fields = ('etapa__denominacion__icontains',)

    def get_query(self, request, term):
        results = super(CuadrosGestionLookup, self).get_query(request, term)
        usuario = request.user
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
         return "%s -%s" % (item.orden,item.etapa.denominacion)

    def get_item_label(self, item):
        return "%s -%s" % (item.orden,item.etapa.denominacion)

registry.register(CuadrosGestionLookup)



@login_required
class CabRegistrosLookup(ModelLookup):
    model = CabRegistros
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(CabRegistrosLookup, self).get_query(request, term)
        usuario = request.user
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(CabRegistrosLookup)

@login_required
class ParametrosAnalisiANALookup(ModelLookup):
    model = ParametrosAnalisis
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(ParametrosAnalisiANALookup, self).get_query(request, term)
        id =request.GET['manautctrl__manautctrl__id']
        print id
        #lista   = ValoresAnaliticas.objects.filter(manautctrl__manautctrl__id=id).values_list('paramanali_id')
        #lista   = ValoresAnaliticas.objects.filter(manautctrl__id=id).values_list('paramanali_id')
        #lista   = ValoresAnaliticas.objects.filter(manautctrl__id=id)
        lista   = ParametrosAnalisis.objects.filter(empresa=Empresas.objects.filter(usuario__username=request.user))
        results = results.filter(id__in=lista)
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(ParametrosAnalisiANALookup)