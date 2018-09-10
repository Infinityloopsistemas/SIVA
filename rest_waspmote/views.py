from rest_framework.views import APIView
from rest_waspmote.models import WaspData
from rest_waspmote.serializers import WaspDataSerializer

__author__ = 'julian'


# -*- coding: utf-8 -*-
import logging
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes

logger = logging.getLogger(__name__)

#@api_view(['POST'])
@permission_classes((AllowAny, ))
class LoadWaspMoteViewSet(APIView):
    authentication_classes = ( BasicAuthentication, TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    model =WaspData
    serializer_class = WaspDataSerializer

    def get_queryset(self):
        queryset = WaspData.objects.all()[:0]
        pid = self.request.query_params.get('pid', None)
        if pid is not None:
            queryset = queryset.filter(pk=pid)
        return queryset

    def post(self, request):
        #datos = request.FILES["owServerData"]
        logger.debug("Recepcion de datos")
        logger.debug(request.FILES)
        print request.FILES
        return Response(  status=status.HTTP_200_OK)