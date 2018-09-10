# -*- coding: utf-8 -*-
# __author__ = 'julian'
from maestros_generales.lookups import PaisesLookup, ProvinciasLookup
from maestros_generales.models import TiposImpuestos, TiposTerceros, Paises, Provincias, CodigosPostales, Municipios, Empresas, Marcas, TipoPlanControl, TiposCatProfesional, ZonasFao, TiposDocumentos, Ingredientes, Componentes
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.utils import render_field
from django.forms import TextInput
from django.template import Context
from django.template.loader import render_to_string
from crispy_forms.layout import Submit, Fieldset, Layout, ButtonHolder, HTML, Div, MultiField, Row, Column, Hidden, Button, Field
import floppyforms as forms
from django.forms.models import formset_factory, inlineformset_factory, BaseInlineFormSet, modelformset_factory
from django.utils.translation import gettext_lazy as _
import selectable
from selectable.forms import AutoCompleteWidget,AutoCompleteSelectField
from siva.utils import *




class TiposDocumentosForms(forms.ModelForm):

    html5_required = True

    class Meta:
        model = TiposDocumentos

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tpdocu'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Div( Field('denominacion',css_class="input-xxlarge") ,css_class=s6), Div('abrv', css_class=s6), css_class=s12 ),
                    ),
                FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(TiposDocumentosForms, self).__init__(*args, **kwargs)

    id        = forms.IntegerField(required=False)
    fechaalta = forms.DateField(required=False)




class TiposImpuestosForms(forms.ModelForm):
    class Meta:
        model = TiposImpuestos

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tpimpuestos'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                    Div('id',css_class="control-group hidden"),
                    Div( Div( Field('epigrafe' ),css_class=s6),
                         Div( Field('descripcion',css_class="input-xxlarge" ),css_class=s6),css_class=s12),
                    Div( Div(Field('aplica',css_class="input-large"),css_class=s6), Div('valor',css_class=s6) , css_class=s12),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
            )
        return super(TiposImpuestosForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    fechaalta = forms.DateField(required=False)


class TiposTercerosForms(forms.ModelForm):
    class Meta:
        model = TiposTerceros

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tpterceros'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Div( 'descripcion' ,css_class=s6), Div( 'accion',css_class=s4),css_class=s12),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(TiposTercerosForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    fechaalta = forms.DateField(required=False)


class PaisesForms(forms.ModelForm):
    class Meta:
        model = Paises

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-pais'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                    Div('id',css_class="control-group hidden"),
                    Div( Field('nombre',css_class="input-xxlarge" ),title="Descripción de la Actividad",css_class="control-group"),
                    Div(Div('isonum',css_class=s4),Div('iso2',css_class=s3),Div('iso3',css_class=s3),css_class=s12)
                    ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(PaisesForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)


class ProvinciasForms(forms.ModelForm):
    class Meta:
        model = Provincias

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-provincias'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
                Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Div( Field('codprovincia',css_class="input-xxlarge" ),css_class=s6),Div('nombre',css_class=s6),css_class=s12 ),
                Div( Div('tipo',css_class=s6) , Div('pais',css_class=s6),  css_class=s12),
                FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
                        )
                                    )

        return super(ProvinciasForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    pais = AutoCompleteSelectField(lookup_class=PaisesLookup,required=False)

class CodigosPostalesForms(forms.ModelForm):
    class Meta:
        model = CodigosPostales

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-codigospostales'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Div('codpostal',css_class=s6),Div('provincia',css_class=s6),css_class=s12),
                Div('calle',css_class=s12)
                ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(CodigosPostalesForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    provincia =  AutoCompleteSelectField(lookup_class=ProvinciasLookup,required=False)



class MunicipiosForms(forms.ModelForm):

    html5_required = True

    class Meta:
        model = Municipios

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-municipios'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Div( Field('municipio',css_class="input-xxlarge") ,css_class=s6), Div('provincia', css_class=s6), css_class=s12 ),
                    ),
                FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(MunicipiosForms, self).__init__(*args, **kwargs)

    id        = forms.IntegerField(required=False)
    provincia = AutoCompleteSelectField(lookup_class=ProvinciasLookup,required=False)




class EmpresasForms(forms.ModelForm):
    class Meta:
        model = Empresas

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-empresas'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Field('descripcion',css_class="input-xxlarge" ),css_class="control-group"),css_class=s12 ),
                FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(EmpresasForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)



class MarcasForms(forms.ModelForm):
    class Meta:
        model = Marcas

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-marcas'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Field('descripcion',css_class="input-xxlarge" ),css_class=s12),
                ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(MarcasForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)




class TipoPlanControlForms(forms.ModelForm):
    class Meta:
        model = TipoPlanControl

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tpplancontrol'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Field('denominacion',css_class="input-xxlarge" ), css_class=s12),
                Div(Div('campoprimario',css_class=s4),Div('habilitaregistros',css_class=s4),Div('habilitanaliticas', css_class=s4),css_class=s12)
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(TipoPlanControlForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)



class TiposCatProfesionalForms(forms.ModelForm):
    class Meta:
        model = TiposCatProfesional

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tpcatprofesional'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Div(Field('denominacion',css_class="input-xxlarge" ),css_class=s6),Div(Field('grupo',css_class=xlarge),css_class=s6),css_class=s12 )),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(TiposCatProfesionalForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)


class ZonasFaoForms(forms.ModelForm):
    class Meta:
        model = ZonasFao

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-zonasfao'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Div(Field('denominacion',css_class=xlarge ),css_class=s6),Div('zonasmaritimas',css_class=s6),css_class=s12 ),
                Div( 'url_zona',css_class=s12)),

            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(ZonasFaoForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)


class IngredientesForms(forms.ModelForm):
    class Meta:
        model = Ingredientes

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-ingredientes'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Field('nombre',css_class="input-xxlarge"),  css_class=s12),
                Div(Field('nombingles',css_class="input-xxlarge"),  css_class=s12),
                Div(Field('nombcientifico',css_class="input-xxlarge"),  css_class=s12),


            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(IngredientesForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)



class ComponentesForms(forms.ModelForm):
    class Meta:
        model = Componentes

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-componentes'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
               Div(Div(Field('denominacion',css_class="input-xlarge"),css_class=s6),Div(Field('tipocompo',css_class="input-xlarge"),css_class=s6),  css_class=s12),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(ComponentesForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)