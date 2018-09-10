from simplejson.encoder import JSONEncoder
from django.utils import simplejson
from Produccion.models import DetProcesos, TiposProcesos, CabProcesos

__author__ = 'julian'
from django.db import connection
from dajax.core.Dajax import Dajax
from dajaxice.core import dajaxice_functions
from elementtree.ElementTree import  Element
import elementtree.ElementTree as ET




def objetoProcesos(head,id,customid,vertex,parent,texto):
    subhead = ET.SubElement(head,"mxCell")
    subhead.set("id",id)
    subhead.set("customId",customid)
    subhead.set("value",'<img src="editors/images/overlays/workplace.png"><br><b> %s </b> ' % texto )
    subhead.set("vertex",vertex)
    subhead.set("parent",parent)
    subele = Element("mxGeometry")
    subele.set("x","0")
    subele.set("y","0")
    subele.set("width","180")
    subele.set("height","70")
    subele.set("as","geometry")
    subhead.append(subele)
    return head

def enlaceProceso(head,id,customid,edge,parent,source,target,texto):
    subhead = ET.SubElement(head,"mxCell")
    subhead.set("id","edge-"+id)
    subhead.set("customId","edge-"+customid)
    subhead.set("value",'<img src="editors/images/overlays/check.png"> %s' % texto )
    subhead.set("edge",edge)
    subhead.set("parent",parent)
    subhead.set("source",source)
    subhead.set("target",target)
    subele = Element("mxGeometry")
    subele.set("relative","1")
    subele.set("as","geometry")
    subhead.append(subele)




def consultaDetalleProduccion(request,nrec):
#def consultaDetalleProduccion(ncab):
    dajax   = Dajax()
    nrec   = DetProcesos.objects.filter(cabprocesos=CabProcesos.objects.get(pk=ncab))[0].id
    raiz   = DetProcesos.get_root(DetProcesos.objects.get(pk=nrec)).id
    size   = DetProcesos.get_descendant_count(DetProcesos.objects.get(id=raiz))+1
    print raiz
    padre  = DetProcesos.objects.get(id=raiz)
    cpadre = str(raiz)
    #Cabecera del Mensaje
    root = ET.Element("mxGraphModel")
    head = ET.SubElement(root,"root")
    ele  = Element("mxCell")
    ele.set("id","0")
    head.append(ele)
    ele1  = Element("mxCell")
    ele1.set("id",cpadre)
    ele1.set("parent","0")
    head.append(ele1)
    objetoProcesos(head,str(raiz+1),str(raiz+1),str(raiz),str(raiz),padre.descripcion)
    print padre.descripcion
    nid  = raiz
    for ele in range(0,size-1):
        obj  =DetProcesos.get_children(DetProcesos.objects.get(id=nid))
        if len(obj) != 0:
            objetoProcesos(head,str(nid+2),str(nid+2),cpadre,cpadre,obj.values()[0]['descripcion'])
            print obj.values()[0]['descripcion']
            nid =obj.values()[0]['id']

    nid   = raiz
    cpadre= str(raiz+1)
    for ele in range(0,size-1):
        obj  =DetProcesos.get_children(DetProcesos.objects.get(id=nid))
        if len(obj) != 0:
            nid =obj.values()[0]['id']
            dest=nid+1
            enlaceProceso(head,str(nid+2),str(nid+2),str(raiz),str(raiz),cpadre,str(dest),TiposProcesos.objects.get(id=obj.values()[0]['tproceso_id']))
            cpadre=str(dest)

    valores= simplejson.dumps(ET.tostring(root),cls = JSONEncoder)
    #tree = ET.ElementTree(root)
    #tree.write("salida.xml")
    return valores

