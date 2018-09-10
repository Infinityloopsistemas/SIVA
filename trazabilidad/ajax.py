# -*- coding: utf-8 -*-
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
#from trazabilidad.models import DetProcesos
from django.utils.translation import gettext_lazy as _

__author__ = 'julian'


# def mensajes_error(dajax,titulo,mensaje):
#     dajax.assign('#titulo', 'innerHTML', '<span> %s </span' % titulo )
#     dajax.assign('#cuerpo', 'innerHTML', '<span> %s </span' % mensaje )
#     dajax.script(" $('#mensajeserror').modal('toggle').css({'width': '500px','margin-left': function () {return -($(this).width() / 2);}})")
# 
# @dajaxice_register
# def buscaProceso(request,id):
#     dajax          = Dajax()
#     nivel="E"
#     if len(id) !=0:
#         try:
#             print "Ver id %s" % id
#             nivel= DetProcesos.objects.get(pk=id).tproceso.nivel
#         except DetProcesos.DoesNotExist:
#             mensajes_error(dajax, _("Error"), _("Es necesario identificar la linea de Proceso") )
# 
#     if nivel == "E":
#         dajax.script("readonlyLoteOrigen('True');")
#     else:
#         dajax.script("readonlyLoteOrigen('False');")
# 
#     return dajax.json()