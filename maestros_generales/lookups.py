# -*- coding: utf-8 -*-
from selectable.decorators import login_required
from maestros.models import TiposMedidasActuacion, TiposLimitesCriticos, TiposMedidasVigilancia, TiposTemperaturas, TiposFrecuencias, Zonas, Terceros, CatalogoEquipos, Personal, Consumibles
from selectable.base import ModelLookup
from selectable.registry import registry
from maestros_generales.models import Provincias, Paises, CodigosPostales, Municipios, TiposCatProfesional, ZonasFao, Marcas, Ingredientes

__author__ = 'julian'

@login_required
class PaisesLookup(ModelLookup):
    model = Paises
    search_fields = ('nombre__icontains',)

    def get_item_value(self, item):
        return item.nombre

    def get_item_label(self, item):
        return "%s" % (item.nombre)

registry.register(PaisesLookup)

@login_required
class ProvinciasLookup(ModelLookup):
    model = Provincias
    search_fields = ('nombre__icontains',)

    def get_item_value(self, item):
        return item.nombre

    def get_item_label(self, item):
        return "%s" % (item.nombre)

registry.register(ProvinciasLookup)

@login_required
class CodigoPostalLookup(ModelLookup):
    model = CodigosPostales
    search_fields = ('codpostal__icontains',)


    def get_item_value(self, item):
        return item.codpostal

    def get_item_label(self, item):
        return "%s" % (item.codpostal)

registry.register(CodigoPostalLookup)

@login_required
class MunicipiosLookup(ModelLookup):
    model = Municipios
    search_fields = ('municipio__icontains',)


    def get_item_value(self, item):
        return item.municipio

    def get_item_label(self, item):
        return "%s" % (item.municipio)

registry.register(MunicipiosLookup)

@login_required
class MarcasLookup(ModelLookup):
    model = Marcas
    search_fields = ('descripcion__icontains',)


    def get_item_value(self, item):
        return item.descripcion

    def get_item_label(self, item):
        return "%s" % (item.descripcion)

registry.register(MarcasLookup)

@login_required
class TpCatProfesionalLookup(ModelLookup):
    model = TiposCatProfesional
    search_fields = ('denominacion__icontains',)


    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(TpCatProfesionalLookup)

@login_required
class ZonasFaoLookup(ModelLookup):
    model = ZonasFao
    search_fields = ('denominacion__icontains',)

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(ZonasFaoLookup)


@login_required
class IngredientesLookup(ModelLookup):
    model = Ingredientes
    search_fields = ('nombre__icontains',)

    def get_item_value(self, item):
        return item.nombre

    def get_item_label(self, item):
        return "%s" % (item.nombre)

registry.register(IngredientesLookup)