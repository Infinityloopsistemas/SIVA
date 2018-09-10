from django import forms
from imagen.models import Imagen

class addImagenForms(forms.Form):
    nombre = forms.CharField()
    file = forms.FileField()
    
class ImagenForms(forms.ModelForm):
    CATEGORIAS = (
        ('0','Sin lugar'),
        ('1','Logo'),
        ('2','Cabecera'),
        ('3','Galeria'),
    )
    lugar = forms.ChoiceField(label="Lugar",choices=CATEGORIAS)
    fich = forms.FileField(label="Fichero",required=False)
    class Meta:
        model = Imagen
        exclude = ('file','content_type_file','content_type','object_id')

class ImagenReportForms(forms.ModelForm):
    fich = forms.FileField(label="Fichero",required=False)
    class Meta:
        model = Imagen
        exclude = ('denominacion','file','content_type_file','content_type','object_id','lugar')
