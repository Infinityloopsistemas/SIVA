# -*- coding: utf-8 -*-
import selectable
from loaddata.models import TrackTemperaturas, TrackSondas
from maestros.models import TiposTurnos, Firmas, HorarioTurnos, Personal
from productos.lookups import ProductosLookup
#from trazabilidad.lookups import LotesLookup
from imagen.models import Imagen
from django.forms.widgets import Textarea, TextInput
#from rest_waspmote.models import WaspSensor

__author__ = 'julian'
from selectable.forms import AutoCompleteWidget,AutoCompleteSelectField, AutoComboboxSelectWidget
from appcc.lookups import CabRegistrosLookup, ParametrosAnalisiANALookup, CuadrosGestionLookup, TrackTemperaturasLookup
from maestros.lookups import TPActuacionPrevLookup, TercerosLookup, TiposFrecuenciasLookup, ZonasLookup, CatalogoEquiposLookup, PersonalLookup, TPActuacionCorrLookup, TipoMedidasVigilanciaLookup, TPLimitesCritLookup, ActividadesLookup, ParametrosAnalisisLookup, ConsumiblesLookup, PeligrosLookup, EtapasLookup, TiposCursosLookup, TercerosTiposLookup, FirmasLookup, HorarioTurnoLookup, TiposLegislacionLookup
from django.utils.translation import gettext_lazy as _
from appcc.models import APPCC, HistorialRevisiones, ManualAutoControl, ConsumiblesDosis, ValoresAnaliticas, PlanAutoControl, CabRegistros, Registros, DetallesRegistros, Documentos, CuadrosGestion, RelacionesEntes, GestorIncidencias, CabAnaliticas, DetAnaliticas, CabInformesTecnicos, DetInformesTecnicos
from crispy_forms.bootstrap import FormActions, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Fieldset, Layout, Div, Button, Field
from django.forms.models import  inlineformset_factory, BaseInlineFormSet
from siva.utils import *
import floppyforms as forms
from ckeditor.widgets import CKEditorWidget


DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')
ATTRS = {'data-selectable-options': {'highlightMatch': True, 'minLength': 5}}


class APPCCForms(forms.ModelForm):
    class Meta:
        model = APPCC
        exclude = ('user','fechaalta')

    def __init__(self,*args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset( Field('id'),
                Div( Div( Field('denominacion',css_class="input-xxlarge" ),css_class=s6), Div(Field('fechaedicion',template=fecha),css_class=s6), css_class=s12),
                Div(Field('contenido',template=editor),css_class=s10)
                )

        )
        return super(APPCCForms, self).__init__(*args, **kwargs)

    def save(self, commit=True, request=None,*args, **kwargs):
        self.user         = request.user
        self.fechaalta = datetime.datetime.now()
        instance =super(APPCCForms,self).save(commit=False)
        if commit:
            instance.save()
        return instance

# Añadir al formset can_delete=True y en CAMPO DELETE

class HistorialRevisionesForms(forms.ModelForm):
    class Meta:
        model = HistorialRevisiones
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TR( Field('id',css_class="control-group hidden"),
                    TD(Field('fecharevision',css_class="control-group span2", template="form/field_date_table.html")),TD(Field('DELETE',template="form/field.html")), css_class="form-row inline dappcc" ) ,

        )
        return super(HistorialRevisionesForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField()

#    def clean_fecha(self):
#        v_fecha = self.cleaned_data['fecha']
#        hoyano = v_fecha.year
#        ahora  = datetime.now().year
#        if hoyano != ahora:
#            raise forms.ValidationError("La fecha no coincide con el ejercicio de apertura")
#        return v_fecha




#Definimos el formset para manipular a nivel de campo

def get_appcc_formset(form, formset=BaseInlineFormSet, **kwargs):
    return inlineformset_factory(APPCC, HistorialRevisiones, form, formset,can_delete=True,extra=1)

HistorialRevisionesFormset=get_appcc_formset(HistorialRevisionesForms,extra=1, can_delete=True )



class ManualAutoControlForms(forms.ModelForm):
    class Meta:
        model = ManualAutoControl
        exclude = ('user','fechaalta','appcc') #Excluir para saltar la validacion en el Form

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-tpmedidasactuacion'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div('appcc_id',css_class="control-group hidden"),
                Div(Field('tpplancontrol',css_class="span5"),css_class=s12),
                Div(Field('objeto',template=editor), css_class=s12),
                Div(Field('alcance',template=editor), css_class=s12),
                Div(Field('contenido',template=editor), css_class=s12),
                Div(Field('marcolegal',template=editor), css_class=s12),
                Div(Field('procedimiento',template=editor), css_class=s12),

            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(ManualAutoControlForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    appcc_id = forms.IntegerField(required=False)


    def save(self, commit=True, user=None,*args, **kwargs):
        self.user      = user
        self.fechaalta = datetime.datetime.now()
        instance =super(ManualAutoControlForms,self).save(commit=False)
        if commit:
            instance.save()
        return instance



class ConsumiblesDosisForms(forms.ModelForm):
    class Meta:
        model = ConsumiblesDosis
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TR( Field('id',css_class="control-group hidden"),
                TD(Field('consumible',css_class="control-group", template="form/field.html")),
                TD(Field('dosis',css_class="control-group", template="form/field.html")),
                TD(Field('DELETE',template="form/field.html")), css_class="form-row inline dcd" ) ,

        )
        return super(ConsumiblesDosisForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    consumible = AutoCompleteSelectField(lookup_class=ConsumiblesLookup,required=False, allow_new=False,help_text=_("Autoseleccion"))


class ValoresAnaliticasForms(forms.ModelForm):
    class Meta:
        model = ValoresAnaliticas
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TR( Field('id',css_class="control-group hidden"),
                TD(Field('paramanali',css_class="control-group analitica", template="form/field.html")),
                TD(Field('valores',css_class="control-group",template="form/field.html")),
                TD(Field('tolerancia',css_class="control-group",template="form/field.html")),
                TD(Field('DELETE',template="form/field.html")), css_class="form-row inline dva" ) ,

    )
        return super(ValoresAnaliticasForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    paramanali = AutoCompleteSelectField(lookup_class=ParametrosAnalisisLookup,required=False, allow_new=False)




def get_consudosis_formset(form, formset=BaseInlineFormSet, **kwargs):
    return inlineformset_factory(PlanAutoControl, ConsumiblesDosis, form, formset,can_delete=True,extra=1)

ConsumiblesDosisFormset=get_consudosis_formset(ConsumiblesDosisForms,extra=1, can_delete=True )



def get_valornalitica_formset(form, formset=BaseInlineFormSet, **kwargs):
    #return inlineformset_factory(PlanAutoControl, ValoresAnaliticas, form, formset,can_delete=True,extra=1)
    return inlineformset_factory(ManualAutoControl, ValoresAnaliticas, form, formset,can_delete=True,extra=1)

ValoresAnaliticasFormset=get_valornalitica_formset(ValoresAnaliticasForms,extra=1, can_delete=True )


class campoFecha(forms.DateInput):
    template_name = 'form/textfield_floppyforms.html'

    def get_context(self, name, value, attrs):
        ctx = super(campoFecha, self).get_context(name, value, attrs)
        ctx['attrs']['class'] = 'textarea span10'
        return ctx

class TextareaAncha(forms.Textarea):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs.setdefault('cols', 100)
        attrs.setdefault('rows', 10)
        super(TextareaAncha, self).__init__(*args, **kwargs)





class PlanAutoControlForms(forms.ModelForm):
    attrs = {'data-selectable-options': {'highlightMatch': True, 'minLength': 5}}
    class Meta:
        model = PlanAutoControl
        exclude = ('user','fechaalta','manautctrl') #Excluir para saltar la validacion en el Form



    #fecha        = forms.DateField(widget=forms.TextInput( attrs={'class' :'grd-white input-small', 'placeholde': "dd/mm/yyyy" ,'data-form': "datepicker"}))
    fecha        = campoFecha()
    frecuencia   = AutoCompleteSelectField(lookup_class=TiposFrecuenciasLookup,required=True,help_text=_("Autoselección"))
    zonas        = AutoCompleteSelectField(lookup_class=ZonasLookup,required=False,help_text=_("Autoselección"))
    zonalimpieza = TextareaAncha()
    proclimpieza = TextareaAncha()
    tercero      = AutoCompleteSelectField(lookup_class=TercerosLookup,required=False,label="Mantenedor",help_text=_("Autoselección"))
    operaciones  = TextareaAncha()
    equipos      = AutoCompleteSelectField(lookup_class=CatalogoEquiposLookup,required=False,help_text=_("Autoselección"))
    productos    = AutoCompleteSelectField(lookup_class=ProductosLookup,required=False,help_text=_("Autoselección"))
    personal     = AutoCompleteSelectField(lookup_class=PersonalLookup,required=False,help_text=_("Autoselección"))
    tpmedactp    = AutoCompleteSelectField(lookup_class=TPActuacionPrevLookup,help_text=_("Autoselección"))
    tpmedactc    = AutoCompleteSelectField(lookup_class=TPActuacionCorrLookup,required=True,help_text=_("Autoselección"))
    tpmedvig     = AutoCompleteSelectField(lookup_class=TipoMedidasVigilanciaLookup,required =True,help_text=_("Autoselección"))
    obervaciones = TextareaAncha()

    id              = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    manautctrl_id   = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))

    def save(self, commit=True, user=None,*args, **kwargs):
        self.user      = user
        self.fechaalta = datetime.datetime.now()
        instance =super(PlanAutoControlForms,self).save(commit=False)
        if commit:
            instance.save()
        return instance



class CabInfTecnicosForms(forms.ModelForm):
    class Meta:
        model = CabInformesTecnicos
        exclude = ('user','fechaalta','appcc')


    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-cabinftec'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div('appcc_id',css_class="control-group hidden"),
                Div( Div( Field('fecha', template=fecha,css_class=small ),css_class=s6),
                     Div( Field('establecimiento',css_class=xlarge ),css_class=s6),css_class=s12),
                Div( Div( Field('expediente', css_class=xlarge),css_class=s6),Div(Field('responsable'), css_class=s6) , css_class=s12),
                Div( Div(Field('auditor',css_class=xlarge),css_class=s6), Div('legislacion',css_class=s6) , css_class=s12),
            ),
        )

        super(CabInfTecnicosForms, self).__init__(*args, **kwargs)


    id               = forms.IntegerField(required=False)
    appcc_id         = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    responsable      = AutoCompleteSelectField(lookup_class=PersonalLookup,required=False,label="Responsable",help_text=_("Autoselección"))
    auditor          = AutoCompleteSelectField(lookup_class=PersonalLookup,required=False, label="Auditor",help_text=_("Autoselección"))
    legislacion      = AutoCompleteSelectField(lookup_class=TiposLegislacionLookup,required=True,help_text=_("Autoselección"))



class DetInfTecnicosForms(forms.ModelForm):
    class Meta:
        model = DetInformesTecnicos
        fields = '__all__'
#         widgets = {
#                    'texto':forms.Textarea(attrs={'data-form':'wysihtml5',
#                                                       'style':'width:95%',
#                                                       #'class':'textarea form-control'
#                                                       })
#         }

    def __init__(self, *args, **kwargs):
        super(DetInfTecnicosForms, self).__init__(*args, **kwargs)        
        prefijo="detinftec"
        self.fields['orden'].widget = TextInput(attrs={'class':'numberinput',
                                                       'type':'number',
                                                       'style':'width:35px;'})
        self.fields['texto'].widget = Textarea(attrs={
                                                      'data-form':'wysihtml5',
                                                      'style':'width:95%',
                                                      #'class':'form-row inline %s' % prefijo
                                                      })
        
        #self.fields['texto'].widget = Textarea(attrs={'data-form':'wysihtml5',
        #                                              'style':'width:95%'})
#         self.helper = FormHelper()
#         self.helper.form_tag = False
#         self.helper.layout = Layout(
#             TR( Field('id',css_class="control-group hidden"),
#                 TD(Field('orden',css_class=mini ,template="form/field.html")),
#                 TD(Field('titulo',css_class=xlarge, template="form/field.html")),
#                 TD(Field('texto',template="form/formset_field_textarea.html")),
#                 TD(Field('fileImagen', template="form/field.html")),
#                 #TD(Field('texto')),
#                 TD(Field('DELETE',template="form/field.html")), css_class="form-row inline %s" % prefijo ) ,#cambiar por el prefijo
#  
#         )
        
    id            = forms.IntegerField(required=False)        
    fileImagen = forms.FileField(label="Imagen",required=False)
    
def get_detinftec_formset(form, formset=BaseInlineFormSet, **kwargs):
    return inlineformset_factory(CabInformesTecnicos, DetInformesTecnicos, form, formset,can_delete=True,extra=1)

DetInfTecnicosFormset=get_detinftec_formset(DetInfTecnicosForms,extra=1, can_delete=True )




class CabRegistrosForms(forms.ModelForm):
    class Meta:
        model = CabRegistros
        exclude = ('user','fechaalta','manautctrl')


    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-cabregistros'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div('manautctrl_id',css_class="control-group hidden"),
                Div( Div( Field('fecha', template=fecha,css_class=small ),css_class=s6),
                     Div( Field('denominacion',css_class=xlarge ),css_class=s6),css_class=s12),
                Div( Field('tpmedvig', css_class=xxlarge), css_class=s12),
                Div( Div(Field('tpmedactc',css_class=xlarge),css_class=s6), Div('frecuencia',css_class=s6) , css_class=s12),
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        return super(CabRegistrosForms, self).__init__(*args, **kwargs)

    id = forms.IntegerField(required=False)
    manautctrl_id   = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    tpmedactc       = AutoCompleteSelectField(lookup_class=TPActuacionCorrLookup,required=False,label="Medida de Actuación Correctoras",help_text=_("Autoselección"))
    tpmedvig        = AutoCompleteSelectField(lookup_class=TipoMedidasVigilanciaLookup,required=False, label="Medida Vigilancia",help_text=_("Autoselección"))
    frecuencia      = AutoCompleteSelectField(lookup_class=TiposFrecuenciasLookup,required=True,help_text=_("Autoselección"))

    def save(self, commit=True, user=None,*args, **kwargs):
        self.user      = user
        self.fechaalta = datetime.datetime.now()
        instance =super(CabRegistrosForms,self).save(commit=False)
        if commit:
            instance.save()
        return instance



class DetallesRegistrosForms(forms.ModelForm):
    #Mostramos la fecha ya que afecta la aparicion de los registros en la agendas
    class Meta:
        model = DetallesRegistros
        exclude = ('user','cabreg')

    def __init__(self, *args, **kwargs):
        idmanctrl= kwargs.pop('idmanctrl')
        usuario  = kwargs.pop('iduser')
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div('cabreg_id',css_class="control-group hidden"),
                Div( Div(Field('actividades'), css_class=s4 ),Div(Field('fechaalta',template=fecha,css_class=small),css_class=s4),Div(Field('tracksondas'),css_class=s4) ,css_class=s12 ),
                    Div( Div('tplimitcrit', css_class=s4),Div('valanali',css_class=s4 ),Div(Field('ordagenda',css_class=mini),css_class=s4 ),css_class=s12 ),
                    Div(Div(Field('equipos',css_class=xlarge),css_class=s4) ,Div(Field('zonas',css_class=xlarge),css_class=s4) ,Div(Field('diaejecuta'),css_class=s4),css_class=s12),
                    Div(Div(Field('tpturnos'),css_class=s6),css_class=s12)
                    #Div(Field('trackwaspsensor'),css_class=s3),css_class=s12),
               ),

        )
        super(DetallesRegistrosForms, self).__init__(*args, **kwargs)
        self.fields['valanali'].widget.update_query_parameters({'manautctrl__manautctrl__id': idmanctrl})
        self.fields['valanali'].label=_("Parametro a Controlar")
        self.fields['tpturnos'].queryset = TiposTurnos.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=usuario) )
        self.fields['tracksondas'].queryset = TrackSondas.objects.filter(tracktemp__empresa__in=Empresas.objects.filter(usuario__username=usuario) )
        #self.fields['trackwaspsensor'].queryset = WaspSensor.objects.filter(empresa__in=Empresas.objects.filter(usuario__username=usuario) )



    id                = forms.IntegerField(required=False)
    cabreg_id         = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    actividades       = AutoCompleteSelectField(lookup_class=ActividadesLookup,required=False,help_text=_("Autoselección"))
    zonas             = AutoCompleteSelectField(lookup_class=ZonasLookup,required=False,help_text=_("Autoselección"))
    equipos           = AutoCompleteSelectField(lookup_class=CatalogoEquiposLookup,required=False,help_text=_("Autoselección"))
    valanali          = AutoCompleteSelectField(lookup_class=ParametrosAnalisiANALookup,required=False,help_text=_("Autoselección"))
    tplimitcrit       = AutoCompleteSelectField(lookup_class=TPLimitesCritLookup,required=False,label="Limite Critico",help_text=_("Autoselección"))




    def save(self, commit=True, user=None,*args, **kwargs):
        self.user      = user
        #self.fechaalta = datetime.datetime.now()
        instance =super(DetallesRegistrosForms,self).save(commit=False)
        if commit:
            instance.save()
        return instance


class RegistrosForms(forms.ModelForm):
    class Meta:
        model = Registros
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        prefijo="registro"
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TR( Field('id',css_class="control-group hidden"),
                TD(Field('fechadesde',css_class=small ,template="form/field_date_table.html")),
                TD(Field('valor',css_class=mini, template="form/field.html")),
                TD(Field('estado',css_class="control-group",template="form/field.html")),
                TD(Field('firmas',css_class=medium,template="form/field.html")),
                TD(Field('observaciones',css_class=medium,template="form/field.html")),
                TD(Field('horarioturno',css_class=small,template="form/field.html")),
                TD(Field('DELETE',template="form/field.html")), css_class="form-row inline %s" % prefijo ) ,#cambiar por el prefijo

        )

        super(RegistrosForms, self).__init__(*args, **kwargs)

    id            = forms.IntegerField(required=False)
    firmas        = AutoCompleteSelectField(lookup_class=FirmasLookup ,widget=AutoComboboxSelectWidget ,required=False, label=_("Firmas"),help_text=_("Autoselección"))
    horarioturno  = AutoCompleteSelectField(lookup_class=HorarioTurnoLookup , widget=AutoComboboxSelectWidget,required=True, help_text=_("Autoselección"))

def get_registro_formset(form, formset=BaseInlineFormSet, **kwargs):
    return inlineformset_factory(DetallesRegistros, Registros, form, formset,can_delete=True,extra=5)

RegistrosFormset=get_registro_formset(RegistrosForms,extra=1, can_delete=True )




class CabAnaliticasForms(forms.ModelForm):
    class Meta:
        model = CabAnaliticas
        exclude = ('user','fechaalta','cabreg')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id  ="form_analiticas"
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div('cabreg_id',css_class="control-group hidden"),
                Div( Div(Field('denominacion'), css_class=s6 ),Div(Field('fecha', template=fecha ), css_class=s6),css_class=s12 ),
                Div(Div(Field('cuadgestion',css_class=xlarge),css_class=s4) , Div(Field('laboratorio'),css_class=s4) ,Div(Field('lotes'),css_class=s4), css_class=s12),
                Div(Field('observaciones',template=editor),css_class=s12)
               ),

        )
        super(CabAnaliticasForms, self).__init__(*args, **kwargs)



    id                = forms.IntegerField(required=False)
    cabreg_id         = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cuadgestion       = AutoCompleteSelectField(lookup_class=CuadrosGestionLookup,required=True,help_text=_("Autoselección"))
    laboratorio       = AutoCompleteSelectField(lookup_class=TercerosLookup,required=True,help_text=_("Autoselección"))
    #lotes             = AutoCompleteSelectField(lookup_class=LotesLookup,required=False,help_text=_("Autoselección"))


    def save(self, commit=True, user=None,*args, **kwargs):
        self.user      = user
        self.fechaalta = datetime.datetime.now()
        instance =super(CabAnaliticasForms,self).save(commit=False)
        if commit:
            instance.save()
        return instance





class DetAnaliticasForms(forms.ModelForm):
    class Meta:
        model = DetAnaliticas
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        prefijo="detanaliticas"
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TR( Field('id',css_class="control-group hidden"),
                TD(Field('parametros',css_class=xlarge,template="form/field.html")),
                TD(Field('valores',css_class="mini", template="form/field.html")),
                TD(Field('DELETE',template="form/field.html")), css_class="form-row inline %s" % prefijo ) ,#cambiar por el prefijo
        )
        super(DetAnaliticasForms, self).__init__(*args, **kwargs)

    id               = forms.IntegerField(required=False)
    parametros       = AutoCompleteSelectField(help_text=_("Autoselección"),lookup_class=ParametrosAnalisisLookup,required=False, allow_new=False)

def get_detanalisis_formset(form, formset=BaseInlineFormSet, **kwargs):
    return inlineformset_factory(CabAnaliticas, DetAnaliticas, form, formset,can_delete=True,extra=5)

DetAnaliticasFormset=get_detanalisis_formset(DetAnaliticasForms,extra=1, can_delete=True )


class UploadForm(forms.Form):
    id                = forms.IntegerField(required=False)
    appcc_id          = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    manautctrl_id     = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    planautoctrl_id   = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cabreg_id         = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    detreg_id         = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    registros_id      = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cuadgest_id       = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    relentes_id       = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    gestincid_id      = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cabanali_id       = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cabinftec_id      = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    fecha             = forms.DateField(initial=datetime.date.today,required=False)
    denominacion      = forms.CharField(max_length="200",required=False)    
    archivos          = forms.FileField(label='Selecciona un archivo',required=False)
    contenido         = forms.CharField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))


class DocumentosUploadForm(forms.ModelForm):    
    class Meta:
        model = Documentos
        exclude = ('user','fechaalta')

    def __init__(self, *args, **kwargs):
        prefijo="documentos"
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TR( Field('id',css_class="control-group hidden",template=campo),
                Field('appcc_id',css_class="control-group hidden",template=campo),
                Field('manautctrl_id',css_class="control-group hidden", template=campo),
                Field('planautoctrl_id',css_class="control-group hidden",template=campo),
                Field('cabreg_id',css_class="control-group hidden",template=campo),
                Field('detreg_id',css_class="control-group hidden",template=campo),
                Field('registros_id',css_class="control-group hidden",template=campo),
                Field('cuadgest_id',css_class="control-group hidden",template=campo),
                Field('relentes_id',css_class="control-group hidden",template=campo),
                Field('gestincid_id',css_class="control-group hidden",template=campo),
                Field('cabanali_id',css_class="control-group hidden",template=campo),
                Field('cabinftec_id',css_class="control-group hidden",template=campo),
                #TD(Field('fecha',css_class="control-group hidden", template="form/field_date_table.html")),
                #TD(Field('denominacion',css_class="control-group", template="form/field.html")),
                #TD(Field('archivos',css_class="control-group", template="form/field.html")),
                #TD(Field('DELETE',template="form/field.html")), 
                css_class="form-row inline %s" % prefijo ) ,#cambiar por el prefijo
 
        )
        super(DocumentosUploadForm, self).__init__(*args, **kwargs)


    id                = forms.IntegerField(required=False)
    appcc_id          = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    manautctrl_id     = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    planautoctrl_id   = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cabreg_id         = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    detreg_id         = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    registros_id      = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cuadgest_id       = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    relentes_id       = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    gestincid_id      = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cabanali_id       = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cabinftec_id      = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    fecha             = forms.DateField(initial=datetime.date.today,required=False)
    denominacion      = forms.CharField(max_length="200",required=False)    
    archivos          = forms.FileField(label='Selecciona un archivo',required=False)



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
                Field('appcc_id',css_class="control-group hidden",template=campo),
                Field('manautctrl_id',css_class="control-group hidden", template=campo),
                Field('planautoctrl_id',css_class="control-group hidden",template=campo),
                Field('cabreg_id',css_class="control-group hidden",template=campo),
                Field('detreg_id',css_class="control-group hidden",template=campo),
                Field('registros_id',css_class="control-group hidden",template=campo),
                Field('cuadgest_id',css_class="control-group hidden",template=campo),
                Field('relentes_id',css_class="control-group hidden",template=campo),
                Field('gestincid_id',css_class="control-group hidden",template=campo),
                Field('cabanali_id',css_class="control-group hidden",template=campo),
                Field('cabinftec_id',css_class="control-group hidden",template=campo),
                TD(Field('fecha',css_class="control-group", template="form/field_date_table.html")),
                TD(Field('denominacion',css_class="control-group", template="form/field.html")),
                TD(Field('archivos',css_class="control-group", template="form/field.html")),
                TD(Field('DELETE',template="form/field.html")), css_class="form-row inline %s" % prefijo ) ,#cambiar por el prefijo

        )
        super(DocumentosForms, self).__init__(*args, **kwargs)


    id                = forms.IntegerField(required=False)
    appcc_id          = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    manautctrl_id     = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    planautoctrl_id   = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cabreg_id         = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    detreg_id         = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    registros_id      = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cuadgest_id       = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    relentes_id       = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    gestincid_id      = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cabanali_id       = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))
    cabinftec_id      = forms.IntegerField(required=False,widget=forms.TextInput(attrs= {'class':'hidden'}))



def get_doc_formset(padre,form, formset=BaseInlineFormSet, **kwargs):
    return inlineformset_factory(padre, Documentos, form, formset,can_delete=True,extra=1)

AppccDocFormset     = get_doc_formset(APPCC,DocumentosForms, extra=5)
#AppccDocFormset     = get_doc_formset(APPCC,DocumentosUploadForm, extra=5)
ManualDocFormset    = get_doc_formset(ManualAutoControl,DocumentosForms, extra=5)
PlanDocFormset      = get_doc_formset(PlanAutoControl,DocumentosForms, extra=5)
CabRegDocFormset    = get_doc_formset(CabRegistros,DocumentosForms, extra=5)
DetRegDocFormset    = get_doc_formset(DetallesRegistros,DocumentosForms, extra=5)
RegistrosDocFormset = get_doc_formset(Registros,DocumentosForms, extra=5)
CuadGestFormset     = get_doc_formset(CuadrosGestion,DocumentosForms, extra=5)
RelEntesFormset     = get_doc_formset(RelacionesEntes,DocumentosForms, extra=5)
GestorIncidenciasFormset = get_doc_formset(GestorIncidencias,DocumentosForms, extra=5)
CabAnaliticasFormset     = get_doc_formset(CabAnaliticas,DocumentosForms, extra=5)
CabInfTecnicosFormset    = get_doc_formset(CabInformesTecnicos,DocumentosForms, extra=5)

class RelacionPersonalForms(forms.ModelForm):
    class Meta:
        model = RelacionesEntes
        exclude = ('user','fechaalta','manautctrl',)

    def __init__(self, *args, **kwargs):
        prefijo="relentes"
        self.helper = FormHelper()
        self.helper.form_id     = 'id-personal'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
            Div( Field('id',css_class="control-group hidden",),

                Field('manautctrl',css_class="control-group hidden")
               ),
            Div(
                    Div(Field('fechavalida', template=fecha),css_class=s6),
                    Div(Field('fechabaja',  template=fecha),css_class=s6),
                    css_class=s12
                ),
            Div(
                Div('frecuencia',css_class=s6),
                Div('personal',css_class=s6),
                css_class=s12
                ),Div(Div(Field('tiposcursos',css_class=xxlarge), css_class=s6), Div(Field('tercero',css_class=xlarge),css_class=s6),css_class=s12),),


            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        super(RelacionPersonalForms, self).__init__(*args, **kwargs)


    id            = forms.IntegerField(required=False)
    manautctrl_id = forms.IntegerField(required=False)
    personal      = AutoCompleteSelectField(lookup_class=PersonalLookup,required=True,help_text=_("Autoselección"))
    frecuencia    = AutoCompleteSelectField(lookup_class=TiposFrecuenciasLookup,required=True,help_text=_("Autoselección"))
    tiposcursos   = AutoCompleteSelectField(lookup_class=TiposCursosLookup,required=True,label=_('Curso Recibido'),help_text=_("Autoselección"))
    tercero       = AutoCompleteSelectField(lookup_class=TercerosTiposLookup,required=True,label=_('Imparte el Curso'),help_text=_("Autoselección"))

    def save(self, commit=True, user=None,*args, **kwargs):
        self.user      = user
        self.fechaalta = datetime.datetime.now()
        instance =super(RelacionPersonalForms,self).save(commit=False)
        if commit:
            instance.save()
        return instance


class RelacionTercerosForms(forms.ModelForm):
    class Meta:
        model = RelacionesEntes
        exclude = ('user','fechaalta','manautctrl',)

    def __init__(self, *args, **kwargs):
        prefijo="relentes"
        self.helper = FormHelper()
        self.helper.form_id     = 'id-terceros'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
            Div( Div('id',css_class="control-group hidden",),
                 Div('personal',css_class="control-group hidden"),
                 Div('manautctrl',css_class="control-group hidden")
            ),
            Div(
                Div(Field('fechavalida', template=fecha),css_class=s4),
                Div(Field('fechabaja', template=fecha),css_class=s4),
                Div('actividades',css_class=s4),
                css_class=s12
            ),
            Div(
                Div('frecuencia',css_class=s6),
                Div('tercero',css_class=s6),
                css_class=s12
                ),
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"))
        )
        super(RelacionTercerosForms, self).__init__(*args, **kwargs)


    id             = forms.IntegerField(required=False)
    manautctrl_id  = forms.IntegerField(required=False)
    frecuencia     = AutoCompleteSelectField(lookup_class=TiposFrecuenciasLookup,required=True,help_text=_("Autoselección"))
    personal_id    = forms.IntegerField(required=False)
    tercero        = AutoCompleteSelectField(lookup_class=TercerosLookup,required=True,help_text=_("Autoselección"))
    actividades    = AutoCompleteSelectField(lookup_class=ActividadesLookup,required=True,help_text=_("Autoselección"))

    def save(self, commit=True, user=None,*args, **kwargs):
        self.user      = user
        self.fechaalta = datetime.datetime.now()
        instance =super(RelacionTercerosForms,self).save(commit=False)
        if commit:
            instance.save()
        return instance

#----------------------------Cuadros Gestion Forms -----------------------------------------#


class CuadrosGestionForms(forms.ModelForm):
    class Meta:
        model = CuadrosGestion
        exclude = ('user','fechaalta','appcc') #Excluir para saltar la validacion en el Form

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-cuagestion'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div('appcc_id',css_class="control-group hidden"),
                Div('parent',css_class="control-group hidden"),
                Div(Div(Field('orden',css_class=mini,readonly=True),css_class=s4),Div(Field('etapa',css_class=xxlarge),css_class=s3),css_class=s12),
                Div(Div(Field('peligro',css_class=xlarge),css_class=s6),Div(Field('tpmedactp',css_class=xlarge),css_class=s6),css_class=s12),
                Div(Div(Field('tplimitcrit',css_class=xlarge),css_class=s4),Div(Field('ptocritico',css_class=mini),css_class=s4),Div(Field('ptoctrlcrit',css_class=mini),css_class=s4),css_class=s12),
                Div(Div(Field('tpmedvig',css_class=xlarge),css_class=s4),Div('momento',css_class=s4),Div('ente',css_class=s4),css_class=s12),
                Div(Div(Field('tpmedactc',css_class=xlarge),css_class=s4),Div('registros',css_class=s4),Div('tpfrecreg',css_class=s4),css_class=s12),


            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"), Submit('subetapa', "Crear SubEtapa"))
        )
        super(CuadrosGestionForms, self).__init__(*args, **kwargs)



    id              = forms.IntegerField(required=False)
    appcc_id        = forms.IntegerField(required=False)
    ente            = AutoCompleteSelectField(lookup_class=PersonalLookup,required=True,label="Persona",help_text=_("Quien es el encargado/a de la vigilancia"))
    tpfrecreg       = AutoCompleteSelectField(lookup_class=TiposFrecuenciasLookup,required=False,label="Frec.Registro",help_text=_("Autoselección"))
    tpmedactp       = AutoCompleteSelectField(lookup_class=TPActuacionPrevLookup,required=False,label="Medida de Actuación Preventiva",help_text=_("Autoselección"))
    tpmedactc       = AutoCompleteSelectField(lookup_class=TPActuacionCorrLookup,required=False,label="Medida de Actuación Correctoras",help_text=_("Autoselección"))
    tpmedvig        = AutoCompleteSelectField(lookup_class=TipoMedidasVigilanciaLookup,required=False, label="Medida Vigilancia",help_text=_("Autoselección"))
    tplimitcrit     = AutoCompleteSelectField(lookup_class=TPLimitesCritLookup,required=False,label="Limite Critico",help_text=_("Autoselección"))
    registros       = AutoCompleteSelectField(lookup_class=CabRegistrosLookup,required=False,help_text=_("Autoselección"))
    peligro         = AutoCompleteSelectField(lookup_class=PeligrosLookup,required=True,label="Peligro",help_text=_("Autoselección"))
    etapa           = AutoCompleteSelectField(lookup_class=EtapasLookup,required=True,label="Etapa",help_text=_("Autoselección"))

    def save(self, commit=True, request=None,*args, **kwargs):
        self.user         = request.user
        self.fechaalta    = datetime.datetime.now()
        instance =super(CuadrosGestionForms,self).save(commit=False)
        if commit:
            instance.save()
        return instance

    #Validación registros con punto criticos
    def clean(self):
        cleaned_data = super(CuadrosGestionForms,self).clean()
        registros    = cleaned_data.get('registros')
        ptoctrlcrit  = cleaned_data.get('ptoctrlcrit')
        tpfrecreg    = cleaned_data.get('tpfrecreg')
        if registros is None and  ptoctrlcrit:
            msg= "Existe un punto critico de control, registro no puede ser nulo"
            self.errors["registros"] = self.error_class([msg])
            del cleaned_data["registros"]
        if registros is not None and tpfrecreg is None:
            msg= "Existe un registro, frecuencia no puede ser nula"
            self.errors["tpfrecreg"] = self.error_class([msg])
            del cleaned_data["tpfrecreg"]
        return cleaned_data






class RegistrosRapidosForms(forms.ModelForm):
    class Meta:
        model = Registros
        exclude=('detreg','horarioturno')




class GestorIncidenciasForms(forms.ModelForm):
    class Meta:
        model = GestorIncidencias
        exclude = ('user','fechaalta','appcc') #Excluir para saltar la validacion en el Form

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id     = 'id-gestincidencias'
        self.helper.form_class  = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                Div('id',css_class="control-group hidden"),
                Div('appcc_id',css_class="control-group hidden"),
                Div(Div(Field('fincidencia',template=fecha),css_class=s4),
                    Div('estado',css_class=s4),
                    Div(Field('festado',template=fecha),css_class=s4 )
                ,css_class=s12),
                Div(Div(Field('denominacion',css_class="input-xlarge"),css_class=s4),Div(Field('etapa',css_class=xlarge),css_class=s4),Div(Field('tpmedactc',css_class=xlarge),css_class=s4),css_class=s12),
                Div(Div(Field('zonas',css_class=xlarge),css_class=s4),Div('equipo',css_class=s4),Div('personal',css_class=s4),css_class=s12),
                Div(Field('observaciones', template=editor),css_class=s12),
            ),
            FormActions( Submit( "Update","Guardar"), Button( "cancel","Cancelar"),)
        )
        super(GestorIncidenciasForms, self).__init__(*args, **kwargs)

    id              = forms.IntegerField(required=False)
    appcc_id        = forms.IntegerField(required=False)
    personal        = AutoCompleteSelectField(lookup_class=PersonalLookup,required=True,label=_("Persona"),help_text=_("Autoselección"))
    tpmedactc       = AutoCompleteSelectField(lookup_class=TPActuacionCorrLookup,required=False,label=_("Medida de Actuación Correctoras"),help_text=_("Autoselección"))
    zonas           = AutoCompleteSelectField(lookup_class=ZonasLookup,required=False,help_text=_("Autoselección"))
    equipo          = AutoCompleteSelectField(lookup_class=CatalogoEquiposLookup,required=False,help_text=_("Autoselección"))
    etapa           = AutoCompleteSelectField(lookup_class=EtapasLookup,required=True,label=_("Etapa"),help_text=_("Autoselección"))

    def save(self, commit=True, request=None,*args, **kwargs):
        self.user         = request.user
        self.fechaalta    = datetime.datetime.now()
        instance =super(GestorIncidenciasForms,self).save(commit=False)
        if commit:
            instance.save()
        return instance