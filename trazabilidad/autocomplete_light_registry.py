'''
Created on 24/3/2015
 
@author: Claudio
'''
import autocomplete_light
from trazabilidad.models import Lotes, StockActual
from productos.models import Productos
from django.db.models import Q
from maestros.models import Terceros
from context_processors.empresa import nombre_empresa
 
# autocomplete_light.register(Lotes,
#                             name="LotesEnt",
#                             search_fields=['referencia'],
#                             attrs={
#                                    'placeholder': 'Introduzca lote 1',                            
#                                    'data-autocomplete-minimum-characters': 0,
#                                    },
#                             choices=Lotes.objects.all())
# autocomplete_light.register(Lotes,
#                             name="LotesSalida",
#                             search_fields=['referencia'],
#                             attrs={
#                                    'placeholder': 'Introduzca lote 2',                            
#                                    'data-autocomplete-minimum-characters': 0,
#                                    },
#                             choices=Lotes.objects.all())
 
# autocomplete_light.register(Productos,
#                             search_fields=['denomina'],
#                             attrs={
#                                    'placeholder': 'Introduzca producto',
#                                    'data-autocomplete-minimum-characters': 0,
#                                    },
#                             choices=Productos.objects.all())

class AutocompleteProveedoresTerceros(autocomplete_light.AutocompleteModelBase):
    search_fields=['denominacion'],
    name = 'Proveedores',
    attrs={'placeholder': 'Introduzca proveedor',
           'data-autocomplete-minimum-characters': 0,
           }
    
    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        empresa = nombre_empresa(self.request)
        choices = Terceros.objects.filter(tipotercero__descripcion = "PROVEEDORES",empresa = empresa['nombre_empresa'])
        if q:
            choices = choices.filter(denominacion__icontains=q)
        return choices

autocomplete_light.register(Terceros, AutocompleteProveedoresTerceros)
class AutocompleteClientesTerceros(autocomplete_light.AutocompleteModelBase):
    search_fields=['denominacion'],
    name = 'Clientes',
    attrs={'placeholder': 'Introduzca Cliente',
           'data-autocomplete-minimum-characters': 0,
           }
    
    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        empresa = nombre_empresa(self.request)
        choices = Terceros.objects.filter(tipotercero__descripcion = "CLIENTES",empresa = empresa['nombre_empresa'])
        if q:
            choices = choices.filter(denominacion__icontains=q)
        return choices

autocomplete_light.register(Terceros, AutocompleteClientesTerceros)
 
class AutocompleteProductosEntrada(autocomplete_light.AutocompleteModelBase):
    name = 'ProductosEntrada'
    attrs={'placeholder': 'Introduzca Producto Entrada ..',
                                'data-autocomplete-minimum-characters': 0,
                                }
 
    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        lote = self.request.GET.get('lotes', None)
        empresa = nombre_empresa(self.request)
 
        choices = self.choices.filter(empresa = empresa['nombre_empresa'])
         
        if lote:
            choices = choices.filter(lotes=lote)
        if q:
            choices = choices.filter(denomina__icontains=q)
 
        return self.order_choices(choices)[0:self.limit_choices]
 
autocomplete_light.register(Productos, AutocompleteProductosEntrada)
 
class AutocompleteLotesSalida(autocomplete_light.AutocompleteModelBase):
    name = 'LotesSalida'
    attrs={'placeholder': 'Introduzca Lote',
                                'data-autocomplete-minimum-characters': 0,
                                }
 
    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        producto = self.request.GET.get('producto', None)
 
        empresa = nombre_empresa(self.request)
 
        choices = self.choices.filter(empresa = empresa['nombre_empresa'])
        # Obtengo el stock actual
        stock = StockActual.objects.filter(Q(peso__gt = 0)|Q(cant__gt = 0)).values_list('id')
        objectStock = choices.in_bulk(stock)
        keys = objectStock.keys()
 
        # Filtro los lotes si tienen stock
        choices = choices.filter(pk__in=keys)
         
        if producto:
            choices = choices.filter(producto=producto)
        if q:
            choices = choices.filter(Q(producto__denomina__icontains=q) | Q(referencia__icontains=q))
 
        return self.order_choices(choices)[0:self.limit_choices]
 
autocomplete_light.register(Lotes, AutocompleteLotesSalida)
 
class AutocompleteLotesEntrada(autocomplete_light.AutocompleteModelBase):
    name="LotesEntrada"
    search_fields=['referencia']
    attrs={'placeholder': 'Introduzca lote',                            
           'data-autocomplete-minimum-characters': 0,
        }
    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        empresa = nombre_empresa(self.request)
 
        choices = Lotes.objects.filter(empresa = empresa['nombre_empresa'])
        # Obtengo el stock actual
        stock = StockActual.objects.filter(Q(peso__gt = 0)|Q(cant__gt = 0)).values_list('id')
        objectStock = choices.in_bulk(stock)
        keys = objectStock.keys()
 
        # Filtro los lotes si tienen stock
        choices = choices.filter(pk__in=keys)
        if q:
            choices = choices.filter(Q(producto__denomina__icontains=q) | Q(referencia__icontains=q))
        return choices
 
 
autocomplete_light.register(Lotes, AutocompleteLotesEntrada)
 
class AutocompleteLotesEntDetAlb(autocomplete_light.AutocompleteModelBase):
    name="LotesEntDetAlb"
    search_fields=['referencia']
    attrs={'placeholder': 'Introduzca lote',                            
           'data-autocomplete-minimum-characters': 0,
        }
    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        empresa = nombre_empresa(self.request)
 
        choices = Lotes.objects.filter(empresa = empresa['nombre_empresa'])
        if q:
            choices = choices.filter(Q(producto__denomina__icontains=q) | Q(referencia__icontains=q))
        return choices
 
 
autocomplete_light.register(Lotes, AutocompleteLotesEntDetAlb)
 
class AutocompleteProductosStock(autocomplete_light.AutocompleteModelBase):
    name="ProductosStock"
    search_fields=['denomina']
    attrs={'placeholder': 'Introduzca producto',                            
           'data-autocomplete-minimum-characters': 0,
        }
    
    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        empresa = nombre_empresa(self.request)
 
        lotes = Lotes.objects.filter(empresa = empresa['nombre_empresa'])
            # Obtengo el stock actual
        stock = StockActual.objects.filter(Q(peso__gt = 0)|Q(cant__gt = 0)).values_list('id')
        objectStock = lotes.in_bulk(stock)
        keys = objectStock.keys()
     
            # Filtro los lotes si tienen stock
        productos = Productos.objects.filter(empresa = empresa['nombre_empresa'])
        lotes = lotes.filter(pk__in=keys)
        product_ids = lotes.values_list('producto')
        productosStock = productos.in_bulk(product_ids)
        keyspro = productosStock.keys()
        choices = productos.filter(pk__in=keyspro)
        if q:
            choices = choices.filter(denomina__icontains=q)        
        
        return choices
     
 
 
autocomplete_light.register(Productos, AutocompleteProductosStock)