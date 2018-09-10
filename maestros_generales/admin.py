# -*- coding: utf-8 -*-
from maestros_generales.models import CodigosPostales, TiposImpuestos, TiposTerceros, Municipios, Paises, Provincias, Empresas, Marcas, TipoPlanControl,EmpresasEdit,\
    MetaUsuarios, Festivos
from siva.utils import EsqueletoModelAdmin
from django.contrib import admin

__author__ = 'julian'

autusua=1

class TiposImpuestosAdmin(EsqueletoModelAdmin):
    exclude =('fechaalta',)
    search_fields=['descripcion']
    def save_model(self,request,obj,form,change):
        if autusua==1:
            obj.user = request.user
            obj.save()


admin.site.register(TiposImpuestos,TiposImpuestosAdmin)



class TipoTerceroAdmin(EsqueletoModelAdmin):

    exclude =('fechaalta',)
    search_fields=['descripcion']




admin.site.register(TiposTerceros,TipoTerceroAdmin)



class PaisesAdmin(EsqueletoModelAdmin):
    list_display = ['nombre','isonum','iso2','iso3']
    search_fields=['nombre']
    ordering = ['nombre']




class CodigosPostalesInline(admin.TabularInline):
    model = CodigosPostales


class CodigosPostalesAdmin(EsqueletoModelAdmin):
    extra = 0
    list_per_page=10
    raw_id_fields = ('provincia',)
    related_lookup_fields = {
        'fk': ['provincia'],
        }
    list_display  = ('codpostal','calle',)
    search_fields = ('codpostal','calle',)




class ProvinciasAdmin(EsqueletoModelAdmin):
    list_display =['codprovincia','nombre','tipo','pais']
    fieldsets = (
        (None, {
            'fields': (('codprovincia' ,'nombre'), ('tipo','pais' ))
        }),
        )
    search_fields = ['nombre']
    list_filter = ['pais']
    inlines =[CodigosPostalesInline]
    raw_id_fields = ('pais',)
    autocomplete_lookup_fields = {
        'fk': ['pais'],
        }



class MunicipiosAdmin(EsqueletoModelAdmin):
    list_display =['municipio','provincia']
    fieldsets = (
        (None, {
            'fields': (('municipio' ,'provincia'),)
        }),
        )
    search_fields = ['municipio']
    list_filter = ['provincia']
    raw_id_fields = ('provincia',)
    autocomplete_lookup_fields = {
        'fk': ['provincia'],
        }

class TiposPlanControlAdmin(EsqueletoModelAdmin):
    list_display =['denominacion']
    fieldsets = (
        (None, {
            'fields': ('denominacion' ,('habilitaregistros','habilitanaliticas'),'etiquetas',)
        }),
        )



class EmpresasAdmin(EsqueletoModelAdmin):

    list_display =['denominacion','habilitar','fechaalta','fechabaja','entrarEmpresa','verRegistrosEmpresas']
    search_fields = ['descripcion']

    def get_queryset(self, request):
                qs = super(EmpresasAdmin, self).queryset(request)
#                 if request.user.is_superuser or request.user.username=='LOZANO':
#                         return qs
                return qs.filter(usuario__username__contains=request.user,fechabaja__isnull=True)

    def __init__(self, *args, **kwargs):
        super(EmpresasAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )
        
class EmpresasEditAdmin(EmpresasAdmin):
    filter_horizontal = ('usuario','festivo',)
    def __init__(self, *args, **kwargs):
        super(EmpresasAdmin, self).__init__(*args, **kwargs)
        #self.list_display_links = (None, )
        
class MetaUsuariosAdmin(EsqueletoModelAdmin):
    filter_horizontal = ('usuario',)
    
    
admin.site.register(TipoPlanControl,TiposPlanControlAdmin)
admin.site.register(Municipios,MunicipiosAdmin)
admin.site.register(Paises,PaisesAdmin)
admin.site.register(Provincias,ProvinciasAdmin)
admin.site.register(CodigosPostales,CodigosPostalesAdmin)

admin.site.register(Empresas,EmpresasAdmin)
admin.site.register(EmpresasEdit,EmpresasEditAdmin)
admin.site.register(Marcas)
admin.site.register(MetaUsuarios,MetaUsuariosAdmin)
admin.site.register(Festivos)