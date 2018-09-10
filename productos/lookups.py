# -*- coding: utf-8 -*-
from selectable.registry import registry
from selectable.base import ModelLookup
from maestros_generales.models import Empresas
from productos.models import Canales, Tipos, Familias, Denominacion, TiposEnvases, Dimensiones, Productos, Ingredientes, Grupos
from selectable.decorators import login_required
__author__ = 'julian'



@login_required
class BaseLookup(ModelLookup):

    search_fields=('denominacion__icontains',)


    def get_query(self, request, term):
        results = super(BaseLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)


class CanalLookup(BaseLookup):
    def __init__(self):
        self.model = Canales
        super(CanalLookup,self).__init__()


registry.register(CanalLookup)


class GruposLookup(BaseLookup):

    def __init__(self):
        self.model = Grupos
        super(GruposLookup,self).__init__()


registry.register(GruposLookup)


class TiposLookup(BaseLookup):
    def __init__(self):
        self.model =Tipos
        super(TiposLookup,self).__init__()


registry.register(TiposLookup)


class FamiliasLookup(BaseLookup):
    def __init__(self):
        self.model=Familias
        super(FamiliasLookup,self).__init__()


registry.register(FamiliasLookup)


class DenominacionLookup(BaseLookup):
    def __init__(self):
        self.model=Denominacion
        super(DenominacionLookup,self).__init__()


registry.register(DenominacionLookup)


class TiposEnvasesLookup(BaseLookup):
    def __init__(self):
        self.model=TiposEnvases
        super(TiposEnvasesLookup,self).__init__()


registry.register(TiposEnvasesLookup)


class DimensionesLookup(BaseLookup):
    def __init__(self):
        self.model=Dimensiones
        super(DimensionesLookup,self).__init__()


registry.register(DimensionesLookup)


@login_required
class ProductosLookup(ModelLookup):

    search_fields=('denominacion__denominacion__icontains',)
    model= Productos

    def get_query(self, request, term):
        results = super(ProductosLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion.denominacion)



registry.register(ProductosLookup)






