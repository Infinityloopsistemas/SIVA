# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from appcc.views import *
from siva.utils import make_url_list
from gestion_usuarios.utils import is_allowed_see


__author__ = 'julian'

#lista_urls=('manualautocontrol',)
#
#
#tup =  tuple(make_url_list(lista_urls,'appcc'))
#urlpatterns = patterns('', *tup)

urlpatterns = patterns('',
    url (
        regex = '^imprimir/listatareas/(?P<empresaid>\d+)/$',
        view =  'appcc.views.ImprimirListaTareas',
        name =  'tareasdia_impresion'
    ),

)

urlpatterns += patterns('',
    url (
        regex = '^imprimir/registrosEmpresa/(?P<empresaid>\d+)/$',
        view =  'appcc.views.ImprimirRegistrosEmpresas',
        name =  'registrosEmpresas_impresion'
    ),

)
#Appcc



urlpatterns += patterns('',
    url (
        #regex = '^appcc/lista/$',
        regex = '^appcc/$',
        view =  user_passes_test(is_allowed_see)(AppccListaView.as_view()),
        name = 'appcc_list'
    ),

    url (
        regex = '^appcc/detalle/(?P<pk>\d+)/$',
        view =  AppccDetalleView.as_view(),
        name = 'appcc_detail'
    ),
    url (
        regex = '^appcc/crear/$',
        view =  'appcc.views.AppccCrearView',
        name = 'appcc_crear'
    ),

    url (
        regex = '^appcc/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(AppccEliminarView.as_view()),
        name = 'appcc_eliminar'
    ),
    url (
        regex = '^appcc/actualizar/(?P<pk>\d+)/$',
        view =   'appcc.views.AppccActualizarView',
        name = 'appcc_actualizar'
    ),
)

#Manual de Auto Control

urlpatterns += patterns('',
    url (
        #regex = '^manualautocontrol/lista/(?P<pappccid>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/$',
        view =  user_passes_test(is_allowed_see)(ManualautocontrolListaView.as_view()),
        name = 'manualautocontrol_list'
    ),

    url (
        #regex = '^manualautocontrol/detalle/(?P<pk>\d+)/$',
        regex = '^appcc/manualautocontrol/detalle/(?P<pk>\d+)/$',
        view =  ManualautocontrolDetalleView.as_view(),
        name = 'manualautocontrol_detail'
    ),
    url (
        #regex = '^manualautocontrol/crear/(?P<pappccid>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/crear/$',
        view =  'appcc.views.ManualautocontrolCrearView',
        name = 'manualautocontrol_crear'
    ),

    url (
        #regex = '^manualautocontrol/eliminar/(?P<pk>\d+)/$',
        regex = '^manualautocontrol/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(ManualautocontrolEliminarView.as_view()),
        name = 'manualautocontrol_eliminar'
    ),
    url (
        #regex = '^manualautocontrol/actualizar/(?P<pk>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/actualizar/(?P<pk>\d+)/$',
        view =   'appcc.views.ManualautocontrolActualizarView',
        name = 'manualautocontrol_actualizar'
    ),
)

#Plan de Auto Control


urlpatterns += patterns('',
    url (
        #regex = '^planautocontrol/lista/(?P<pmanuctrid>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/planautocontrol/(?P<pmanuctrid>\d+)/$',
        view =  user_passes_test(is_allowed_see)(PlanautocontrolListaView.as_view()),
        name = 'planautocontrol_list'
    ),

    url (
        regex = '^planautocontrol/detalle/(?P<pk>\d+)/$',
        view =  PlanautocontrolDetalleView.as_view(),
        name = 'planautocontrol_detail'
    ),
    url (
        #regex = '^planautocontrol/crear/(?P<pmanuctrid>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/planautocontrol/(?P<pmanuctrid>\d+)/crear/$',
        view =  'appcc.views.PlanautocontrolCrearView',
        name = 'planautocontrol_crear'
    ),

    url (
        regex = '^planautocontrol/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(PlanautocontrolEliminarView.as_view()),
        name = 'planautocontrol_eliminar'
    ),
    url (
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/planautocontrol/(?P<pmanuctrid>\d+)/actualizar/(?P<pk>\d+)/$',
        view =   'appcc.views.PlanautocontrolActualizarView',
        name = 'planautocontrol_actualizar'
    ),
)

#Cabeceras de Registros

urlpatterns += patterns('',
    url (
        #regex = '^cabregistros/lista/(?P<pmanautctrid>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/cabregistros/(?P<pmanautctrid>\d+)/$',
        view =  user_passes_test(is_allowed_see)(CabRegistrosListaView.as_view()),
        name = 'cabregistros_list'
    ),

    url (
        regex = '^cabregistros/detalle/(?P<pk>\d+)/$',
        view =  CabRegistrosDetalleView.as_view(),
        name = 'cabregistros_detail'
    ),
    url (
        #regex = '^cabregistros/crear/(?P<pmanautctrid>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/cabregistros/(?P<pmanautctrid>\d+)/crear/$',
        view =  'appcc.views.CabRegistrosCrearView',
        name = 'cabregistros_crear'
    ),

    url (
        regex = '^cabregistros/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(CabRegistrosEliminarView.as_view()),
        name = 'cabregistros_eliminar'
    ),
    url (
        #regex = '^cabregistros/actualizar/(?P<pk>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/cabregistros/(?P<pmanautctrid>\d+)/actualizar/(?P<pk>\d+)/$',
        view =   'appcc.views.CabRegistrosActualizarView',
        name = 'cabregistros_actualizar'
    ),
)


#Detalles Registros

urlpatterns += patterns('',
    url (
        #regex = '^detallesregistros/lista/(?P<pcabregid>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/cabregistros/(?P<pmanautctrid>\d+)/detallesregistros/(?P<pcabregid>\d+)/$',
        view =  user_passes_test(is_allowed_see)(DetallesRegistrosListaView.as_view()),
        name = 'detallesregistros_list'
    ),

    url (
        regex = '^detallesregistros/detalle/(?P<pk>\d+)/$',
        view =  DetallesRegistrosDetalleView.as_view(),
        name = 'detallesregistros_detail'
    ),
    url (
        #regex = '^detallesregistros/crear/(?P<pcabregid>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/cabregistros/(?P<pmanautctrid>\d+)/detallesregistros/(?P<pcabregid>\d+)/crear/$',
        view =  'appcc.views.DetallesRegistrosCrearView',
        name = 'detallesregistros_crear'
    ),

    url (
        regex = '^detallesregistros/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(DetallesRegistrosEliminarView.as_view()),
        name = 'detallesregistros_eliminar'
    ),
    url (
        #regex = '^detallesregistros/actualizar/(?P<pk>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/cabregistros/(?P<pmanautctrid>\d+)/detallesregistros/(?P<pcabregid>\d+)/actualizar/(?P<pk>\d+)/$',
        view =   'appcc.views.DetallesRegistrosActualizarView',
        name = 'detallesregistros_actualizar'
    ),

)

urlpatterns += patterns('',
    url (
        #regex = '^cabanaliticas/lista/(?P<pcabregid>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/cabregistros/(?P<pmanautctrid>\d+)/cabanaliticas/(?P<pcabregid>\d+)/$',
        view =  user_passes_test(is_allowed_see)(CabAnaliticasListaView.as_view()),
        name = 'cabanaliticas_list'
    ),

    url (
        regex = '^cabanaliticas/detalle/(?P<pk>\d+)/$',
        view =  CabAnaliticasDetalleView.as_view(),
        name = 'cabanaliticas_detail'
    ),
    url (
        #regex = '^cabanaliticas/crear/(?P<pcabregid>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/cabregistros/(?P<pmanautctrid>\d+)/cabanaliticas/(?P<pcabregid>\d+)/crear/$',
        view =  'appcc.views.CabAnaliticasCrearView',
        name = 'cabanaliticas_crear'
    ),

    url (
        regex = '^cabanaliticas/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(CabAnaliticasEliminarView.as_view()),
        name = 'cabanaliticas_eliminar'
    ),
    url (
        #regex = '^cabanaliticas/actualizar/(?P<pk>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/cabregistros/(?P<pmanautctrid>\d+)/cabanaliticas/(?P<pcabregid>\d+)/actualizar/(?P<pk>\d+)/$',
        view =   'appcc.views.CabAnaliticasActualizarView',
        name = 'cabanaliticas_actualizar'
    ),

)



urlpatterns += patterns('',
    url (
        #regex = '^documentos/lista/(?P<pmodelo>\w+)/(?P<pid>\d+)/$',
        regex = '^(?P<purl>.*)/documentos/(?P<pmodelo>\w+)/(?P<pid>\d+)/$',
        view =  user_passes_test(is_allowed_see)(DocumentosListaView.as_view()),
        name = 'documentos_list'
    ),

    url (
        regex = '^documentos/detalle/(?P<pk>\d+)/$',
        view =  DocumentosDetalleView.as_view(),
        name = 'documentos_detail'
    ),
    url (
        #regex = '^documentos/crear/(?P<pmodelo>\w+)/(?P<pid>\d+)/$',
        regex = '^(?P<purl>.*)/documentos/(?P<pmodelo>\w+)/(?P<pid>\d+)/crear/$',
        view =  'appcc.views.DocumentosCrearView',
        name = 'documentos_crear'
    ),

    url (
        regex = '^documentos/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(DocumentosEliminarView.as_view()),
        name = 'documentos_eliminar'
    ),
    url (
        regex = '^documentos/actualizar/(?P<pk>\d+)/$',
        view =   'appcc.views.DocumentosActualizarView',
        name = 'documentos_actualizar'
    ),
)

#Relacion Proveedores y Personal

urlpatterns += patterns('',
    url (
        #regex = '^relacionespersonal/lista/(?P<pmanautctrid>\d+)/$',
        #regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/relacionespersonal/(?P<pmanautctrid>\d+)/$',
        #regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/(?P<prelacion>.*)/(?P<pmanautctrid>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/relacionespersonal/(?P<pmanautctrid>\d+)/$',
        view =  user_passes_test(is_allowed_see)(RelacionPersonalListaView.as_view()),
        name = 'relacionpersonal_list',
        kwargs = {'prelacion' : 'relacionespersonal'}
    ),
    url (
        #regex = '^relacionesterceros/lista/(?P<pmanautctrid>\d+)/$',
        #regex = '^relacionesterceros/(?P<pmanautctrid>\d+)/$',
        #regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/(?P<prelacion>.*)/(?P<pmanautctrid>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/relacionesterceros/(?P<pmanautctrid>\d+)/$',
        view =  user_passes_test(is_allowed_see)(RelacionTercerosListaView.as_view()),
        name = 'relacionterceros_list',
        kwargs = {"prelacion":"relacionesterceros"}
    ),

    url (
        regex = '^relaciones/detalle/(?P<pk>\d+)/$',
        view =  RelacionesEntesDetallelView.as_view(),
        name = 'relacionesentes_detail'
    ),
    url (
        #regex = '^relaciones/crear/(?P<pmanautctrid>\d+)/$',
        #regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/relaciones/(?P<pmanautctrid>\d+)/crear/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/(?P<prelacion>.*)/(?P<pmanautctrid>\d+)/crear/$',
        view =  'appcc.views.RelacionesEntesCrearView',
        name = 'relacionesentes_crear'
    ),

    url (
        regex = '^relaciones/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(RelacionesEntesEliminarView.as_view()),
        name = 'relacionesentes_eliminar'
    ),
    url (
        #regex = '^relaciones/actualizar/(?P<pk>\d+)/$',
        #regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/(?P<prelacion>.*)/(?P<pmanuctrid>\d+)/actualizar/(?P<pk>\d+)/$',
        regex = '^appcc/manualautocontrol/(?P<pappccid>\d+)/(?P<prelacion>.*)/(?P<pmanautctrid>\d+)/actualizar/(?P<pk>\d+)/$',
        view =  'appcc.views.RelacionesEntesActualizarView',
        name = 'relacionesentes_actualizar'
    ),
)


#Cuadros Gestion

urlpatterns += patterns('',
    url (
        #regex = 'cuadrosgestion/lista/(?P<pappccid>\d+)/$',
        regex = 'appcc/cuadrosgestion/(?P<pappccid>\d+)/$',
        view =  user_passes_test(is_allowed_see)(CuadrosgestionListaView.as_view()),
        name = 'cuadrosgestion_list'
    ),

    url (
        regex = '^cuadrosgestion/detalle/(?P<pk>\d+)/$',
        view =  CuadrosgestionDetalleView.as_view(),
        name = 'cuadrosgestion_detail'
    ),
    url (
        #regex = '^cuadrosgestion/crear/(?P<pappccid>\d+)/$',
        regex = '^appcc/cuadrosgestion/(?P<pappccid>\d+)/crear/$',
        view =  'appcc.views.CuadrosgestionCrearView',
        name = 'cuadrosgestion_crear'
    ),

    url (
        regex = '^cuadrosgestion/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(CuadrosgestionEliminarView.as_view()),
        name = 'cuadrosgestion_eliminar'
    ),
    url (
        #regex = '^cuadrosgestion/actualizar/(?P<pk>\d+)/$',
        regex = '^appcc/cuadrosgestion/(?P<pappccid>\d+)/actualizar/(?P<pk>\d+)/$',
        view =  'appcc.views.CuadrosgestionActualizarView',
        name = 'cuadrosgestion_actualizar'
    ),
    url (
        #regex = '^cuadrosgestion/hijos/(?P<pappcid>\d+)/(?P<padreid>\d+)/$',
        regex = '^appcc/cuadrosgestion/(?P<pappcid>\d+)/hijos/(?P<padreid>\d+)/$',
        view =   'appcc.views.CuadrogestionHijoCrear',
        name = 'cuadrosgestion_crearhijo'
    ),
    url (
        regex = '^cuadrosgestion/arbol/(?P<empresaid>\d+)/$',
        view =  'appcc.views.CuadrosGestionArbol',
        name =  'cuadrosgestion_arbol'
    ),
)


##Gestor Incindencias
urlpatterns += patterns('',
    url (
        #regex = '^gestorincidencias/lista/(?P<pappccid>\d+)/$',
        regex = '^appcc/gestorincidencias/(?P<pappccid>\d+)/$',
        view =  user_passes_test(is_allowed_see)(GestorincidenciasListaView.as_view()),
        name = 'gestorincidencias_list'
    ),

    url (
        regex = '^gestorincidencias/detalle/(?P<pk>\d+)/$',
        view =  GestorincidenciasDetalleView.as_view(),
        name = 'gestorincidencias_detail'
    ),
    url (
        #regex = '^gestorincidencias/crear/(?P<pappccid>\d+)/$',
        regex = '^appcc/gestorincidencias/(?P<pappccid>\d+)/crear/$',
        view =  'appcc.views.GestorincidenciasCrearView',
        name = 'gestorincidencias_crear'
    ),

    url (
        regex = '^gestorincidencias/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(GestorincidenciasEliminarView.as_view()),
        name = 'gestorincidencias_eliminar'
    ),
    url (
        #regex = '^gestorincindencias/actualizar/(?P<pk>\d+)/$',
        regex = '^appcc/gestorincidencias/(?P<pappccid>\d+)/actualizar/(?P<pk>\d+)/$',
        view  = 'appcc.views.GestorincidenciasActualizarView',
        name  = 'gestorincidencias_actualizar'
    ),
)


##Informes Tecnicos
urlpatterns += patterns('',
    url (
        #regex = '^auditorias/lista/(?P<pappccid>\d+)/$',
        regex = '^appcc/auditorias/(?P<pappccid>\d+)/$',
        view =  user_passes_test(is_allowed_see)(CabInfTecnicosListaView.as_view()),
        name = 'cabinftecnicos_list'
    ),

    url (
        regex = '^auditorias/detalle/(?P<pk>\d+)/$',
        view =  CabInfTecnicosDetalleView.as_view(),
        name = 'cabinftecnicos_detail'
    ),
    url (
        #regex = '^auditorias/crear/(?P<pappccid>\d+)/$',
        regex = '^appcc/auditorias/(?P<pappccid>\d+)/crear/$',
        view =  'appcc.views.CabInfTecnicosCrearView',
        name = 'cabinftecnicos_crear'
    ),

    url (
        regex = '^auditorias/eliminar/(?P<pk>\d+)/$',
        view =  user_passes_test(is_allowed_edit)(CabInfTecnicosEliminarView.as_view()),
        name = 'cabinftecnicos_eliminar'
    ),
    url (
        #regex = '^auditorias/actualizar/(?P<pk>\d+)/$',
        regex = '^appcc/auditorias/(?P<pappccid>\d+)/actualizar/(?P<pk>\d+)/$',
        view  = 'appcc.views.CabInfTecnicosActualizarView',
        name  = 'cabinftecnicos_actualizar'
    ),
)

