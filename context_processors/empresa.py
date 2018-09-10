# -*- coding: utf-8 -*-
from maestros_generales.models import Empresas

__author__ = 'julian'


def nombre_empresa(request):
    try:
        empresa = Empresas.objects.get(usuario=request.user)
        return { 'nombre_empresa' : empresa, }
    except:
        return { 'nombre_empresa' : " "}