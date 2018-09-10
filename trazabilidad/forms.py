# -*- coding: utf-8 -*-
from selectable.forms import AutoCompleteWidget,AutoCompleteSelectField
from appcc.lookups import CuadrosGestionLookup
from maestros.lookups import ZonasLookup, TercerosLookup
#from trazabilidad.lookups import TiposUbicacionLookup, CuadernosCamposLookup, SeriesLotesLookup, ExistenciasLotesLookup
from trazabilidad.models import  Albaran, Documentos, Lotes, DetalleAlbaran,\
    StockActual
from crispy_forms.bootstrap import FormActions, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Fieldset, Layout, Div, Button, Field
from django.utils.translation import gettext_lazy as _
from django.forms.models import  inlineformset_factory, BaseInlineFormSet,\
    modelformset_factory
from siva.utils import *
import floppyforms as forms
from django.contrib.admin import widgets
from maestros_generales.models import TiposDocumentos

import autocomplete_light
from django.forms.formsets import formset_factory
from productos.models import Productos

__author__ = 'julian'


class AlbaranEntradaForms(autocomplete_light.ModelForm):
    class Meta:
        model = Albaran
        exclude = ('user','fechaalta')
 
    def __init__(self,*args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset( Field('id'),
                Div( Div( 'tpdoc',css_class=s4), Div(Field('referencia')), css_class=s12),
                Div( Field( 'proveedor',css_class=s12), css_class=s12),
                Div(Field('fecha',template=fecha),css_class=s12),
                Div( Field('observaciones',template=editor),css_class=s12)
 
         ),
            #FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        super(AlbaranEntradaForms, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs['placeholder'] = 'dd/mm/aaaa'
        self.fields['tpdoc'].widget.attrs['readonly'] = 'readonly'
    tpdoc = forms.ModelChoiceField(widget=forms.Select() ,queryset=TiposDocumentos.objects.filter(abrv="ALBIN"),initial=0)
    proveedor = autocomplete_light.ModelChoiceField('TercerosAutocompleteProveedoresTerceros')
    
#     def save(self, commit=True, request=None,*args, **kwargs):
#         self.user         = request.user
#         self.fechaalta = datetime.datetime.now()
#         instance =super(AlbaranEntradaForms,self).save(commit=False)
#         if commit:
#             instance.save()
#         return instance

class AlbaranSalidaForms(forms.ModelForm):
    class Meta:
        model = Albaran
        exclude = ('user','fechaalta')
 
    def __init__(self,*args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset( Field('id'),
                Div( Div( 'tpdoc',css_class=s4), Div(Field('referencia')), css_class=s12),
                Div( Field( 'proveedor',css_class=s12), css_class=s12),
                Div(Field('fecha',template=fecha),css_class=s12),
                Div( Field('observaciones',template=editor),css_class=s12)
 
         ),
            #FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        super(AlbaranSalidaForms, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs['placeholder'] = 'dd/mm/aaaa'
        self.fields['tpdoc'].widget.attrs['readonly'] = 'readonly'
        self.fields['proveedor'].required = False
        self.fields['proveedor'].label = "Cliente"
    tpdoc = forms.ModelChoiceField(widget=forms.Select() ,queryset=TiposDocumentos.objects.filter(abrv="ALBOUT"),initial=0)
    proveedor = autocomplete_light.ModelChoiceField('TercerosAutocompleteClientesTerceros')
    
#     def save(self, commit=True, request=None,*args, **kwargs):
#         self.user         = request.user
#         self.fechaalta = datetime.datetime.now()
#         instance =super(AlbaranSalidaForms,self).save(commit=False)
#         instance.user = self.user
#         if commit:
#             instance.save()
#         return instance
class LotesForms(autocomplete_light.ModelForm):
    class Meta:
        model = Lotes
        exclude = ('user','fechaalta') #Excluir para saltar la validacion en el Form
 
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-lotes'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),                
                Div(Div(Field('referencia',css_class=small),css_class=s4), Div(Field('fechacaducidad',template=fecha,css_class=small),css_class=s4),css_class=s12),
                Div(Div(Field('producto',css_class=xxlarge),css_class=s12),css_class=s12),
                Div(Div(Field('templote',css_class=xlarge),css_class=s6),Div(Field('carorganolep',css_class=xlarge),css_class=s6),css_class=s12),
                Div(Div(Field('cantidad',css_class=small),css_class=s3),Div(Field('pesobulto',css_class=small),css_class=s3),Div(Field('peso',css_class=small),css_class=s3),Div(Field('volumen',css_class=small),css_class=s3),css_class=s12,css_id="data-agrupa"),
                Div(Field('observaciones',template=editor),css_class=s12)
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        super(LotesForms, self).__init__(*args, **kwargs)
        
 
    def save(self, commit=True, request=None,*args, **kwargs):
        instance =super(LotesForms,self).save(commit=False)
        instance.user_id      = request.user.id
        instance.empresa      = Empresas.objects.get(usuario=request.user)
        instance.fechaalta    = datetime.datetime.today()
        if commit:
            instance.save()
        return instance
 
 
class DetalleAlbaranEntradaForms(autocomplete_light.ModelForm):
    class Meta:
        model = DetalleAlbaran
        exclude = ('user','fechaalta')
 
    def __init__(self, *args, **kwargs):
        prefijo="detalbaran"
#         self.helper = FormHelper()
#         self.helper.form_tag = False
#         self.helper.layout = Layout(
#             TR( Field('id',css_class="control-group hidden"),
#                 TD(Field('producto' ,css_class=mini,template="form/field.html")),
#                 TD(Field('lote'   ,css_class=mini,template="form/field.html")),
#                 TD(Field('referencia',css_class=mini,template="form/field.html")),                
#                 TD(Div(Field('cantidad',css_class=mini,template="form/field.html")),Div(Field('pesobulto',css_class=mini,template="form/field.html"))),
#                 #TD(Field('pesobulto',css_class=mini,template="form/field.html")),
#                 TD(Field('peso'     ,css_class=mini,template="form/field.html")),
#                 TD(Field('volumen'  ,css_class=mini,template="form/field.html")),
#                 TD(Field('DELETE'   ,template="form/field.html")), css_class="form-row inline %s" % prefijo ) ,#cambiar por el prefijo
#  
#         )
        super(DetalleAlbaranEntradaForms, self).__init__(*args, **kwargs)
        self.fields['cantidad'].widget.attrs['class'] = 'span8'
        self.fields['peso'].widget.attrs['class'] = 'span8'
        self.fields['pesobulto'].widget.attrs['class'] = 'span8'
        self.fields['volumen'].widget.attrs['class'] = 'span8'
 
 
 
 
    id         = forms.IntegerField(required=False)
    lote = autocomplete_light.ModelChoiceField('LotesAutocompleteLotesEntDetAlb')
    producto = autocomplete_light.ModelChoiceField('ProductosAutocompleteProductosEntrada')
 
 
def get_detallealbaranentrada_formset(form, formset=BaseInlineFormSet, *args,**kwargs):
 
    return inlineformset_factory(Albaran, DetalleAlbaran, form, formset,can_delete=True,extra=1)
 
DetalleAlbaranEntradaFormset=get_detallealbaranentrada_formset(DetalleAlbaranEntradaForms,extra=1, can_delete=True )

class DetalleAlbaranSalidaForms(autocomplete_light.ModelForm):
    class Meta:
        model = DetalleAlbaran
        exclude = ('user','fechaalta')
 
    def __init__(self, *args, **kwargs):
        prefijo="detalbaran"
#         self.helper = FormHelper()
#         self.helper.form_tag = False
#         self.helper.layout = Layout(
#             TR( Field('id',css_class="control-group hidden"),
#                 TD(Field('producto' ,css_class=mini,template="form/field.html")),
#                 TD(Field('lote'   ,css_class=mini,template="form/field.html")),
#                 TD(Field('referencia',css_class=mini,template="form/field.html")),                
#                 TD(Div(Field('cantidad',css_class=mini,template="form/field.html")),Div(Field('pesobulto',css_class=mini,template="form/field.html"))),
#                 #TD(Field('pesobulto',css_class=mini,template="form/field.html")),
#                 TD(Field('peso'     ,css_class=mini,template="form/field.html")),
#                 TD(Field('volumen'  ,css_class=mini,template="form/field.html")),
#                 TD(Field('DELETE'   ,template="form/field.html")), css_class="form-row inline %s" % prefijo ) ,#cambiar por el prefijo
#  
#         )
        super(DetalleAlbaranSalidaForms, self).__init__(*args, **kwargs)
        self.fields['cantidad'].widget.attrs['class'] = 'span8'
        self.fields['peso'].widget.attrs['class'] = 'span8'
        self.fields['pesobulto'].widget.attrs['class'] = 'span8'
        self.fields['volumen'].widget.attrs['class'] = 'span8'
 
 
 
 
    id         = forms.IntegerField(required=False)
    lote = autocomplete_light.ModelChoiceField('LotesAutocompleteLotesSalida')
    
#     def save(self, commit=True, request=None,*args, **kwargs):
#         instance =super(DetalleAlbaranSalidaForms,self).save(commit=False)
#         instance.user_id      = request.user.id
#         instance.empresa      = Empresas.objects.get(usuario=request.user)
#         instance.fechaalta    = datetime.datetime.today()
#         if commit:
#             instance.save()
#         return instance
 
 
def get_detallealbaransalida_formset(form, formset=BaseInlineFormSet, *args,**kwargs):
 
    return inlineformset_factory(Albaran, DetalleAlbaran, form, formset,can_delete=True,extra=1)
 
DetalleAlbaranSalidaFormset=get_detallealbaransalida_formset(DetalleAlbaranSalidaForms,extra=1, can_delete=True )



class DocumentosForms(forms.ModelForm):
    class Meta:
        model = Documentos
        exclude = ('user','fechaalta','nodescargas',)

    def __init__(self, *args, **kwargs):
        prefijo="documentos"
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TR( Field('id',css_class="control-group hidden",template=campo),
                Field('albaran_id',css_class="control-group hidden", template=campo),
                Field('lotes_id',css_class="control-group hidden",template=campo),
                TD(Field('fecha',css_class="control-group", template="form/field_date_table.html")),
                TD(Field('denominacion',css_class="control-group", template="form/field.html")),
                TD(Field('archivos',css_class="control-group", template="form/field.html")),
                TD(Field('DELETE',template="form/field.html")), css_class="form-row inline %s" % prefijo ) ,#cambiar por el prefijo

        )
        super(DocumentosForms, self).__init__(*args, **kwargs)


    id            = forms.IntegerField(required=False)
    albaran_id    = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    lotes_id      = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))





def get_doc_formset(padre,form, formset=BaseInlineFormSet, **kwargs):
    return inlineformset_factory(padre, Documentos, form, formset,can_delete=True,extra=1)

AlbaranDocFormset           = get_doc_formset(Albaran,DocumentosForms, extra=5)
LotesDocFormset             = get_doc_formset(Lotes,DocumentosForms, extra=5)


class ConsultaExistenciasForm(forms.Form):
    def __init__(self, *args, **kwargs):
        prefijo="detexistencias"
        super(ConsultaExistenciasForm, self).__init__(*args, **kwargs)

    lote = autocomplete_light.ModelChoiceField('LotesAutocompleteLotesEntrada',required=False)
    producto = autocomplete_light.ModelChoiceField('ProductosAutocompleteProductosStock', required=False)
    

class ConsultaExistenciaLotesProductoForm(forms.ModelForm):
    class Meta:
        model = Lotes
        exclude = ('user','fechaalta','fechabaja','cantidad','empresa','fechacaducidad','templote','templote',
                   'carorganolep','observaciones','peso','volumen','pesobulto','producto') #Excluir para saltar la validacion en el Form
        #exclude = ('user','fechaalta') #Excluir para saltar la validacion en el Form
    def __init__(self, *args, **kwargs):
        prefijo = "detexistenciaslotesproductos"
        super(ConsultaExistenciaLotesProductoForm, self).__init__(*args, **kwargs)
        initial = kwargs['initial']
        id =  initial.get('id')
        lote = Lotes.objects.get(pk=id)
        stock = StockActual.objects.get(id=id)
        self.reflote = lote.referencia
        self.fechacad = pasarFechaTextoEsp(lote.fechacaducidad)
        if stock.peso == None:
            self.cantidad = ("%s unidades") % stock.cant
            self.peso = ""
        else:
            self.peso = ("%s Kg.") % stock.peso
            self.cantidad = ""


    reflote = forms.CharField
    cantidad = forms.CharField
    peso = forms.CharField
    fechacad = forms.CharField

LotesFormset = formset_factory(ConsultaExistenciaLotesProductoForm,extra=0)

class ConsultaExistenciaLotesDetAlbForm(forms.ModelForm):
    class Meta:
        model = DetalleAlbaran
        exclude = ('user','fechaalta','empresa','fechabaja','peso','volumen','pesobulto','producto','cantidad','referencia','lote','albaran')
    def __init__(self, *args, **kwargs):
        prefijo = "detexistenciaslotesdetalbsal"
        super(ConsultaExistenciaLotesDetAlbForm, self).__init__(*args, **kwargs)
        initial = kwargs['initial']
        print initial
        id =  initial.get('id')
        print id
        detalb = DetalleAlbaran.objects.get(pk=id)
        print detalb
        self.reflote = detalb.referencia
        self.albaran = detalb.albaran.referencia
        self.proveedor = detalb.albaran.proveedor
        self.fechacad = pasarFechaTextoEsp(detalb.lote.fechacaducidad)
        if detalb.peso == None:
            self.stock = ("%s unidades") % detalb.cantidad
        else:
            self.stock = ("%s Kg.") % detalb.peso
    reflote = forms.CharField
    stock = forms.CharField
    albaran = forms.CharField
    fechacad = forms.CharField
    proveedor = forms.CharField


LotesDetAlbFormset = formset_factory(ConsultaExistenciaLotesDetAlbForm,extra=0)
