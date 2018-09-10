from django import forms
import selectable.forms as selectable
from gestion.lookups import OProduccionLookup
from gestion.models import DetLotes, Lotes
_author__ = 'julian'

#
#class DetalleMercanciaLote(forms.ModelForm):
#    class Meta:
#                model = DetLotes
#
#    id       = forms.IntegerField(required=False)
#    feccad   = forms.forms.DateField(label='Fecha Caducidad',required=True, input_formats=('%d/%m/%Y',), widget=DateInput(format='%d/%m/%Y'))
#    producto = forms.AutoCompletSelectField('mercancias', required=True, help_text =_("Se autocompleta"))
#    bultos   = forms.IntegerField(required=False,widget=TextInput(attrs={'class':'bultos'}) )
#    kilos    = forms.DecimalField( max_digits=15, decimal_places=2, localize=True, required=True,widget=TextInput(attrs={'class':'kilos'}))
#

class LotesAdminForm(forms.ModelForm):

    class Meta(object):
        model=Lotes

    oproduccion   = forms.CharField(label='Orden Produccion',widget=selectable.AutoComboboxSelectWidget(OProduccionLookup), required=True)
    fecha         = forms.DateField()
    lote          = forms.CharField()
    analiticas    = forms.ComboField()
    procesos      = forms.ComboField()
    templote      = forms.CharField()
    carorganolep  = forms.CharField()
    observaciones = forms.CharField()

