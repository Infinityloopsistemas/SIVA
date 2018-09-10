# -*- coding: utf-8 -*-
from logging import exception
from parser import ParserError
from django.contrib.contenttypes.models import ContentType
from django.db.models import ProtectedError
from clonar.models import EmpresasClonadas

__author__ = 'julian'
from copy import deepcopy
from maestros.models import *
from appcc.models import  *
from productos.models import *

#El orden de clonado, primero entidades sin ForeingKey



def clonando(emporig,empdest,userdest,modulo, relcampos):

    print "Clonando ... %s" % modulo
    instancia = eval( "%s.objects.filter(empresa_id=%s)" % (modulo,emporig))
    aplicacion= eval("%s._meta.app_label" % modulo)
    nombusuario  = User.objects.get(pk=userdest)
    for obj in instancia:
        regclonado = deepcopy(obj)
        regclonado.id=None
        regclonado.empresa_id = empdest
        regclonado.user_id    = userdest
        if modulo == "CuadrosGestion":
            try:
                id=EmpresasClonadas.objects.get(emporigen_id=emporig,empdestino_id=empdest,modulo_id=46 ,idorigen =regclonado.parent_id ).idestino
            except EmpresasClonadas.DoesNotExist:
                id=None
            if id is None:
                regclonado.parent = None
            else:
                regclonado.parent= CuadrosGestion.objects.get(pk=id )

        if relcampos is not None:
            for campos in relcampos:
                valorreg  = getattr(regclonado,campos['campo']) #Registro Origen Valor
                if valorreg is not None:
                    idabuscar=None
                    try:
                        print "CLonando tablas %s" % campos['tabla'].lower()
                        idabuscar = EmpresasClonadas.objects.get(emporigen_id=emporig,empdestino_id=empdest,modulo=ContentType.objects.get(model=campos['tabla'].lower()),idorigen =valorreg ).idestino
                    except EmpresasClonadas.DoesNotExist:
                        error= "No encuentra de la tabla: %s  en campo:%s el registro:%s" % (campos['tabla'],campos['campo'],valorreg)
                        print error
                        pass
                    setattr(regclonado,campos['campo'],idabuscar)

        if aplicacion=="appcc" or modulo=="TiposTurnos":
            regclonado.save(user=nombusuario)
        else:
            regclonado.save()
        #Registra clonacion, fundamental para ForeingKey
        EmpresasClonadas.objects.create(emporigen_id=emporig,empdestino_id=empdest,modulo=ContentType.objects.get(model=modulo.lower()),idorigen=obj.id,idestino=regclonado.id)


def findForeignKeyTablas(modulo):
    aplicaciones  = ['maestros_generales','auth']
    tablasabuscar = []
    campos = eval("%s._meta.fields" % modulo)
    for field in campos:
        if field.get_internal_type() in ("ForeignKey"):
            if field.rel.to._meta.app_label not in (aplicaciones):
                tablasabuscar.append({ 'tabla': field.rel.to.__name__ , 'campo' : field.get_attname() })
    return tablasabuscar


def limpiarClonado(emporig,empdest,userdest,modulo,objmodulo):
    sw=0
    try:
        instancia = eval( "%s.objects.filter(empresa_id=%s).delete()" % (modulo,empdest))
    except ProtectedError:
         print "Imposible eliminar %s" % modulo
         sw=1
    if sw==0:
        EmpresasClonadas.objects.filter(emporigen_id=emporig,empdestino_id=empdest,modulo=objmodulo).delete()

#Sentencia :
# clonadoRecursivo(1,4,9,"PlanAutoControl","C")
# clonadoRecursivo(1,4,9,"DetallesRegistros","C")
# clonadoRecursivo(1,4,9,"CuadrosGestion","C")

def clonadoRecursivo(emporig,empdest,userdest,modulo, tipo):

    #Modulos que no interesa clonar
    if modulo.lower() in ('tracksondas','loaddatadevice','loaddatasensor','tracksondas','tracktemperaturas'):
        return

    #Recorremos las ForeingKey recursivamente
    try:
            objmodulo = ContentType.objects.get(model=modulo.lower())
    except ContentType.DoesNotExist:
            raise Exception("Entidad desconocidad")
    if tipo=="C":
        objemp =EmpresasClonadas.objects.filter(emporigen_id=emporig,empdestino_id=empdest,modulo=objmodulo)
    else:
        objemp=[]
    if len(objemp) ==0:
        listatablas=findForeignKeyTablas(modulo)
        if len(listatablas) ==0:
            if tipo =="C":
                clonando(emporig,empdest,userdest,modulo,None)
            else:
                limpiarClonado(emporig,empdest,userdest,modulo,objmodulo)
        else:
            for tablas in listatablas:
                clonadoRecursivo(emporig,empdest,userdest,tablas['tabla'],tipo)
            if tipo=="C":
                clonando(emporig,empdest,userdest,modulo,listatablas)
            else:
                limpiarClonado(emporig,empdest,userdest,modulo,objmodulo)
    return


def actualizaRegistros():
    empresas = Empresas.objects.all()

    # for emp in empresas:
    #     tiposturnos =TiposTurnos(denominacion='UNICO')
    #     tiposturnos.save(user=filter( lambda  u: str(u).find("LOZANO") != -1 ,emp.usuario.all() )[0].username)
    #     h1 = HorarioTurnos(tpturnos=tiposturnos,ihora=0,fhora=24)
    #     h1.save()
    #     ldetalle=DetallesRegistros.objects.filter(empresa=emp).update(tpturnos=tiposturnos)
    #     lreg    = Registros.objects.filter(detreg=ldetalle).update(horarioturno=h1)

    for emp in empresas:
        ldetalle=DetallesRegistros.objects.filter(empresa=emp)
        for det in ldetalle:
            reg = Registros.objects.filter(detreg=det).update(horarioturno=HorarioTurnos.objects.get(tpturnos=det.tpturnos))


#CREACION DE USUARIOS
def crearUsuarios(nombempresa,usergestion,passgestion,idorigen):

    creada=False

    sivauser="%s_%s" % ('julian',nombempresa.lower())
    email     = 'julian@infinityloop.es'
    contra    = 'fractal'

    objuser1=User.objects.filter(username=sivauser)
    if len(objuser1) ==0:
        user1 = User.objects.create_user(sivauser,email,contra)
        user1.is_staff  = True
        user1.is_active = True
        user1.is_superuser=True
        user1.save()
    else:
        user1 = User.objects.get(username=sivauser)


    sivauser        ="%s_%s" % ('LOZANO',nombempresa.upper())
    email           = 'josealzn@gmail.com'
    contra          = 'LOZANO1976B'
    objuser2=User.objects.filter(username=sivauser)
    if  len(objuser2) ==0:
        user2           = User.objects.create_user(sivauser,email,contra)
        user2.is_staff  = True
        user2.is_active = True
        user2.save()
        print "Usuario ID LOZANO %s" % user2.id
        idadmin=user2.id
    else:
       user2=User.objects.get(username=sivauser)


    sivauser        ="%s" % (usergestion)
    email           = ''
    contra          = passgestion
    objuser3=User.objects.filter(username=sivauser)
    if len(objuser3) == 0 :
        user3           = User.objects.create_user(sivauser,email,contra)
        user3.is_active = True
        user3.save()
    else:
        user3 = User.objects.get(username=sivauser)

    fobjemp= Empresas.objects.filter(descripcion=nombempresa.upper())
    if len(fobjemp) == 0:
        objemp  = Empresas( descripcion=nombempresa.upper(),habilitar=True,fechaalta=datetime.datetime.now().date())
        objemp.save()
        objemp.usuario.add(user1,user2,user3)
        objemp.save()
        print "Empresa ID: %s" % objemp.id
        try:
            clonadoRecursivo(idorigen,objemp.id,user2.id,"PlanAutoControl","C")
            clonadoRecursivo(idorigen,objemp.id,user2.id,"DetallesRegistros","C")
            clonadoRecursivo(idorigen,objemp.id,user2.id,"CuadrosGestion","C")
            creada=True
        except:
            creada=False
    else:
        objemp = Empresas.objects.get(descripcion=nombempresa.upper())

    return {'empresaid' : objemp.id , 'adminid' : user2.id, 'creada' : creada}



def clonadoTotal(idorigen,iddestino,idadmin):
    clonadoRecursivo(idorigen,iddestino,idadmin,"PlanAutoControl","C")
    clonadoRecursivo(idorigen,iddestino,idadmin,"DetallesRegistros","C")
    clonadoRecursivo(idorigen,iddestino,idadmin,"CuadrosGestion","C")