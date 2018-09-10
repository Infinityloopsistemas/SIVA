# -*- coding: utf-8 -*-
from maestros.lookups import UnidadesLookup
from maestros_generales.lookups import MarcasLookup, IngredientesLookup
from productos.lookups import GruposLookup, FamiliasLookup, TiposLookup, CanalLookup, DimensionesLookup, DenominacionLookup, TiposEnvasesLookup
from productos.models import Canales, Grupos, Tipos, Familias, Denominacion, TiposEnvases, Productos, Composicion, Dimensiones, Ingredientes

__author__ = 'julian'
from crispy_forms.bootstrap import FormActions, PrependedAppendedText, AppendedText
from crispy_forms.helper import FormHelper
from crispy_forms.utils import render_field
from django.forms import TextInput
from django.template import Context
from django.template.loader import render_to_string
from crispy_forms.layout import Submit, Fieldset, Layout, ButtonHolder, HTML, Div, MultiField, Row, Column, Hidden, Button, Field
import floppyforms as forms
from django.forms.models import formset_factory, inlineformset_factory, BaseInlineFormSet, modelformset_factory
import selectable
from selectable.forms import AutoCompleteWidget,AutoCompleteSelectField
from django.utils.translation import gettext_lazy as _
from siva.utils import *


class CanalesForms(forms.ModelForm):
    class Meta:
        model = Canales

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-canales'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Field('denominacion',css_class="input-xxlarge"),  css_class=s12),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(CanalesForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)



class GruposForms(forms.ModelForm):
    class Meta:
        model = Grupos

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-grupos'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Field('denominacion',css_class="input-xxlarge"),  css_class=s12),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(GruposForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)



class TiposForms(forms.ModelForm):
    class Meta:
        model = Tipos

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tipos'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Field('denominacion',css_class="input-xxlarge"),  css_class=s12),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(TiposForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)


class FamiliasForms(forms.ModelForm):
    class Meta:
        model = Familias

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-familias'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Field('denominacion',css_class=xxlarge),  css_class=s12),
                Div(Field('grupos',css_class=xlarge),css_class=s12),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(FamiliasForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    grupos = AutoCompleteSelectField(lookup_class=GruposLookup,required=True,help_text=_("Autoseleccion"))




class DenominacionForms(forms.ModelForm):
    class Meta:
        model = Denominacion

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-denomina'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Field('familias',css_class=xxlarge),  css_class=s12),
                Div(Field('denominacion',css_class=xxlarge),  css_class=s12),
                Div(Field('dcientifico',css_class=xxlarge),  css_class=s12),
                Div(Field('url'),css_class=s12),
                Div(Field('descripcion',template=editor),css_class=s12)

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(DenominacionForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    familias = AutoCompleteSelectField(lookup_class=FamiliasLookup,required=True,help_text=_("Autoseleccion"))


class TiposEnvasesForms(forms.ModelForm):
    class Meta:
        model = TiposEnvases

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tiposenvases'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Field('denominacion',css_class=xxlarge),  css_class=s12),
                Div( Div('f_master',css_class=s3),Div('peso_ud',css_class=s3),Div('peso_envase',css_class=s3),Div('agranel',css_class=s3) , css_class=s12),
                Div( Div('volumen',css_class=s4),Div('unidadesporpalet',css_class=s4),Div('filasporpalet',css_class=s4), css_class=s12),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(TiposEnvasesForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)


class DimensionesForms(forms.ModelForm):
    class Meta:
        model = Dimensiones

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-dimensiones'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Field('denominacion',css_class=xxlarge),  css_class=s12),
                Div(Div(Field('unidades',css_class=mini),css_class=s3),Div(Field('maximo',css_class=mini),css_class=s3 ) ,Div(Field('minimo',css_class=mini),css_class=s3),Div(Field('piezas',css_class=mini),css_class=s3) ,  css_class=s12),
                Div(Div(Field('alto',css_class=mini),css_class=s4),Div(Field('largo',css_class=mini),css_class=s4),Div(Field('ancho',css_class=mini),css_class=s4),  css_class=s12),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(DimensionesForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    unidades = AutoCompleteSelectField(lookup_class=UnidadesLookup,required=True,help_text=_("Autoseleccion"))


class ProductosForms(forms.ModelForm):
    #Validar codigos Ean entrada sobre todo digito de control
    class Meta:
        model = Productos

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-productos'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Div(Field('denomina',css_class=xxlarge),css_class=s6),Div(Field('elaborado',css_class=mini),css_class=s6),css_class=s12),
                Div(Div(Field('tipo',css_class=xlarge),css_class=s4),Div(Field('envase',css_class=xlarge),css_class=s4 ) ,Div(Field('dimension'),css_class=s4),css_class=s12),
                Div(Div(Field('canal'),css_class=s4),Div(Field('marca'),css_class=s4),Div(Field('regsanitario'),css_class=s4),  css_class=s12),
                Div(Div(Field("codeancaja",css_class=xlarge),css_class=s6),Div(Field("codeanproducto",css_class=xlarge),css_class=s6),css_class=s12)

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(ProductosForms, self).__init__(*args, **kwargs)

    id                = forms.IntegerField(required=False)
    denomina      = AutoCompleteSelectField(lookup_class=DenominacionLookup,required=True,help_text=_("Autoseleccion"))
    tipo              = AutoCompleteSelectField(lookup_class=TiposLookup,required=True,help_text=_("Autoseleccion"))
    envase            = AutoCompleteSelectField(lookup_class=TiposEnvasesLookup,required=True,help_text=_("Autoseleccion"))
    canal             = AutoCompleteSelectField(lookup_class=CanalLookup,required=True,help_text=_("Autoseleccion"))
    dimension         = AutoCompleteSelectField(lookup_class=DimensionesLookup,required=True,help_text=_("Autoseleccion"))
    marca             = AutoCompleteSelectField(lookup_class=MarcasLookup,required=True,help_text=_("Autoseleccion"))



class ComposicionForms(forms.ModelForm):
    class Meta:
            model = Composicion

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TR( Field('id',css_class="control-group hidden"),
                TD(Field('ingredientes',css_class="control-ingredientes", template="form/field.html")),
                TD(Field('cantidad',css_class="control-group",template="form/field.html")),
                TD(Field('DELETE',template="form/field.html")), css_class="form-row inline compo" ) ,

    )
        return super(ComposicionForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    ingredientes = AutoCompleteSelectField(lookup_class=IngredientesLookup,required=False, allow_new=False,help_text=_("Autoselección"))




def get_composicion_formset(form, formset=BaseInlineFormSet, **kwargs):
    return inlineformset_factory(Productos, Composicion, form, formset,can_delete=True,extra=5)

ComposicionFormset=get_composicion_formset(ComposicionForms,extra=1, can_delete=True )



