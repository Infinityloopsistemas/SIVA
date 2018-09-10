# -*- coding: utf-8 -*-
from appcc.models import CabRegistros
from maestros.models import Terceros, Personal, Actividades, Unidades, ParametrosAnalisis, CatalogoEquipos, TiposTemperaturas, Zonas, ConsumiEspecificaciones, TiposFrecuencias, TiposLimitesCriticos, TiposMedidasVigilancia, TiposMedidasActuacion, Consumibles,\
    ExcepcionesCalendario
from django.contrib import admin
from maestros_generales.models import Empresas
from siva.utils import EsqueletoModelAdmin

__author__ = 'julian'

class MaestrosGenerales(EsqueletoModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(MaestrosGenerales,self).queryset(request)
        return qs.filter( empresa__in=Empresas.objects.filter(usuario=request.user) )



class TercerosAdmin(MaestrosGenerales):
    fieldsets=(('Terceros',{'fields': (('tipotercero','cif'),
                                       'denominacion','direccion1','registrosani', ('direccion2','municipio'),('codpostal','provincia'),('pais','telefono'),('email','paginaweb') )
    }),)

    #form  = make_ajax_form(Terceros, dict(municipio='municipios',provincia='provincias',pais='paises'))
    raw_id_fields = ('municipio','provincia','pais',)
    autocomplete_lookup_fields = {
        'fk': ['provincia','municipio','pais'],
        }




admin.site.register(Terceros,TercerosAdmin)

class PersonalAdmin(MaestrosGenerales):
    fieldsets=(('Personal',{'fields': (('apellidos','nombres'),
                                       ('dni','estadocivil','fechanacimiento'), ('sexo','nss','cargo'),'observaciones', )
    }),)


    list_display = ['apellidos','nombres','dni','cargo']
    search_fields = ['apellidos','nombres','dni','cargo']


class ActividadesAdmin(MaestrosGenerales):
    fieldsets=(('Actividades',{'fields': ( 'denominacion', )}),)


class UnidadesAdmin(MaestrosGenerales):
    fieldsets=(('Unidades',{'fields': ( 'denominacion', )}),)


class ParametrosAnalisisAdmin(MaestrosGenerales):
    fieldsets=(('Parametros',{'fields': (('tipo','denominacion','unidades') )
    }),)

    list_display = ['denominacion','tipo','unidades']


class CatalogoEquiposAdmin(MaestrosGenerales):
    fieldsets=(('Equipos',{'fields': (('noserie','denominacion'),'caracteristicas',('marcas','fadquirir','finstala','modelo') )
    }),)

    list_display = ['denominacion','noserie','marcas']
    raw_id_fields = ['marcas']

class TiposTempAdmin(MaestrosGenerales):
    fieldsets=(('Temperaturas',{'fields': ( 'denominacion',('tmax','tmin') )}),)

    list_display = ['denominacion','tmax','tmin']


class ZonasAdmin(MaestrosGenerales):
    fieldsets=(('Zonas',{'fields': ( 'denominacion',('superficie','tipotemp') )}),)

    list_display = ['denominacion','superficie','tipotemp']
    raw_id_fields = ['tipotemp']

class TiposMedActuaAdmin(MaestrosGenerales):
    fieldsets=(('Medidas de Actuación',{'fields': (( 'denominacion','tipo'),'ayuda' )}),)

    list_display = ['denominacion','tipo',]
    search_fields = ['denominacion','tipo']


class TiposMedVigAdmin(MaestrosGenerales):
    fieldsets=(('Medidas de Vigilancia',{'fields': ('denominacion','ayuda' )}),)

    list_display = ['denominacion']
    search_fields = ['denominacion']

class TiposLimCritAdmin(MaestrosGenerales):
    fieldsets=(('Limites Criticos',{'fields': (('denominacion',('valormax','valormin','unidades'),'ayuda') )}),)
    list_display = ['denominacion','valormax','valormin']
    search_fields = ['denominacion']
    raw_id_fields =['unidades']

class ConsumiblesEspeciDeta(admin.TabularInline):
    model= ConsumiEspecificaciones
    fieldsets=(('Detalles Consumibles',{'fields': ('descripcion',)}),)

class ConsumiblesAdmin(MaestrosGenerales):
    fieldsets=(('Consumibles',{'fields': (('denominacion','tipo'))}),)
    inlines = [ConsumiblesEspeciDeta]
    list_display = ['denominacion','tipo']

class TiposFrecueAdmin(MaestrosGenerales):
    fieldsets=(('Frecuencias',{'fields': ('denominacion','nounidades')}),)

    list_display = ['denominacion','nounidades']

class ExcepcionesCalendarioAdmin(EsqueletoModelAdmin):

    list_display = ['denominacion','fecha_inicio','fecha_final']
    fieldsets=(('Denominacion y Fechas',{'fields': ('denominacion',('fecha_inicio','fecha_final'))}),)

    def get_queryset(self, request):
        qs = super(EsqueletoModelAdmin,self).queryset(request)
        return qs.filter( empresa__in=Empresas.objects.filter(usuario=request.user) )

    def save_model(self, request, obj, form, change):

        obj.user    = request.user
        obj.empresa=  Empresas.objects.filter(usuario=request.user)[0]
        obj.save()

admin.site.register(Personal,PersonalAdmin)
admin.site.register(Actividades,ActividadesAdmin)
admin.site.register(Unidades,UnidadesAdmin)
admin.site.register(ParametrosAnalisis,ParametrosAnalisisAdmin)
admin.site.register(CatalogoEquipos,CatalogoEquiposAdmin)
admin.site.register(TiposTemperaturas,TiposTempAdmin)
admin.site.register(Zonas,ZonasAdmin)
admin.site.register(TiposMedidasActuacion,TiposMedActuaAdmin)
admin.site.register(TiposMedidasVigilancia,TiposMedVigAdmin)
admin.site.register(TiposLimitesCriticos,TiposLimCritAdmin)
admin.site.register(Consumibles,ConsumiblesAdmin)
admin.site.register(TiposFrecuencias,TiposFrecueAdmin)
admin.site.register(ExcepcionesCalendario,ExcepcionesCalendarioAdmin)

