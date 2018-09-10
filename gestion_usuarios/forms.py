# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from maestros_generales.models import MetaUsuarios, Empresas

ROLE_STAFF_CHOICES =(('1','Administrador/a'),('2','Veterinario/a'))
ROLE_USER_CHOICES =(('5','Operario'),('3','Coordinador/a'),('4','Responsable'))
class CrearUsuariosForm(forms.Form):
    nombre = forms.CharField(label='Nombre de usuario',max_length=8, required=True)
    password = forms.CharField(label='Contraseña',max_length=15,widget=forms.PasswordInput, required=True)
    repassword = forms.CharField(label='Repita Contraseña',max_length=15,widget=forms.PasswordInput, required=True)
    email = forms.EmailField(label='Correo electrónico', required=True)
    rol = forms.ChoiceField(widget=forms.RadioSelect,choices=ROLE_STAFF_CHOICES,required=True)
    passadm = forms.CharField(label='Contraseña Admin',max_length=15,widget=forms.PasswordInput, required=True)
    
    def __init__(self,user,data=None):
        self.user = user
        super(CrearUsuariosForm,self).__init__(data=data)
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if User.objects.filter(username=nombre).count() > 0:
            raise forms.ValidationError("El usuario existe.")
        return nombre
    def clean_repassword(self):
        password = self.cleaned_data.get('password')
        repassword = self.cleaned_data.get('repassword')
        if password and repassword:
            if password != repassword:
                raise forms.ValidationError("Las contraseñas no coinciden.")
        return repassword
    
    def clean_passadm(self):
        passadm = self.cleaned_data.get('passadm')
        if not self.user.check_password(passadm):
            raise forms.ValidationError('Invalid admin password')
        return passadm
class BorrarUsuariosForms(forms.Form):
    metaUser = forms.CharField(label='Meta-Usuario',widget=forms.Select(choices=MetaUsuarios.objects.all().values_list('id','nombre')))
    passadm = forms.CharField(label='Contraseña Admin',max_length=15,widget=forms.PasswordInput, required=True)
    def __init__(self,user,*args,**kwargs):
        self.user = user
        super(BorrarUsuariosForms,self).__init__(*args,**kwargs)
        
    
    def clean_passadm(self):
        passadm = self.cleaned_data.get('passadm')
        if not self.user.check_password(passadm):
            raise forms.ValidationError('Invalid admin password')
class ModificarUsuarioForms(forms.Form):
    passactual = forms.CharField(label='Contraseña Actual',max_length=15,widget=forms.PasswordInput, required=True)
    password = forms.CharField(label='Nueva Contraseña',max_length=15,widget=forms.PasswordInput, required=True)
    repassword = forms.CharField(label='Repita Nueva Contraseña',max_length=15,widget=forms.PasswordInput, required=True)
    
    def __init__(self,user,data=None):
        self.user = user
        super(ModificarUsuarioForms,self).__init__(data=data)
        
    def clean_passactual(self):
        passactual = self.cleaned_data.get('passactual')
        if not self.user.check_password(passactual):
            raise forms.ValidationError('Invalid actual password')
    def clean_repassword(self):
        password = self.cleaned_data.get('password')
        repassword = self.cleaned_data.get('repassword')
        if password and repassword:
            if password != repassword:
                raise forms.ValidationError("Las contraseñas no coinciden.")
        return repassword

class CrearUsuarioForm(forms.Form):
    empresa = forms.CharField(label='Empresas',widget=forms.Select(choices=Empresas.objects.all().values_list('id','descripcion')))
    nombre = forms.CharField(label='Nombre de usuario',max_length=8, required=True)
    password = forms.CharField(label='Contraseña',max_length=15,widget=forms.PasswordInput, required=True)
    repassword = forms.CharField(label='Repita Contraseña',max_length=15,widget=forms.PasswordInput, required=True)
    email = forms.EmailField(label='Correo electrónico', required=True)
    rol = forms.ChoiceField(widget=forms.RadioSelect,choices=ROLE_USER_CHOICES,required=True)
    passadm = forms.CharField(label='Contraseña Admin',max_length=15,widget=forms.PasswordInput, required=True)
    
    def __init__(self,user,data=None):
        self.user = user
        super(CrearUsuarioForm,self).__init__(data=data)
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        empresa = self.cleaned_data.get('empresa')
        emp = Empresas.objects.get(pk=empresa)
        nombre_empresa = emp.descripcion.lower()
        nombre_empresa = nombre_empresa.replace(' ','_')
        user_nombre = '%s_%s' % (nombre,nombre_empresa)
        print nombre_empresa
        if User.objects.filter(username=user_nombre).count() > 0:
            raise forms.ValidationError("El usuario existe.")
        return nombre
    def clean_repassword(self):
        password = self.cleaned_data.get('password')
        repassword = self.cleaned_data.get('repassword')
        if password and repassword:
            if password != repassword:
                raise forms.ValidationError("Las contraseñas no coinciden.")
        return repassword
    
    def clean_passadm(self):
        passadm = self.cleaned_data.get('passadm')
        if not self.user.check_password(passadm):
            raise forms.ValidationError('Invalid admin password')
        return passadm

class BorrarUsuarioForms(forms.Form):
    nombre = forms.CharField(label='Nombre de usuario',max_length=30, required=True)
    passadm = forms.CharField(label='Contraseña Admin',max_length=15,widget=forms.PasswordInput, required=True)
    def __init__(self,user,*args,**kwargs):
        self.user = user
        super(BorrarUsuarioForms,self).__init__(*args,**kwargs)
        
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if User.objects.filter(username=nombre).count() == 0:
            raise forms.ValidationError("El usuario no existe.")
        return nombre
    def clean_passadm(self):
        passadm = self.cleaned_data.get('passadm')
        if not self.user.check_password(passadm):
            raise forms.ValidationError('Invalid admin password')