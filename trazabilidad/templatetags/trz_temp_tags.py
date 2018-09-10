'''
Created on 24/4/2015

@author: Claudio
'''
from django import template
from trazabilidad.models import Lotes
from siva.utils import pasarFechaTextoEsp

register = template.Library()

@register.filter(name='pasarFechaESP')
def pasarFechaESP(value):
    return pasarFechaTextoEsp(value)


register.filter('pasarFechaESP', pasarFechaESP)