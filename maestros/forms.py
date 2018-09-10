# -*- coding: utf-8 -*-
# __author__ = 'julian'
from django.contrib.auth.models import User
from maestros.lookups import ZonasLookup, TiposTemperaturasLookup, TiposLegislacionLookup, UnidadesLookup, FirmasLookup, PersonalLookup
from maestros.models import Actividades, CatalogoEquipos, Unidades, TiposTemperaturas, Zonas, Terceros, Personal, ParametrosAnalisis, TiposMedidasActuacion, TiposMedidasVigilancia, TiposLimitesCriticos, Consumibles, ConsumiEspecificaciones, TiposFrecuencias, Documentos, Etapas, Peligros, TiposLegislacion, TiposCursos, TiposProcesos, TiposTurnos, HorarioTurnos, Firmas
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
from maestros_generales.lookups import MarcasLookup, ProvinciasLookup, PaisesLookup, MunicipiosLookup, CodigoPostalLookup, TpCatProfesionalLookup
from siva.utils import *



class TercerosForms(forms.ModelForm):
    class Meta:
        model = Terceros

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-terceros'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                    Div('id',css_class="control-group hidden"),
                    Div( Div( Field('tipotercero' ),css_class=s4),
                         Div( Field('denominacion',css_class="input-xxlarge" ),css_class=s4),css_class=s12),
                    Div( Div('cif',css_class=s4), Div('registrosani', css_class=s4), Div('telefono', css_class=s4), css_class=s12),
                    Div( Div(Field('direccion1',css_class="input-large"),css_class=s4), Div('direccion2',css_class=s4) ,Div('municipio',css_class=s4), css_class=s12),
                    Div( Div('provincia',css_class=s4),Div('codpostal',css_class=s4),Div('pais' ,css_class=s4),css_class=s12),
                    Div( Div('percontacto' ,css_class=s4),  Div('email',css_class=s4), Div( 'paginaweb',css_class=s4) ,css_class=s12),
                    Div(Field('fechabaja',template=fecha,css_class=s6),css_class=s4),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
            )
        return super(TercerosForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    provincia = AutoCompleteSelectField(lookup_class=ProvinciasLookup,help_text=_("Autoselección"))
    pais      = AutoCompleteSelectField(lookup_class=PaisesLookup,required=True,help_text=_("Autoselección"))
    municipio = AutoCompleteSelectField(lookup_class=MunicipiosLookup,required=True,help_text=_("Autoselección"))
    codpostal = AutoCompleteSelectField(lookup_class=CodigoPostalLookup ,required=True, label=_("Codigo Postal"),help_text=_("Autoselección"))



class PersonalForms(forms.ModelForm):
    class Meta:
        model = Personal

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-personal'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Div( 'dni' ,css_class=s4), Div( 'apellidos',css_class=s4), Div('nombres',css_class=s4),css_class=s12),
                Div( Div('estadocivil',css_class=s4), Div(Field('fechanacimiento',template="form/field_date.html"), css_class=s4, ), Div('sexo', css_class=s4), css_class=s12),
                Div( Div('nss',css_class=s4), Div('cargo',css_class=s4) ,Div('catprofesional',css_class=s4) ,css_class="span12"),
                Div( Div( Field('email'), css_class=s4 ),Div(Field('emailnotifica'),css_class=s4), Div(Field('telefonosms'),css_class=s4),css_class=s12),
                Div(Field('fechabaja',template=fecha,css_class=s6),css_class=s4),
                Div ( Field('observaciones', template=editor), css_class=s12),
                Div('fileImagen',css_class=s12)
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(PersonalForms, self).__init__(*args, **kwargs)
    def save(self, commit=True, user=None,*args, **kwargs):

        self.user      = user
        instance =super(PersonalForms,self).save(commit=False)
        if commit:
            instance.save(user)
        return instance
    id = forms.IntegerField(required=False)
    catprofesional =  AutoCompleteSelectField(lookup_class=TpCatProfesionalLookup ,required=True, label=_("Cat. Profesional"),help_text=_("Autoselección"))
    fileImagen = forms.FileField(label="Firma",required=False)

    id = forms.IntegerField(required=False)
    catprofesional =  AutoCompleteSelectField(lookup_class=TpCatProfesionalLookup ,required=True, label=_("Cat. Profesional"),help_text=_("Autoselección"))

class FirmasForms(forms.ModelForm):
    class Meta:
        model = Firmas

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-firmas'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Div(Field('personal',css_class="input-xlarge"),  css_class=s6),
                Div(Field('fecha',template=fecha),css_class=s6),css_class=s12),
                Div(Field('fechabaja',template=fecha,css_class=s6),css_class=s4),
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )

        return super(FirmasForms, self).__init__(*args, **kwargs)


    id = forms.IntegerField(required=False)
    personal = AutoCompleteSelectField(lookup_class=PersonalLookup ,required=True, label=_("Personal"),help_text=_("Autoselección"))


class EtapasForms(forms.ModelForm):
    class Meta:
        model = Etapas

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-etapas'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Field('denominacion',css_class="input-xxlarge"),  css_class=s12),
                Div(Field('ayuda',template=editor),css_class=s12),
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(EtapasForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)


class PeligrosForms(forms.ModelForm):
    class Meta:
        model = Peligros

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-peligros'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Field('denominacion',css_class="input-xxlarge"),  css_class=s12),
                Div(Field('ayuda',template=editor),css_class=s12),
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(PeligrosForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)


class ActividadesForms(forms.ModelForm):
    class Meta:
        model = Actividades

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-actividades'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                    Div('id',css_class="control-group hidden"),
                    Div( Div(Field('denominacion',css_class="input-xxlarge" ),css_class=s4),Div("tipo",css_class=s4),Div("agenda",css_class=s4),css_class=s12),
                    Div( Div(Field('colortxt', template="form/field_color.html"), css_class=s6), Div(Field('colorback', template="form/field_color.html"), css_class=s6),css_class=s12)
                    ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(ActividadesForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)



class UnidadesForms(forms.ModelForm):
    class Meta:
        model = Unidades

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-actividades'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Field('denominacion',css_class="input-xxlarge" ),css_class=s12)),

            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(UnidadesForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)

class TiposLegislacionForms(forms.ModelForm):
    class Meta:
        model = TiposLegislacion

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-actividades'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Field('denominacion',css_class="input-xxlarge" ),css_class=s12),
                Div( Field('contenido',template=editor),css_class=s12) ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar")
        ))
        return super(TiposLegislacionForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)

class TiposCursosForms(forms.ModelForm):
    class Meta:
        model = TiposCursos

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-actividades'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Div( Field('denominacion',css_class=xlarge ),css_class=s6),Div(Field('legislacion',css_class=xlarge),css_class=s6),css_class=s12),
                Div(Field('contenido',template=editor),css_class=s12),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        ))
        return super(TiposCursosForms, self).__init__(*args, **kwargs)

    id             = forms.IntegerField(required=False)
    legislacion    = AutoCompleteSelectField(lookup_class=TiposLegislacionLookup,required=True,help_text=_("Autoselección"))


class ParametrosAnalisisForms(forms.ModelForm):
    class Meta:
        model = ParametrosAnalisis

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-parametrosanalisis'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div('tipo',css_class=s12),
                Div ( Div('denominacion',css_class=s6), Div('unidades',css_class=s6),css_class=s12)
                ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(ParametrosAnalisisForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    unidades = AutoCompleteSelectField(lookup_class=UnidadesLookup,required=True,help_text=_("Autoselección"))

class CatalogoEquiposForms(forms.ModelForm):

    html5_required = True

    class Meta:
        model = CatalogoEquipos

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-catequipo'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(
                Div( Field('denominacion',css_class=xlarge ), title=_("Nombre del Equipo"),css_class=s4),Div(Field('tipo',title=_("Tipos de Equipos")),css_class=s4),
                Div( Field('noserie',css_class="input-large"),css_class=s4),
                css_class="span12"),
                Div( Div('marcas', css_class="span3"),
                 Div( Field('fadquirir',template=fecha) ,css_class="span3"),
                 Div( Field('finstala',template=fecha) ,css_class="span3"),
                 Div('modelo' ,css_class="span3"),
                css_class="span12"),
            Div(Field('caracteristicas',template=editor),css_class=s12 )
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(CatalogoEquiposForms, self).__init__(*args, **kwargs)

    id     = forms.IntegerField(required=False)
    marcas = AutoCompleteSelectField(lookup_class = MarcasLookup,required=False,help_text=_("Autoselección"))




class TiposTemperaturasForms(forms.ModelForm):
    class Meta:
        model = TiposTemperaturas

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tipostemperaturas'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Field('denominacion',css_class="input-xxlarge" ),css_class="control-group"),
                Div( Div('tmax',css_class="span6") , Div('tmin', css_class="span6" ), css_class="span12" ),
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(TiposTemperaturasForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)



class ZonasForms(forms.ModelForm):
    class Meta:
        model = Zonas

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-zonas'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Field('denominacion',css_class="input-xxlarge" ),css_class="span12"),
                Div ( Div('superficie',css_class="span6"), Div('tipotemp',css_class="span6" ), css_class="span12"),
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(ZonasForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    tipotemp = AutoCompleteSelectField(lookup_class=TiposTemperaturasLookup,required=True, label="Tipos Temperatura",help_text=_("Autoselección"))




class TiposMedidasActuacionForms(forms.ModelForm):
    class Meta:
        model = TiposMedidasActuacion

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tpmedidasactuacion'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Div( Field('denominacion',css_class="input-xxlarge" ),css_class=s6), Div('tipo',css_class=s6), css_class=s12),
                Div(Field('ayuda',template=editor),css_class=s12),
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(TiposMedidasActuacionForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)


class TiposMedidasVigilanciaForms(forms.ModelForm):
    class Meta:
        model = TiposMedidasVigilancia

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tpmedidasvigilancia'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Field('denominacion',css_class="input-xxlarge" ), css_class=s12),
                Div(Field('ayuda',template=editor) ,css_class=s12),
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(TiposMedidasVigilanciaForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)


class TiposLimitesCriticosForms(forms.ModelForm):
    class Meta:
        model = TiposLimitesCriticos

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tplimitescriticos'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Div( Field('denominacion',css_class="input-xxlarge" ),css_class=s6), Div('unidades',css_class=s6), css_class=s12),
                Div(Div( 'valormin', css_class=s6) , Div('valormax',css_class=s6), css_class=s12),
                Div(Field('ayuda',template=editor),css_class=s12),
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(TiposLimitesCriticosForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    unidades = AutoCompleteSelectField(lookup_class=UnidadesLookup,required=True,help_text=_("Autoselección"))




class ConsumiblesForms(forms.ModelForm):
    class Meta:
        model = Consumibles

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset( Field('id'),
                Div( Div( Field('denominacion',css_class="input-xxlarge" ),css_class=s6), Div('tipo',css_class=s6), css_class=s12)
                )

        )
        return super(ConsumiblesForms, self).__init__(*args, **kwargs)



# Añadir al formset can_delete=True y en CAMPO DELETE

class ConsumiEspecificacionesForms(forms.ModelForm):
    class Meta:
        model = ConsumiEspecificaciones

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TR( Field('id',css_class="control-group hidden"),
                    TD(Field('descripcion',css_class="control-group", template="form/field.html")),TD(Field('DELETE',template="form/field.html")), css_class="form-row inline conespeci" ) ,

        )

        return super(ConsumiEspecificacionesForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField()

#Definimos el formset para manipular a nivel de campo

def get_consumibles_formset(form, formset=BaseInlineFormSet, **kwargs):
    return inlineformset_factory(Consumibles, ConsumiEspecificaciones, form, formset,can_delete=True,extra=1)

ConsumEspeciFormset=get_consumibles_formset(ConsumiEspecificacionesForms,extra=1, can_delete=True )



class TiposFrecuenciasForms(forms.ModelForm):
    class Meta:
        model = TiposFrecuencias

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tpmedidasactuacion'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div(Div( Field('denominacion',css_class="input-xlarge" ),css_class=s6), Div(Field('nounidades',css_class=mini),css_class=s6), css_class=s12),
                Div(Div('diaslaborables',css_class=s12),css_class=s12),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(TiposFrecuenciasForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)



class TiposProcesosForms(forms.ModelForm):
    class Meta:
        model = TiposProcesos

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tpprocesos'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div( Field('denominacion',css_class="input-xxlarge"),css_class=s12),
                Div(Div( Field('pesado', css_class=mini ), css_class=s4 ), Div(Field('etiquetado',css_class=mini), css_class=s4), Div('nivel',css_class=s4),css_class=s12),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(TiposProcesosForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)






class TiposTurnosForms(forms.ModelForm):
    class Meta:
        model = TiposTurnos

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset( Field('id'),
                Div( Field('denominacion',css_class="input-xxlarge" ),css_class=s12)
                )

        )
        return super(TiposTurnosForms, self).__init__(*args, **kwargs)



# Añadir al formset can_delete=True y en CAMPO DELETE

class HorariosTurnosForms(forms.ModelForm):
    class Meta:
        model = HorarioTurnos

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TR( Field('id',css_class="control-group hidden"),
                    TD(Field('ihora',css_class="control-group", template="form/field.html")),
                    TD(Field('fhora',css_class="control-group", template="form/field.html")),
                    TD(Field('DELETE',template="form/field.html")), css_class="form-row inline horariostur" ) ,

        )

        return super(HorariosTurnosForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField()

#Definimos el formset para manipular a nivel de campo

def get_tiposturnos_formset(form, formset=BaseInlineFormSet, **kwargs):
    return inlineformset_factory(TiposTurnos, HorarioTurnos, form, formset,can_delete=True,extra=3)

HorarioTurnosFormset=get_tiposturnos_formset(HorariosTurnosForms,extra=3, can_delete=True )




class DocumentosForms(forms.ModelForm):
    class Meta:
        model = Documentos
        exclude = ('user','fechaalta')

    def __init__(self, *args, **kwargs):
        prefijo="documentos"
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TR( Field('id',css_class="control-group hidden",template=campo),
                Field('terceros_id',css_class="control-group hidden",template=campo),
                Field('personal_id',css_class="control-group hidden", template=campo),
                Field('zonas_id',css_class="control-group hidden",template=campo),
                Field('catequipos_id',css_class="control-group hidden",template=campo),
                Field('consumibles_id',css_class="control-group hidden",template=campo),
                TD(Field('fecha',css_class="control-group", template="form/field_date_table.html")),
                TD(Field('denominacion',css_class="control-group", template="form/field.html")),
                TD(Field('archivos',css_class="control-group", template="form/field.html")),
                TD(Field('DELETE',template="form/field.html")), css_class="form-row inline %s" % prefijo ) ,#cambiar por el prefijo

        )
        super(DocumentosForms, self).__init__(*args, **kwargs)


    id                = forms.IntegerField(required=False)
    terceros_id       = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    personal_id       = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    catequipos_id     = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    zonas_id         = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    consumibles_id         = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))





def get_doc_formset(padre,form, formset=BaseInlineFormSet, **kwargs):
    return inlineformset_factory(padre, Documentos, form, formset,can_delete=True,extra=1)

TercerosDocFormset = get_doc_formset(Terceros,DocumentosForms, extra=5)
PersonalDocFormset = get_doc_formset(Personal,DocumentosForms, extra=5)
ZonasDocFormset = get_doc_formset(Zonas,DocumentosForms, extra=5)
CatEquiposDocFormset = get_doc_formset(CatalogoEquipos,DocumentosForms, extra=5)
ConsumiblesDocFormset = get_doc_formset(Consumibles,DocumentosForms, extra=5)

