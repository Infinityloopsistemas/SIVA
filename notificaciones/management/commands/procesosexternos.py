# -*- coding: utf-8 -*-
from optparse import make_option
import os
import subprocess
import datetime
from django.core.management import BaseCommand
import appcc
import maestros
from siva import settings

__author__ = 'julian'


class ParserError(Exception):
    """
    Raised when a text parser fails to understand a file it been passed
    or the resulting parsed text is invalid
    """
    pass


class ParserUnknownFile(Exception):
    pass



class Command(BaseCommand):


    def onlypdf(self,archivo):
        if len(archivo) ==0:
            return -1
        ext = os.path.splitext(archivo)[1]
        ext = ext.lower()
        if ext in (".pdf"):
            print "Es pdf"
            return 1
        else:
            print "No es pdf"
            return -1

    def pdftoText(self,document_file):
            print "Procesando ... %s  " % document_file.name
            if self.onlypdf(document_file.name) == 1:
                command = []
                command.append('/usr/bin/pdftotext')
                command.append(os.path.join(settings.MEDIA_ROOT ,document_file.name))
                command.append('-')
                proc = subprocess.Popen(command, close_fds=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                return_code = proc.wait()
                if return_code != 0:
                    print "Error ..."
                    raise ParserError
                output = proc.stdout.read()
                print output
                if output == '\x0c':
                    print "Salida vacia"
                    raise ParserError('No output')
                else:
                    return output
            return None


    def procesadoOCR(self):
          #PDF
          objdoc = appcc.models.Documentos.objects.filter(fechaproceso__isnull=True)
          if objdoc!=[]:
              for obj in objdoc:
                    salida = self.pdftoText(obj.archivos)
                    if salida is not None:
                        actualiza = appcc.models.Documentos.objects.get(pk=obj.id)
                        actualiza.contenido = salida
                        actualiza.fechaproceso = datetime.datetime.today().date()
                        actualiza.save()

          objdoc = maestros.models.Documentos.objects.filter(fechaproceso__isnull=True)

          if objdoc!=[]:
              for obj in objdoc:
                    salida = self.pdftoText(obj.archivos)
                    if salida is not None:
                        actualiza = maestros.models.Documentos.objects.get(pk=obj.id)
                        actualiza.contenido = salida
                        actualiza.fechaproceso = datetime.datetime.today().date()
                        actualiza.save()

    option_list = BaseCommand.option_list + (
            make_option('--ocr',
                action='store_true',
                dest='ocr',
                default=False,
                help='Cumplimenta contenido ocr a texto'),

            )
    def handle(self, *args, **options):
        if options['ocr']:
           self.procesadoOCR()
