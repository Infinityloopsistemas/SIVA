from django.shortcuts import render, render_to_response
from maestros_generales.models import Empresas, MetaUsuarios
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from gestion_usuarios.utils import is_allowed_edit

from django.template import RequestContext
from gestion_usuarios.forms import CrearUsuariosForm, BorrarUsuariosForms, ModificarUsuarioForms, CrearUsuarioForm,\
    BorrarUsuarioForms


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser,login_url='/')
def CrearUsuariosView(request):
    
    if request.method == 'POST':
        form = CrearUsuariosForm(user = request.user,data=request.POST or None)
        if form.is_valid():
            usuarios_creados = []
            nombre_usuario = form.cleaned_data['nombre']
            contra = form.cleaned_data['password']
            email = form.cleaned_data['email']
            rol = form.cleaned_data['rol']
            userDefault = User.objects.create_user(nombre_usuario,email,contra)
            if rol == '1':        
                userDefault.is_staff = True
                userDefault.is_superuser = True
                userDefault.is_active = True
            elif rol == '2':
                userDefault.is_staff  = True
                userDefault.is_active = True
            else:
                userDefault.is_active = True
            userDefault.groups.add(rol)
            userDefault.save()
            usuarios_creados.append(userDefault)
            meta = MetaUsuarios(nombre = nombre_usuario)
            print meta
            meta.save()
            meta.usuario.add(userDefault)
            empresas = Empresas.objects.all()
            for empresa in empresas:
                nombre_empresa = empresa.descripcion.lower()
                nombre_empresa = nombre_empresa.replace(' ','_')
                user_nombre = '%s_%s' % (nombre_usuario,nombre_empresa)        
                newuser = User.objects.create_user(user_nombre,email,contra)
         
                if rol == '1':
                    newuser.is_staff  = True
                    newuser.is_active = True
                    newuser.is_superuser=True
                elif rol == '2':
                    newuser.is_staff  = True
                    newuser.is_active = True
                else:
                    newuser.is_active = True
                newuser.groups.add(rol)
                newuser.save()
                usuarios_creados.append(newuser)
                meta.usuario.add(newuser)
                empresa.usuario.add(newuser)
                empresa.save()
            meta.save()
            return render_to_response('gestion_usuarios/usuarios_creados.html',{'users':usuarios_creados},context_instance=RequestContext(request))
    else:
        form = CrearUsuariosForm(user = request.user,data=request.POST or None)
    return render_to_response('gestion_usuarios/form.html',{'form':form},context_instance=RequestContext(request))

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser,login_url='/')
def BorrarUsuariosView(request):
    if request.method == 'POST':
        form = BorrarUsuariosForms(user=request.user,data = request.POST or None)
        if form.is_valid():
            metaUser = form.cleaned_data['metaUser']
            print metaUser  
            usuarios = MetaUsuarios.objects.get(pk=metaUser).usuario.all()     
            usuarios_borrados = []
            for usuario in usuarios:
                usuarios_borrados.append(usuario)
                usuario.delete()
            meta = MetaUsuarios.objects.get(pk=metaUser)
            meta.delete()
            return render_to_response('gestion_usuarios/usuarios_borrados.html',{'users':usuarios_borrados},context_instance=RequestContext(request))
    else:
        form = BorrarUsuariosForms(user=request.user,data = request.POST or None)
    return render_to_response('gestion_usuarios/form.html',{'form':form},context_instance=RequestContext(request))
     
@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def ModificarUsuarioView(request):
    if request.method == 'POST':
        form = ModificarUsuarioForms(user=request.user,data = request.POST or None)
        if form.is_valid():
            password = form.cleaned_data['password']
            usuarios = MetaUsuarios.objects.get(nombre=request.user).usuario.all()     
            usuarios_modificados = []
            for usuario in usuarios:
                usuarios_modificados.append(usuario)
                usuario.set_password(password)
                usuario.save()
            
            return render_to_response('gestion_usuarios/usuario_modificado.html',{'users':usuarios_modificados},context_instance=RequestContext(request))
    else:
        form = ModificarUsuarioForms(user=request.user,data = request.POST or None)
    return render_to_response('gestion_usuarios/form.html',{'form':form},context_instance=RequestContext(request))
@login_required(login_url='/')
@user_passes_test(is_allowed_edit)
def comprobar_usuarios_empresas(request):
    template_name = "gestion_usuarios/usuarios_empresas.html"
    empresas = Empresas.objects.all()
    empresas_no_user = []
    meta_users = MetaUsuarios.objects.all()
    user_adm = Group.objects.get(name="administradores").user_set.all()
    user_vet = Group.objects.get(name="veterinarios").user_set.all()
    usuarios = []
    for meta_user in meta_users:
        mu = User.objects.filter(username=meta_user).first()
        if mu in user_adm or mu in user_vet:
            for empresa in empresas:
                nombre_empresa = empresa.descripcion.lower()
                nombre_empresa = nombre_empresa.replace(' ','_')
                user_nombre = '%s_%s' % (meta_user,nombre_empresa)
                users_empresas = Empresas.objects.get(pk=empresa.pk).usuario.all()
                user = User.objects.filter(username=user_nombre).first()
                if user not in users_empresas:
                    empresas_no_user.append(empresa)
                    usuarios.append(user_nombre)
                    user = User.objects.filter(username=mu).first()
                    print user
                    newuser = User.objects.create_user(user_nombre,user.email,user.password)
                    newuser.is_active= user.is_active
                    newuser.is_staff  = user.is_staff
                    newuser.is_superuser=user.is_superuser
                    newuser.groups.add(user.groups.all().first())
                    newuser.save()
                    meta = MetaUsuarios.objects.get(usuario=user)
                    meta.usuario.add(newuser)
                    empresa.usuario.add(newuser)
                    empresa.save()
                    print users_empresas
                    print usuarios
    return render_to_response(template_name,{'user_adm':empresas_no_user,'users':usuarios},context_instance=RequestContext(request))


@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser,login_url='/')
def CrearUsuarioView(request):
    
    if request.method == 'POST':
        form = CrearUsuarioForm(user = request.user,data=request.POST or None)
        if form.is_valid():
            nombre_usuario = form.cleaned_data['nombre']
            contra = form.cleaned_data['password']
            email = form.cleaned_data['email']
            rol = form.cleaned_data['rol']
            empresa = form.cleaned_data['empresa']
            emp = Empresas.objects.get(pk=empresa)
            nombre_empresa = emp.descripcion.lower()
            nombre_empresa = nombre_empresa.replace(' ','_')
            user_nombre = '%s_%s' % (nombre_usuario,nombre_empresa)        
            newuser = User.objects.create_user(user_nombre,email,contra)
            newuser.is_active = True
            newuser.groups.add(rol)
            newuser.save()
            emp.usuario.add(newuser)
            return render_to_response('gestion_usuarios/usuario_creado.html',{'user':newuser},context_instance=RequestContext(request))
    else:
        form = CrearUsuarioForm(user = request.user,data=request.POST or None)
    return render_to_response('gestion_usuarios/form.html',{'form':form},context_instance=RequestContext(request))

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser,login_url='/')
def BorrarUsuarioView(request):
    if request.method == 'POST':
        form = BorrarUsuarioForms(user=request.user,data = request.POST or None)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            print nombre
            user = User.objects.get(username=nombre)
            user.delete()
            return render_to_response('gestion_usuarios/usuario_borrado.html',{'user':user},context_instance=RequestContext(request))
    else:
        form = BorrarUsuarioForms(user=request.user,data = request.POST or None)
    return render_to_response('gestion_usuarios/form.html',{'form':form},context_instance=RequestContext(request))   