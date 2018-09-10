# -*- coding: utf-8 -*-
from crispy_forms.layout import Layout, Fieldset, Div, Field, Submit, HTML
from django.forms import ModelForm, models
from django import forms
from reportes.models import DetalleInformes, Informes
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions, StrictButton
from siva.utils import fecha, xlarge


#class ParametrosForms(ModelForm):
#    class Meta:
#        model = DetalleInformes
#
#    nombetiqueta  = forms.CharField(max_length=20, widget = forms.TextInput(attrs={'class':'etiqueta','readonly':'readonly'}))
#    nombparametro = forms.CharField(max_length=20 )
#    valor         = forms.CharField(max_length=20,widget = forms.TextInput(attrs={'class':'valor'}))
#
#
#def get_detalle_formset(form, formset=models.BaseInlineFormSet, **kwargs):
#    return models.inlineformset_factory(Informes,DetalleInformes,form,formset,can_delete=False,extra=0)
#

class ParametrosForms(forms.Form):

    def __init__(self, *args, **kwargs):
        idinfo     = kwargs.pop("pidinfo")
        idcons     = kwargs.pop("idconsulta")
        parametros = DetalleInformes.objects.filter(informe_id= idinfo)
        super(ParametrosForms, self).__init__(*args, **kwargs)
        #self.fields['pid']=forms.IntegerField(required=False, initial=idcons)
        self.helper = FormHelper()
        self.helper.layout =Layout(Div(HTML("<span>  </span>")))
        pare = parametros.count()
        for par in parametros:
            i=0
            if par.tipoparametro =="D":
                 self.fields[par.nombparametro]= forms.DateField(label=par.nombetiqueta)
                 self.helper.layout.insert(i,Div(Field(par.nombparametro, template="form/field_date.html",css_class="span6")))
            if par.tipoparametro == "T":
                self.fields[par.nombparametro]= forms.CharField(label=par.nombetiqueta)
                self.helper.layout.insert(i,Div(Field(par.nombparametro,css_class="span12")))
            if par.tipoparametro == "N" and par.mostrar==False:
                 self.fields[par.nombparametro]= forms.IntegerField(required=False, initial=idcons)
                 self.helper.layout            = Layout(Div(Field(par.nombparametro,type="hidden") ) )
            if par.tipoparametro == "N" and par.mostrar==True:
                self.fields[par.nombparametro]= forms.IntegerField(label=par.nombetiqueta)
                self.helper.layout.insert(i,Div(Field(par.nombparametro,css_class="span12")))
            i+=1

        self.helper.form_id     = 'id-informes'
        self.helper.form_class  = 'form-vertical'
        self.helper.form_method = 'post'
        self.helper.form_action = 'imprimir'
        self.helper.add_input(Submit('submit', 'Generar'))

