# -*- coding: utf-8 -*-
from django.contrib import admin
from clonar.models import IntroClonaEmpresas

from siva.utils import EsqueletoModelAdmin

__author__ = 'julian'


class IntroClonaEmpresasAdmin(EsqueletoModelAdmin):
    readonly_fields = ('adminempresa','idempresa','fechaalta')
    fieldsets = (
        (None, {
            'fields': (('nombreempresa' ,'usergestion','passgestion'),('emporigen',),('adminempresa','idempresa','fechaalta'))
        }),
        )

    list_display = ['idempresa','fechaalta']
    search_fields = ['adminempresa__descripcion']


admin.site.register(IntroClonaEmpresas,IntroClonaEmpresasAdmin)