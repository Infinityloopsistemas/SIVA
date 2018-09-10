# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.db import models
from maestros.models import TiposTurnos, HorarioTurnos
from maestros_generales.models import Empresas

__author__ = 'julian'


class IntroClonaEmpresas(models.Model):
    nombreempresa = models.CharField(max_length=100)
    usergestion   = models.CharField(max_length=100)
    passgestion   = models.CharField(max_length=100)
    emporigen     = models.ForeignKey(Empresas, verbose_name="Empresas origen", related_name="u_empresa_origen")
    adminempresa  = models.ForeignKey(User, null=True, blank=True)
    idempresa     = models.ForeignKey(Empresas, verbose_name="Empresas Destino", related_name="u_empresa_destino",null=True,blank=True)
    fechaalta     = models.DateField(verbose_name="Fecha Alta", blank=True, null=True)


    def save(self, *args, **kwargs):
       from clonar.api import crearUsuarios
       #{'emrpesaid' : objemp.id , 'adminid' : user2.id, 'creada' : creada}
       dictEmpre = crearUsuarios(self.nombreempresa,self.usergestion,self.passgestion,self.emporigen.id)
       self.fechaalta       = datetime.date.today()
       self.idempresa_id    = dictEmpre['empresaid']
       self.adminempresa_id = dictEmpre['adminid']
       if dictEmpre['creada']:
        super(IntroClonaEmpresas, self).save(*args, **kwargs)
        #Crea los horarios de turnos , no se crean en la clonación
        objtiptur  = TiposTurnos.objects.filter(empresa_id=self.idempresa)
        for turno in objtiptur:
            objhorario = HorarioTurnos(tpturnos_id = turno.id,ihora=0,fhora=24)
            objhorario.save()
        #Envia email al admin de la empresa
        mensaje ="Se han clonado la siguiente empresa: %s , usuario administrador %s , usuario de gestion: %s , password de gestion : %s " % (self.nombreempresa,self.adminempresa.username,self.usergestion,self.passgestion)
        asunto  = "Clonado %s" % self.nombreempresa
        remitente = 'info@infinityloop.es'
        email     = ['josealzn@gmail.com']
       #email =['info@infinityloop.es',]
        send_mail(asunto,mensaje,remitente,email)


class EmpresasClonadas(models.Model):
    emporigen  = models.ForeignKey(Empresas, verbose_name="Empresas origen", related_name="empresa_origen")
    empdestino = models.ForeignKey(Empresas, verbose_name="Empresas destino",related_name="empresa_destino")
    modulo     = models.ForeignKey(ContentType, verbose_name="Modulo")
    idorigen   = models.IntegerField(verbose_name="Id Origen")
    idestino   = models.IntegerField(verbose_name="Id Destino")


