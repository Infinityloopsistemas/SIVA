# -*- coding: utf-8 -*-
# import string
# from django.db.models import Q
# from selectable.base import ModelLookup
# from selectable.decorators import login_required
# from selectable.registry import registry
# from maestros_generales.models import Empresas
# from trazabilidad.models import Lotes
# 
# __author__ = 'julian'
# 
# 
# 
# 
# @login_required
# class LotesLookup(ModelLookup):
#     model = Lotes
#     search_fields = ('numlote__icontains',)
# 
#     def get_query(self, request, term):
#         results = super(LotesLookup, self).get_query(request, term)
#         usuario = request.user
#         results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
#         return results
# 
#     def get_item_value(self, item):
#         return item.numlote
# 
#     def get_item_label(self, item):
#         return "%s" % (item.numlote)
# 
# registry.register(LotesLookup)


# @login_required
# class TiposUbicacionLookup(ModelLookup):
#     model = TiposUbicaciones
#     search_fields = ('denominacion__icontains',)
# 
#     def get_query(self, request, term):
#         results = super(TiposUbicacionLookup, self).get_query(request, term)
#         usuario = request.user
#         results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
#         return results
# 
#     def get_item_value(self, item):
#         return item.denominacion
# 
#     def get_item_label(self, item):
#         return "%s" % (item.denominacion)
# 
# registry.register(TiposUbicacionLookup)
# 
# 
# @login_required
# class CuadernosCamposLookup(ModelLookup):
#     model = CuadernoCampo
#     search_fields = ('descripcion__icontains',)
# 
#     def get_query(self, request, term):
#         results = super(CuadernosCamposLookup, self).get_query(request, term)
#         usuario = request.user
#         results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
#         return results
# 
#     def get_item_value(self, item):
#         return "%s - %s " % (item.descripcion,item.tercero)
# 
#     def get_item_label(self, item):
#         return "%s -%s" % (item.descripcion,item.tercero)
# 
# registry.register(CuadernosCamposLookup)
# 
# 
# 
# @login_required
# class SeriesLotesLookup(ModelLookup):
#     model = SeriesLotes
#     search_fields = ('serie__icontains',)
# 
#     def get_query(self, request, term):
#         results = super(SeriesLotesLookup, self).get_query(request, term)
#         usuario = request.user
#         results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
#         return results
# 
#     def get_item_value(self, item):
#         return item.serie
# 
#     def get_item_label(self, item):
#         return "%s - %s" % (item.serie,item.descripcion)
# 
# registry.register(SeriesLotesLookup)
# 
# 
# @login_required
# class ExistenciasLotesLookup(ModelLookup):
#     model = ExistenciasLotes
#     search_fields = ('numlote__icontains',)
# 
#     def get_query(self, request, term):
#         results  = super(ExistenciasLotesLookup, self).get_query(request, term)
#         usuario  = request.user
#         results  = results.filter(empresa__in=Empresas.objects.filter(usuario__username=usuario)). exclude(Q(saldocantidad=0),Q(saldopeso=0)).exclude( Q(saldocantidad=0),Q(saldovolumen=0))
#         return results
# 
#     def get_item_value(self, item):
#         return item.numlote
# 
#     def get_item_label(self, item):
#         return item.numlote
# 
# registry.register(ExistenciasLotesLookup)