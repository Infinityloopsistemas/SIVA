import datetime
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer

__author__ = 'julian'
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions, filters, viewsets
from rest_framework_jsonp.renderers import JSONPRenderer
from loaddata.models import  LoadDataSensor
from rest_loaddata.serializers import LoadDataSensorSerialize



class LoadDataSensorViewSet(viewsets.ModelViewSet):

    renderer_classes = (JSONRenderer,)
    queryset = LoadDataSensor.objects.all()
    authentication_classes = ( BasicAuthentication, TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)



    def list(self,request):
        empid    = self.request.query_params.get('empid', None)
        queryset = self.queryset.filter(loadatadevice__empresa__id=empid).order_by('date')
        serializer = LoadDataSensorSerialize(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request):
        empid   = self.request.query_params.get('empid', None)
        fecha   = self.request.query_params.get('fecha', None)
        selmes  = self.request.query_params.get('selmes', None)
        idsonda = self.request.query_params.get('idsonda', None)



        if idsonda is None:
            return Response(None)

        if fecha is not None:
            dia= int(fecha[:2])
            mes= int(fecha[2:4])
            ano= int(fecha[4:])
            finicia = datetime.datetime(ano,mes,dia,0,0)
            ffin     = datetime.datetime(ano,mes,dia,23,59)
        if selmes is not None:
            mes= int(selmes[:2])
            ano= int( selmes[2:])
            finicia = datetime.datetime(ano,mes,1,0,0)
            if mes== 12:
                mes =1
            else:
                mes = mes+1
            ffin    = datetime.datetime(ano,mes,1,0,0) - datetime.timedelta(days=1)

        datasensor = self.queryset.filter(loadatadevice__empresa__id=empid,date__range=[finicia,ffin],tracksonda__id=idsonda).order_by('date')


        if datasensor.first():
            serializer = LoadDataSensorSerialize(datasensor,many=True)
        else:
            return Response(None)
        return Response(serializer.data)


#/rest_maestros/terceros/ -H 'Authorization: Token aeb251c825176a8351e447fe1f49c5b6353056a7