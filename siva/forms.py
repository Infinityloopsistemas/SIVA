# -*- coding: utf-8 -*-
from django import forms
class ContactoForm(forms.Form):
    asunto = forms.CharField(label=("Asunto"), max_length=100, required=True)
    mensaje = forms.CharField(label=("Mensaje"), widget=forms.Textarea, max_length=1000, required=True)