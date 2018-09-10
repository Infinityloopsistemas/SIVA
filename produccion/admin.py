__author__ = 'julian'
from django.contrib import admin
from produccion.models import ZonasFao, TiposAnaliticas, TiposProcesos, CabProcesos, DetProcesos, TiposUbicaciones
from utils import EsqueletoModelAdmin





class ZonasFaoAdmin(EsqueletoModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('denominacion', ('zonasmaritimas','url_zona'), )
        }),
        )

    list_display = ['denominacion', 'urlZonaFao']
    search_fields = ['denominacion']
    list_filter = ['zonasmaritimas']



admin.site.register(ZonasFao,ZonasFaoAdmin)

class TiposAnaliticasAdmin(EsqueletoModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('descripcion','valoresmax'), )
        }),
        )

    list_display  = ['descripcion','valoresmax']
    search_fields = ['descripcion']
    list_filter   = ['descripcion']


admin.site.register(TiposAnaliticas)


class TiposProcesosAdmin(EsqueletoModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('descripcion','nivel'), ('pesado','etiquetado'),('falta','fbaja') )
        }),
        )
    list_display  = ['descripcion','nivel','pesado','etiquetado','falta','fbaja']
    search_fields = ['descripcion']
    list_filter   = ['nivel','pesado','etiquetado']


admin.site.register(TiposProcesos,TiposProcesosAdmin)


class TiposUbicacionesAdmin(EsqueletoModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('descripcion','parent'), ('limita_up','limita_down'),('limita_right','limita_left') )
        }),
        )
    list_display  = ['descripcion','parent','limita_up','limita_down','limita_right','limita_left']
    search_fields = ['descripcion']


admin.site.register(TiposUbicaciones,TiposUbicacionesAdmin)



class DetProcesosAdmin(admin.TabularInline):
    model=DetProcesos
    fieldsets = (
        (None, {
            'fields': (('descripcion','tproceso'),('tpubicacion','parent'),)
        }),
        )
    raw_id_fields = ('tproceso','tpubicacion',)
    autocomplete_lookup_fields = {'fk': ['tproceso','tpubicacion'], }

class CabProcesosAdmin(EsqueletoModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('descripcion'),('falta','fbaja') )
        }),
        )

    inlines = [DetProcesosAdmin]

    list_display  = ['descripcion']
    search_fields = ['descripcion']
    list_filter   = ['falta','fbaja']

admin.site.register(CabProcesos,CabProcesosAdmin)


class ProcesosAdmin(EsqueletoModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('cabprocesos','descripcion'),'tproceso', )
        }),
        )

admin.site.register(DetProcesos,ProcesosAdmin)