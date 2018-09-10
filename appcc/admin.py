# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from appcc.models import DetallesRegistros, CabRegistros, HistorialRevisiones, APPCC, ManualAutoControl, PlanAutoControl, ValoresAnaliticas, ConsumiblesDosis, DetalleConfiguracion, Configuracion, Registros
from maestros.models import Personal, Terceros, TiposTurnos
from maestros_generales.models import Empresas
from siva.utils import EsqueletoModelAdmin

__author__ = 'julian'


class APPCGenerales(EsqueletoModelAdmin):

    exclude = ['user','empresa']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save(request.user)

    def get_queryset(self, request):
        qs = super(APPCGenerales,self).queryset(request)
        return qs.filter( empresa__in=Empresas.objects.filter(usuario=request.user) )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name =='operador':
            kwargs["queryset"] = Terceros.objects.filter(empresa__in=Empresas.objects.filter(usuario=request.user))


        return super(APPCGenerales, self).formfield_for_foreignkey(db_field, request, **kwargs)



class DetRegistrosAdmin(admin.TabularInline):
    model = DetallesRegistros

    fieldsets=(('Detalles Registros',{'fields': ( 'actividades','zonas','equipos','tplimitcrit' ) }),)
    raw_id_fields = ['actividades','zonas','equipos']



class CabRegistrosAdmin(APPCGenerales):

    fieldsets=(('Registros',{'fields':( ( 'fecha','manautctrl',),('tpmedvig','frecuencia' , 'tpmedactc')) }),)

    inlines = [DetRegistrosAdmin]
    list_display = ['fecha','manautctrl','tpmedvig']
    raw_id_fields = ['manautctrl','tpmedvig','frecuencia','tpmedactc']

admin.site.register(CabRegistros,CabRegistrosAdmin)



class RegistrosAdmin(EsqueletoModelAdmin):

    exclude = ['user','empresa']


    def get_queryset(self, request):
        qs = super(RegistrosAdmin,self).queryset(request)
        return qs.filter( detreg__empresa__in=Empresas.objects.filter(usuario=request.user) )

    fieldsets=(('Registros',{'fields':( ('fechadesde','fechahasta',),('valor','estado' ,'observaciones','horarioturno','firmas'))  }),)

    list_display = ['denominacion','fechadesde','fechahasta','valor','estado','observaciones']
    raw_id_fields = ['horarioturno','firmas']

    search_fields= ['detreg__id']


class DetHistorialRevisiones(admin.TabularInline):
    model = HistorialRevisiones




class APPCAdmin(APPCGenerales):
    inlines = [DetHistorialRevisiones]
    fieldsets=(('Definicion APPC',{'fields':( ( 'fechaedicion','denominacion',),) }),)
    list_display = ['fechaedicion','denominacion']

admin.site.register(APPCC,APPCAdmin)

class ValoresAnaliticasAdmin(admin.TabularInline):
    model= ValoresAnaliticas
    fieldsets=(('Valores Analiticas',{ 'classes': ('grp-collapse grp-closed',),'fields':(  'paramanali','valores') }),)
    raw_id_fields = ['paramanali']


class ConsumiblesDosisAdmin(admin.TabularInline):
    model= ConsumiblesDosis
    fieldsets=(('Dosis Conumibles',{ 'classes': ('grp-collapse grp-closed',),'fields':(  'consumible','dosis') }),)
    raw_id_fields = ['consumible']


class ManualAutoControlAdmin(APPCGenerales):
    fieldsets = (
        ('Apartados', {
            'fields': ('appcc', 'tpplancontrol', ),
            }),
        ('Objeto', {
            'classes': ('grp-collapse grp-open',),
            'fields' : ('objeto',),
            }),
        ('Alcance', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('alcance',),
            }),
        ('Contenido', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('contenido',),
            }),
        ('Marco Legal', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('marcolegal',),
            }),
        ('Procedimiento', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('procedimiento',),
            }),

    )

    inlines = [ValoresAnaliticasAdmin]
    raw_id_fields = ['appcc','tpplancontrol',]
    list_display =  ['appcc','tpplancontrol',]


admin.site.register(ManualAutoControl,ManualAutoControlAdmin)





class PlanAutoControlAdmin(APPCGenerales):
    fieldsets = (
        ('Manual', {
            'fields': (('manautctrl','fecha','frecuencia') ),
            }),
        ('Zonas', {
            'classes': ('grp-collapse grp-open',),
            'fields' : ('zonas','zonalimpieza'),
            }),
        ('Mantenedor', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('tercero',('equipos','personal'),'operaciones',),
            }),
        ('Medidas', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('tpmedvig','tpmedactp','tpmedactc'),
            }),
        ('Observaciones', {
            'classes': ('grp-collapse grp-closed',),
            'fields' : ('observaciones',),
            }),

        )
    inlines = [ConsumiblesDosisAdmin]
    raw_id_fields = ['manautctrl','frecuencia','zonas','tercero','equipos','personal','tpmedvig','tpmedactp','tpmedactc']
    list_display = ['manautctrl','fecha','zonas']


admin.site.register(PlanAutoControl,PlanAutoControlAdmin)


class DetalleConfiguracionAdmin(admin.TabularInline):
    model = DetalleConfiguracion

    fieldsets=(('Detalle Configurar',{'fields': ('personas','registros','accion','habilitar','dias','turnos')}),)


    def formfield_for_manytomany(self, db_field, request=None, **kwargs):

        if db_field.name =='personas':
            kwargs["queryset"] = Personal.objects.filter(empresa__in=Empresas.objects.filter(usuario=request.user))

        if db_field.name =='registros':
            kwargs["queryset"] = CabRegistros.objects.filter(empresa__in=Empresas.objects.filter(usuario=request.user))

        return super(DetalleConfiguracionAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        if db_field.name =='turnos':
            kwargs["queryset"] = TiposTurnos.objects.filter(empresa__in=Empresas.objects.filter(usuario=request.user))

        return super(DetalleConfiguracionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class ConfiguracionAdmin(APPCGenerales):
    fieldsets=(('Configurar',{'fields': ('operador','activar')}),)

    inlines = [DetalleConfiguracionAdmin]
    list_display = ['operador','activar']
    raw_id_fields = ['operador']



admin.site.register(Configuracion,ConfiguracionAdmin)
admin.site.register(Registros,RegistrosAdmin)

#class ProLimpiezaAdmin(ModelAdmin):
#    fieldsets=(('Procedimiento',{'fields':( ( 'planautctrl','descripcion',),'parent',) }),)
#
#    list_display = ['planautctrl','descripcion','parent']
#
#    raw_id_fields = ['planautctrl']
#
#
#admin.site.register(ProcedimientosLimpieza,ProLimpiezaAdmin)


