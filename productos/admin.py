# from utils import *
# from productos.models import *
# __author__ = 'julian'
#
#
# class VistaProductosAdmin(EsqueletoModelAdmin):
#
#     list_fields=['producto']
#     search_fields =['producto']
#     list_filter=['producto']
#
#
#
# admin.site.register(Vista_Productos,VistaProductosAdmin)
#
#
#
# class ProductosAdmin(EsqueletoModelAdmin):
#     fieldsets = (
#         (None, {
#             'fields': (('especie' ,'tipo'), ('dimension','envase' ),('codigo_barra','canal'), ('elaborado','marca'), ('estado','fecha_baja'))
#         }),
#         )
#     list_fields=['especie','tipo','dimension','envase']
#     search_fields =['especie__descripcion','tipo__descripcion','canal__descripcion']
#     list_filter=['especie','tipo','canal']
#     raw_id_fields=('especie','tipo','dimension','envase')
#     autocomplete_lookup_fields = {
#             'fk': ['especie','tipo','dimension','envase'],}
#
#
# admin.site.register(Productos,ProductosAdmin)
# admin.site.register(Grupos)
#
# class EspeciesAdmin(EsqueletoModelAdmin):
#     fieldsets = (
#         (None, {
#             'fields': (('familia_familia' ,'p_arancela_p_arancela'), 'descripcion','dcientifico','denglish','dfrench','ditalian','dspanish','dotros' )
#         }),
#         )
#     valid_lookups=('familia_familia')
#     list_fields=['descripcion','familia_familia']
#     raw_id_fields = ('familia_familia','p_arancela_p_arancela',)
#     autocomplete_lookup_fields = {
#                 'fk': ['familia_familia','p_arancela_p_arcancela'] }
#     search_fields =['descripcion']
#     list_filter=['familia_familia',]
#
#
# admin.site.register(Especies,EspeciesAdmin)
#
#
#
# class FamiliasAdmin(EsqueletoModelAdmin):
#     list_fields=['descripcion']
#     search_fields =['descripcion']
#
# admin.site.register(Familias,FamiliasAdmin)
#
#
# class TiposAdmin(EsqueletoModelAdmin):
#     list_fields=['descripcion']
#     search_fields =['descripcion']
#
# admin.site.register(Tipos,TiposAdmin)
#
# class DimensionesAdmin(EsqueletoModelAdmin):
#     list_fields=['descripcion']
#     search_fields =['descripcion']
#
# admin.site.register(Dimensiones,DimensionesAdmin)
#
#
# class TiposEnvasesAdmin(EsqueletoModelAdmin):
#     list_fields=['descripcion']
#     search_fields =['descripcion']
#
# admin.site.register(TiposEnvases,TiposEnvasesAdmin)
#
#
# class MarcasAdmin(EsqueletoModelAdmin):
#     list_fields=['descripcion']
#     search_fields =['descripcion']
#
# admin.site.register(Marcas,MarcasAdmin)