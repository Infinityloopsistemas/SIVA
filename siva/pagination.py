__author__ = 'julian'
from rest_framework.compat import OrderedDict
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class DstorePagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        print "Entra en paginado"
        return Response(OrderedDict([
            ('total', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('items', data )
        ]))
