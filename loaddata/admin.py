# -*- coding: utf-8 -*-
from loaddata.models import LoadDataDevice, TrackTemperaturas, TrackSondas
from maestros.models import Zonas
from maestros_generales.models import Empresas

__author__ = 'julian'
from siva.utils import EsqueletoModelAdmin
from django.contrib import admin



class LoadDataDeviceAdmin(EsqueletoModelAdmin):
    # fieldsets = (
    #     (None, {
    #         'fields': (('serie' ,'descripcion'),)
    #     }),
    #     )

    list_display = ['HostName','DeviceName','PollCount','temperaturas']
    search_fields = ['HostName']

class TrackSondasAdmin(admin.TabularInline):
    model= TrackSondas



class TrackTemperaturasAdmin(EsqueletoModelAdmin):
    inlines  =[TrackSondasAdmin]

    fieldsets = (
       (None, {
             'fields': (('DeviceName' ,'HostName'),('MACAddress','zonas'), ('fechabaja'), )
        }),
         )


    list_display =['DeviceName','HostName','MACAddress','zonas','numeroSondas']
    search_fields = ['DeviceName']

    def get_queryset(self, request):
            qs = super(TrackTemperaturasAdmin, self).queryset(request)
            return qs.filter(empresa__in=Empresas.objects.filter(usuario=request.user))

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name =='zonas':
            kwargs["queryset"] = Zonas.objects.filter(empresa__in=Empresas.objects.filter(usuario=request.user))
        return super(TrackTemperaturasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.user    = request.user
        obj.empresa=  Empresas.objects.filter(usuario=request.user)[0]
        obj.save()

admin.site.register( LoadDataDevice, LoadDataDeviceAdmin)

admin.site.register(TrackTemperaturas,TrackTemperaturasAdmin)
