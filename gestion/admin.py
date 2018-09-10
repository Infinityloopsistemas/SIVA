# -*- coding: utf-8 -*-
from django.contrib import admin
from gestion.forms import LotesAdminForm
from gestion.models import SeriesLotes, DetAnaliticas, Procedencia, CabAnaliticas, Lotes, DetLotes, OrdenProduccion
from maestros.models import Terceros
from produccion.models import DetProcesos
from utils import *



class SeriesLotesAdmin(EsqueletoModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('serie' ,'descripcion'),)
        }),
        )

    list_display = ['serie','descripcion']
    search_fields = ['descripcion']




admin.site.register(SeriesLotes,SeriesLotesAdmin)


class ProcedenciaAdmin(EsqueletoModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('descripcion','tercero'),('zonafao','pesquero'),('origen','medio'),('formobtencion','fbaja'),)
        }),
        )

    list_display=['descripcion','tercero','zonafao','pesquero','origen','medio']
    search_fields = ['descripcion','tercero']
    list_filter =  ['zonafao','pesquero','origen','medio']
    raw_id_fields = ['tercero','zonafao']
    autocomplete_lookup_fields = {
        'fk': ['tercero','zonafao'],}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "tercero":
            #Tipo de tercero acreedor, filtra por todos los acreedores
            kwargs["queryset"] = Terceros.objects.filter(tipotercero__accion=1)
        return super(ProcedenciaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Procedencia,ProcedenciaAdmin)

class DetAnaliticasAdmin(admin.TabularInline):
    fieldsets = (
        (None, {
            'fields': (('tipoanalitica' ,'valores'),)
        }),
        )

    model = DetAnaliticas

    list_display=['tipoanalitica','valores']
    search_fields=['tipoanalitica','valores']
    raw_id_fields = ('tipoanalitica',)
    autocomplete_lookup_fields = {
            'fk': ['tipoanalitica'],}


class CabAnaliticasAdmin(EsqueletoModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('denominacion' ,'laboratorio',('proceso','fecha'),'docanalitica',)
        }),
        )

    inlines = [DetAnaliticasAdmin]


    list_display  = ['denominacion','proceso','fecha','laboratorio']
    search_fields = ['denominacion','proceso','laboratorio']
    list_filter   = ['proceso']
    raw_id_fields = ('proceso',)
    autocomplete_lookup_fields = {
        'fk': ['proceso'],}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "laboratorio":
            #Tipo de tercero acreedor, filtra por todos los acreedores
            kwargs["queryset"] = Terceros.objects.filter(tipotercero__accion=3)
        return super(CabAnaliticasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(CabAnaliticas,CabAnaliticasAdmin)


class OrdenProduccionAdmin(EsqueletoModelAdmin):
    fieldsets = (
        ('Identificiacion', {
            'fields': ('cuadcampo',('fecha','serlote'),('cabprocesos','numalbaran'),),
            }),
        ('Observaciones', {
            'fields': ('observaciones',),
            }),
        ('Cierre de Producción', {
            'fields': ('fecha_cierre',),
            }),
        )

    raw_id_fields = ['cuadcampo','cabprocesos','serlote',]
    autocomplete_lookup_fields = {
        'fk': ['cuadcampo','cabprocesos','serlote',],}

    list_display = ['fecha','numalbaran','iralotes','cuadcampo','cabprocesos','serlote','fecha_cierre']
    search_fields = ['cuadcampo','numalbaran','serlote','cabprocesos',]

    class Media:
#       css = { "all": (settings.STATIC_URL+"css/jquery.autocomplete.css",settings.STATIC_URL+"css/iconic.css",settings.STATIC_URL+"css/jquery.ui.dialog.css",settings.STATIC_URL+"css/apprise.css") }
        js  = (settings.STATIC_URL+"js/gestion_ordenproduccion_admin.js",)



admin.site.register(OrdenProduccion,OrdenProduccionAdmin)


class DetLotesAdmin(admin.TabularInline):
    model= DetLotes
    fieldsets = (
    ('Producto', {
        'classes': ('collapse open',),
        'fields' : ('producto','bultos','kilos','feccad'),
        }),
    )


    raw_id_fields = ['producto']
    autocomplete_lookup_fields = {
    'fk': ['producto'],}


class LotesAdmin(EsqueletoModelAdmin):
    fieldsets = (
        ('Identificiacion', {
        'fields': ('oproduccion',('fecha','lote'),('analiticas'),('procesos'),),
        }),
        ('Estado', {
            'classes': ('collapse open',),
            'fields' : (('templote', 'carorganolep'),),
            }),

        ('Observaciones', {
            'fields': ('observaciones',),
            }),
        )

    #form    = LotesAdminForm
    inlines = [DetLotesAdmin]
    readonly_fields = ['lote',]
    list_display = ['fecha','lote','oproduccion','procesos','templote','carorganolep',]
    search_fields = ['oproduccion','procesos','lote',]
    list_filter =  ('oproduccion',)

#    def changelist_view( self, request, extra_context = None ):
#        default_filter = False
#        idlote =0
#        try:
#            ref = request.META['HTTP_REFERER']
#            pinfo = request.META['PATH_INFO']
#            qq    = request.META['QUERY_STRING']
#            qstr = ref.split( pinfo )
#            default_filter = True
#            idlote =  qq.split('=')[1]
#
#        except:
#            default_filter = True
#
#        if default_filter:
#            q = request.GET.copy()
#            q['oproduccion__id__exact'] = '%s' % idlote
#            request.GET = q
#            request.META['QUERY_STRING'] = request.GET.urlencode()
#
#        return super( LotesAdmin, self ).changelist_view( request, extra_context = extra_context )

#    class Media:
#        css = { "all": (settings.STATIC_URL+"css/jquery.autocomplete.css",settings.STATIC_URL+"css/iconic.css",settings.STATIC_URL+"css/jquery.ui.dialog.css",settings.STATIC_URL+"css/apprise.css") }
#
#        js  = (settings.STATIC_URL+"js/jquery-1.5.1.min.js",settings.STATIC_URL+"js/dajaxice.core.js",settings.STATIC_URL+"js/jquery-ui-1.8.13.custom.min.js",settings.STATIC_URL+"js/jquery.autocomplete.min.js",settings.STATIC_URL+"js/jquery.dajax.core.js",settings.STATIC_URL+"js/jquery.number_format.js",settings.STATIC_URL+"js/adminlib.js",settings.STATIC_URL+"js/apprise-1.5.full.js")


admin.site.register(Lotes,LotesAdmin)
