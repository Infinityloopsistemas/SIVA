from selectable.registry import registry
from selectable.base import ModelLookup
from gestion.models import OrdenProduccion
from selectable.decorators import login_required


__author__ = 'julian'

class OProduccionLookup(ModelLookup):
    model = OrdenProduccion
    search_fields = ("cuadcampo__descripcion__icontains" )

#    def get_query(self, request, term):
#        results = super(CityLookup, self).get_query(request, term)
#        state = request.GET.get('state', '')
#        if state:
#            results = results.filter(state=state)
#        return results

    def get_item_value(self, item):
        # Display for currently selected item
        return item.cuadcampo.id

    def get_item_label(self, item):
        # Display for choice listings
        return u"%s" % (item.cuadcampo)

#registry.register(OProduccionLookup)