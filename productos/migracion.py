import cx_Oracle
import unicodedata
from django.core.exceptions import ObjectDoesNotExist
from Productos.models import Grupos, Familias, Especies, PartidasArancelarias, Tipos, UnidadesMedidas, Canales, Marcas, TiposEnvases, Dimensiones, Productos
import os
os.environ["NLS_LANG"] = ".AL32UTF8"
__author__ = 'julian'


def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def leeEspecies():
    connectionMaestros      = cx_Oracle.connect("maestros", "maestros","oracle.world", threaded = True)
    #sql  = "select esp.descripcion, dcientifico,dingles,dfrances,ditaliano,dotros,fam.descripcion,grp.descripcion, par.descripcion from especies esp, familias fam, grupos grp, partidas_arancelarias par where familia_familia_id = familia_id and fam.grupo_grupo_id= grp.grupo_id and esp.p_arancela_p_arancela_id = par.p_arancela_id"
    #sql   = "select familias.descripcion, grupos.descripcion from familias, grupos where grupo_grupo_id = grupo_id"
    #sql  = "select descripcion  from grupos"
    #sql  = "select  descripcion , codigo_estadistico from partidas_arancelarias"
    #sql   = "select descripcion from tipos"
    #sql    = "select descripcion from unidades_medidas "
    #sql    = "select descripcion from canales"
    #sql    = "select * from marcas"
    #sql     = "select descripcion,f_master,peso_ud,peso_envase,agranel,volumen from envases"
    #sql     = "select dim.descripcion,dim.maximo,dim.minimo,dim.piezas,uni.descripcion from dimensiones dim, unidades_medidas uni where u_medida_id= u_medida_u_medida_id"
    sql = "select  dim.descripcion,esp.descripcion,tip.descripcion,codigo_barra,nvl(can.descripcion,'---') canal,  env.descripcion, NVL(elaborado,'N'), nvl(mar.descripcion,'---') marcas, estado, fecha_baja, codarticulo , env.f_master from mercancias mer , dimensiones dim , especies esp , tipos tip , canales can, envases env ,marcas mar where mer.especie_especie_id = esp.especie_id and  mer.tipo_tipo_id            = tip.tipo_id and  mer.marca_marca_id(+)    = mar.marca_id and  mer.envase_envase_id  = env.envase_id and  mer.dimension_dimension_id = dim.dimension_id"
    cursor= connectionMaestros.cursor()
    cursor.execute(sql)
    array=[]
    array= cursor.fetchall()

#    for partidas in array:
#        PartidasArancelarias.objects.create( descripcion= partidas[0],codigo_estadistico = partidas[1])

#    for grupos in array:
#        Grupos.objects.create(descripcion=grupos[0])

#    for descrip in array:
#        print "Descripcion %s " % descrip[0]
#        Familias.objects.create(descripcion=descrip[0],grupo_grupo=Grupos.objects.get(descripcion=descrip[1]))

#

#    for especies in array:
#            uespecies = []
#            i=0
#            for x in especies:
#                if x is None:
#                    uespecies.append(elimina_tildes(unicode(x)))
#                else:
#                    print x
#                    uespecies.append(elimina_tildes(unicode(x.decode('utf-8'))))
#            Especies.objects.create(descripcion=uespecies[0],dcientifico=uespecies[1],denglish=uespecies[2],dfrench=uespecies[3],ditalian=uespecies[4],dotros=uespecies[5],familia_familia=Familias.objects.get(descripcion=uespecies[6], grupo_grupo=Grupos.objects.get(descripcion=uespecies[7])), p_arancela_p_arancela = PartidasArancelarias.objects.filter(descripcion=uespecies[8])[0])

#    for tipos in array:
#        Tipos.objects.create(descripcion=tipos[0])
#
#    for umedidas in array:
#        UnidadesMedidas.objects.create(descripcion=umedidas[0])

#    for ucanales in array:
#        Canales.objects.create(descripcion = ucanales[0])
#
#    for umarcas in array:
#        Marcas.objects.create(descripcion = umarcas)

#    for tpenv in array:
#         if tpenv[0] is None:
#             cdesc="."
#         else:
#            cdesc=tpenv[0]
#         TiposEnvases.objects.create(descripcion=cdesc,f_master=tpenv[1],peso_ud=tpenv[2],peso_envase=tpenv[3],agranel=tpenv[4],volumen=tpenv[5])

#    for dime in array:
#        Dimensiones.objects.create(descripcion=dime[0],maximo=dime[1],minimo=dime[2],piezas=dime[3],u_medida_u_medida = UnidadesMedidas.objects.get(descripcion=dime[4]))

    for prod in array:
        print prod
        try:
            espe  = Especies.objects.get(descripcion=prod[1])
            try:
                dime  = Dimensiones.objects.get(descripcion=prod[0])
            except  ObjectDoesNotExist:
                pass

            tipos = Tipos.objects.get(descripcion=prod[2])
            try:
                can   = Canales.objects.get(descripcion=prod[4])
            except  ObjectDoesNotExist:
                pass
            try:
                enva  = TiposEnvases.objects.get(descripcion=prod[5],f_master=prod[11])
            except  ObjectDoesNotExist:
                pass
            try:
                marc  = Marcas.objects.get(descripcion=prod[7])
            except  ObjectDoesNotExist:
                pass

            Productos.objects.create(dimension=dime
                                 ,especie=espe,
                                  tipo   =tipos,
                                  codigo_barra = prod[3],
                                  canal = can,
                                  envase = enva,
                                  elaborado = prod[6],
                                  marca = marc,
                                  estado = prod[8],
                                  codarticulo = prod[10])
        except  ObjectDoesNotExist:
            pass