__author__ = 'julian'


class ProductosLookup(object):
    def get_query(self,q,request):
        return VProductos.objects.filter(descripcion__icontains=q,fecha_baja=None )
    def format_result(self,objeto):
        return u"%s" % (objeto.descripcion)
    def format_item(self,objeto):
        return unicode(objeto.descripcion)
    def get_objects(self,ids):
        return VMercancias.objects.filter(pk__in=ids)