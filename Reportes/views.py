# -*- coding: utf-8 -*-
import datetime
from types import IntType
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import ModelFormMixin
from pyjasperclient import JasperClient
from reportes.forms import ParametrosForms
from reportes.models import DetalleInformes, Informes
from siva import settings
from maestros_generales.models import Empresas
from siva.utils import render_response
from django.core.urlresolvers import reverse
from django.utils.translation import gettext_lazy as _
from context_processors.empresa import nombre_empresa
from django.contrib.auth.models import User
from reportes.utils import comprobar_autorizacion_reportes
from appcc.models import *

#Hacer informe para agrupar por Equipos



class ReporteBaseView(object):
    extra_context={}
    model = Informes
    def __init__(self):
        auxiliar   = {"etiqueta" : "Relación de informes"}
        self.acciones={}
        ReporteBaseView.extra_context = { "auxiliar" : auxiliar, "acciones": self.acciones, "cabezera" : ["Reporte","Imprimir"]}

    def get_context_data(self, **kwargs):
        context = super( ReporteBaseView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_success_url(self):
        return reverse('reportes_list'  )

    @method_decorator(login_required(login_url="/"))
    def dispatch(self, *args, **kwargs):
        return super(ReporteBaseView, self).dispatch(*args, **kwargs)

class ReportesListaView(ReporteBaseView,ListView):

    template_name = "base/listmodal_impresion.html"

    def get_queryset(self):
        id     = self.kwargs['pid']
        modelo = self.kwargs['pmodelo']
        tpid   = self.kwargs['ptpid']
        objeto = nombre_empresa(self.request)
        self.acciones["empresa"] = objeto['nombre_empresa']
        self.acciones ['id']   = id
        objeto    = ContentType.objects.get(model=modelo)
        idmodelo = objeto.id
        if tpid =="0": #Discrimina si tiene que hacer referencia a un tipo de plan de control especifico
            q = { "content_type_id" : idmodelo} #Filtra el reporte a la tabla
        else:
            q = { "content_type_id" : idmodelo, "tpplancontrol_id" : tpid} #Filtra el reporte a la tabla y al tipo de plan de control
        return Informes.objects.filter(**q)




def llamareporte(nombre,camino,parametros):
    j = JasperClient(camino,settings.USUARIO_JASPER,settings.PASSWD_JASPER)
    listaparametros  = []
    for para in parametros:
            valor = para['valor']
            if type(valor)== datetime.date:
                valor=valor.strftime('%Y%m%d')
            if type(valor) == int:
                valor=str(valor)
            listaparametros.append((str(para['nombparametro']),valor))
    if parametros ==[]:
        ret = j.runReport(nombre,"PDF")
    else:
        ret = j.runReport(nombre,"PDF",params=dict(listaparametros))
    return ret['data']

@login_required(login_url='/')
def impresion(request,pid,id):
    # Solo se puede pasar un parametro al reporte , SOLO ID SOLO ID, !CUIDADO!
    # id valor del parametro a pasar al  informe sirve para su generacion
    #pid valor de id de detalles infomre sirve para generar entrada de parametros para el informe
    #Verificar si existen paramaetros a mostrar ......
    nombreEmpresa = nombre_empresa(request)
    empresa = nombreEmpresa['nombre_empresa']
    pempresa = empresa.pk
    try:
        informe = Informes.objects.get(pk=pid)
        print informe.content_type.model
        if not comprobar_autorizacion_reportes(informe.content_type.model,id,pempresa) :
            raise Http404
        numpara = DetalleInformes.objects.filter(informe = pid).count()
    except Informes.DoesNotExist:
        raise Http404
    if numpara == 0:
            if len(informe.nombprocede) != 0:
                from django.db import connection
                sql    =  informe.nombprocede
                cursor = connection.cursor()
                cursor.execute(sql)
                cursor.close()
            camino = informe.url
            return HttpResponse(llamareporte(informe.nombrereport,informe.url,[]), content_type='application/pdf')
    else:
        try:
            informe          = Informes.objects.get(pk=pid)
            parametros       = DetalleInformes.objects.filter(informe = pid, mostrar=True).exclude(nombparametro='pid')
            numpara          = parametros.count()
            formInformes     = ParametrosForms(request.POST or None,pidinfo=pid,idconsulta=id)
        except Informes.DoesNotExist:
            raise Http404
        if numpara ==0: #Solo existe una opcion para un parametro sin ventana de entrada de datos de parametros
            dinforme  = DetalleInformes.objects.filter(informe =pid ,mostrar=False)
            if dinforme.count() == 1:
                cd=[]
                if dinforme[0].query_modelo is not None:
                    if len(dinforme[0].query_modelo) !=0:
                        id = eval( dinforme[0].query_modelo )                                              
                cd.append({ 'nombparametro': dinforme[0].nombparametro, 'valor' : str(id) })
                print cd
                return HttpResponse(llamareporte(informe.nombrereport,informe.url,cd), content_type='application/pdf')

        else:
            #Llama a ventana para introducir parametros.....
            if request.method == 'POST':
                cd=[]
                if formInformes.is_valid():
                    paraform = formInformes.cleaned_data
                    if len(informe.nombprocede) != 0: #Llamada a procedimientos em caso de que exista
                        from django.db import connection
                        var=[]
                        i=0
                        for para in  cd:
                            var.append(str(para['valor']))
                            cursor   = connection.cursor()
                            #ret      = cursor.callproc(str(informe.nombprocede),(var[1],var[0]))
                            ret      = cursor.callproc(str(informe.nombprocede))
                            cursor.close()
                    else:
                        dinforme  = DetalleInformes.objects.filter(informe=pid)
                        for para in dinforme:
                                print "----------- parametros"
                                print paraform
                                print "Valor parametros %s" % paraform[para.nombparametro]
                                print "Nombre parametos %s " % para.nombparametro
                                print para.query_modelo
                                id=0
                                if para.query_modelo is not None and  len(para.query_modelo) !=0:
                                            id = eval( para.query_modelo )
                                            if id is not None:
                                                id= str(id)
                                            else:
                                                id="0"
                                else:
                                    id =paraform[para.nombparametro]

                                cd.append({ 'nombparametro': para.nombparametro, 'valor' : id  })
                                print cd


                    return  HttpResponse(llamareporte(informe.nombrereport,informe.url,cd), content_type='application/pdf')
                else:
                    print formInformes.errors
                #recorremos el post construyendo la cadena de parametros para anexar a la url del informe.



        return render_response( request,"reportes/parametros.html",{'form': formInformes,})