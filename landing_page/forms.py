from django import forms

class addLandingPage(forms.Form):
    
    empresa = forms.CharField()
    descripcion = forms.CharField()
    latitud = forms.FloatField()
    longitud = forms.FloatField()
    nota = forms.CharField()
    tags = forms.CharField()

    
class verLandingPage(forms.Form):
    empresa = forms.CharField()
    descripcion = forms.CharField()
    latitud = forms.FloatField()
    longitud = forms.FloatField()
    nota = forms.CharField()
    tags = forms.CharField()
    
class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField(label=("Username"), max_length=30)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)
