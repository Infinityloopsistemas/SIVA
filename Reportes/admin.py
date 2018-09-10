from django.contrib import admin
from reportes.models import Informes, DetalleInformes
from siva.utils import EsqueletoModelAdmin

__author__ = 'julian'

class DInformesAdmin(admin.TabularInline):
    model = DetalleInformes
    fieldsets = (
                    ('Detalle', {
                            'fields': ( 'nombetiqueta','nombparametro','tipoparametro','mostrar','modelo','query_modelo' )
                            }
                     ),)

class InformesAdmin(EsqueletoModelAdmin):
    inlines=[DInformesAdmin]
    list_display = ('descripcion','Impresion','fecha','tpplancontrol')
    search_fields = ['descripcion']
    list_filter = ('tpplancontrol',)
#    def save_model(self,request,obj,form,change):
#            if request.user=="julian":
#                obj.save()


admin.site.register(Informes, InformesAdmin)



