# -*- coding: utf-8 -*-
from selectable.decorators import login_required
from maestros.models import TiposMedidasActuacion, TiposLimitesCriticos, TiposMedidasVigilancia, TiposTemperaturas, TiposFrecuencias, Zonas, Terceros, CatalogoEquipos, Personal, Consumibles, ParametrosAnalisis, Actividades, Etapas, Peligros, TiposCursos, TiposLegislacion, Unidades, Firmas, HorarioTurnos
from selectable.base import ModelLookup
from selectable.registry import registry
from maestros_generales.models import Empresas
from siva import settings

__author__ = 'julian'

@login_required
class TPActuacionPrevLookup(ModelLookup):
    model = TiposMedidasActuacion
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(TPActuacionPrevLookup, self).get_query(request, term)
        results = results.filter(tipo="P",empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(TPActuacionPrevLookup)

@login_required
class TPActuacionCorrLookup(ModelLookup):
    model = TiposMedidasActuacion
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(TPActuacionCorrLookup, self).get_query(request, term)
        results = results.filter(tipo="C",empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(TPActuacionCorrLookup)

@login_required
class TPLimitesCritLookup(ModelLookup):
    model = TiposLimitesCriticos
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(TPLimitesCritLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(TPLimitesCritLookup)

@login_required
class ActividadesLookup(ModelLookup):
    model =  Actividades
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(ActividadesLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(ActividadesLookup)

@login_required
class TipoMedidasVigilanciaLookup(ModelLookup):
    model = TiposMedidasVigilancia
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(TipoMedidasVigilanciaLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(TipoMedidasVigilanciaLookup)

@login_required
class TiposTemperaturasLookup(ModelLookup):
    model = TiposTemperaturas
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(TiposTemperaturasLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(TiposTemperaturasLookup)

@login_required
class TiposFrecuenciasLookup(ModelLookup):
    model = TiposFrecuencias
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(TiposFrecuenciasLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(TiposFrecuenciasLookup)

@login_required
class ZonasLookup(ModelLookup):
    model = Zonas
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(ZonasLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(ZonasLookup)

@login_required
class TercerosLookup(ModelLookup):
    model = Terceros
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(TercerosLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(TercerosLookup)

@login_required
class TercerosTiposLookup(ModelLookup):
    model = Terceros
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(TercerosTiposLookup, self).get_query(request, term)
        results = results.filter(tipotercero__descripcion=settings.ASESORSANITARIO, empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(TercerosTiposLookup)


@login_required
class CatalogoEquiposLookup(ModelLookup):
    model = CatalogoEquipos
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(CatalogoEquiposLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(CatalogoEquiposLookup)

@login_required
class PersonalLookup(ModelLookup):
    model = Personal
    search_fields = ('apellidos__icontains',)

    def get_query(self, request, term):
        results = super(PersonalLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.apellidos

    def get_item_label(self, item):
        return "%s %s" % (item.apellidos, item.nombres)

registry.register(PersonalLookup)

@login_required
class TiposCursosLookup(ModelLookup):
    model = TiposCursos
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(TiposCursosLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(TiposCursosLookup)


@login_required
class TiposLegislacionLookup(ModelLookup):
    model = TiposLegislacion
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(TiposLegislacionLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(TiposLegislacionLookup)


@login_required
class ConsumiblesLookup(ModelLookup):
    model = Consumibles
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(ConsumiblesLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(ConsumiblesLookup)


@login_required
class ParametrosAnalisisLookup(ModelLookup):
    model = ParametrosAnalisis
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(ParametrosAnalisisLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(ParametrosAnalisisLookup)

@login_required
class EtapasLookup(ModelLookup):
    model = Etapas
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(EtapasLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(EtapasLookup)

@login_required
class PeligrosLookup(ModelLookup):
    model = Peligros
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(PeligrosLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(PeligrosLookup)


@login_required
class UnidadesLookup(ModelLookup):
    model = Unidades
    search_fields = ('denominacion__icontains',)

    def get_query(self, request, term):
        results = super(UnidadesLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.denominacion

    def get_item_label(self, item):
        return "%s" % (item.denominacion)

registry.register(UnidadesLookup)


@login_required
class FirmasLookup(ModelLookup):
    model = Firmas
    search_fields = ('personal__apellidos__icontains',)

    def get_query(self, request, term):
        results = super(FirmasLookup, self).get_query(request, term)
        results = results.filter(empresa__in=Empresas.objects.filter(usuario__username=request.user))
        return results

    def get_item_value(self, item):
        return item.personal.apellidos

    def get_item_label(self, item):
        return "%s %s" % (item.personal__apellidos, item.personal__nombres)

registry.register(FirmasLookup)


@login_required
class HorarioTurnoLookup(ModelLookup):
    model = HorarioTurnos
    search_fields = ('ihora__icontains','fhora__icontains')

    def get_query(self, request, term):
        results = super(HorarioTurnoLookup, self).get_query(request, term)
        idtpturno = request.GET.get('idtpturno', '')
        if idtpturno:
            results = results.filter(tpturnos_id=idtpturno)
        return results

    def get_item_value(self, item):
        return  "%s - %s" % (item.ihora, item.fhora)

    def get_item_label(self, item):
        return "%s - %s" % (item.ihora, item.fhora)

registry.register(HorarioTurnoLookup)

