# -*- coding: utf-8 -*-
import logging
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from loaddata.models import LoadDataDevice, LoadDataSensor, TrackTemperaturas, TrackSondas
from loaddata.serializers import  LoadDataDeviceSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
import xml.etree.ElementTree as ET
from rest_framework.decorators import api_view, permission_classes

logger = logging.getLogger(__name__)

#@api_view(['POST'])
@permission_classes((AllowAny, ))
class LoadDataDeviceViewSet(ListCreateAPIView):

    authentication_classes = ( BasicAuthentication, TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    model =LoadDataDevice
    serializer_class = LoadDataDeviceSerializer

    def get_queryset(self):
        queryset = LoadDataDevice.objects.all()[:0]
        pid = self.request.query_params.get('pid', None)
        if pid is not None:
            queryset = queryset.filter(pk=pid)
        return queryset

    def post(self, request, format='xml'):
        datos = request.FILES["owServerData"]
        logger.debug("Recepcion de datos")
        root  = ET.fromstring(datos.read())
        reg={}
        address=""
        for i in range(16):
            if root[i].tag == 'MACAddress':
                address = root[i].text
            if i==0:
                reg={ root[i].tag : root[i].text }
            else:
                reg.update({root[i].tag : root[i].text})

        #Alta del Sensor
        objtrack =TrackTemperaturas.objects.get(MACAddress=address)
        reg.update({'tracktemp_id': int(objtrack.id) , 'empresa_id': int(objtrack.empresa_id) } )
        logger.debug("Comprueba que existe track")
        if objtrack:
            logger.debug("Entra en Track")
            objidM=LoadDataDevice.objects.create(**reg)
            idM= objidM.id
            reg={'loadatadevice_id': idM }
            logger.debug("Id de loaddataDevice %s" % idM);
            romid=""
            numsens = int(objidM.DevicesConnected)
            sensores =[16,17,18]
            s=0
            for s in range(numsens):
                for i in range(8):
                    if root[sensores[s]][i].tag != 'RawData':
                        reg.update({root[sensores[s]][i].tag : root[sensores[s]][i].text})
                    if root[16][i].tag == 'ROMId':
                        romid =root[sensores[s]][i].text
                objsensor = TrackSondas.objects.get(ROMId=romid)
                if objsensor:
                    reg.update({'tracksonda_id' : objsensor.id })
                    logger.debug(reg)
                    LoadDataSensor.objects.create(**reg)

        return Response(  status=status.HTTP_200_OK)





