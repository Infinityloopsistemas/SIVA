from rest_framework import serializers
from rest_waspmote.models import WaspData

__author__ = 'julian'



class WaspDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WaspData
        fields = ('timestamp_waspmote','status','alt','lat','long','speed','voltage','notes','objects','valorsensor','timestamp_server')


