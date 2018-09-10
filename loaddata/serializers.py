# -*- coding: utf-8 -*-
from loaddata.models import LoadDataDevice

__author__ = 'julian'

from rest_framework import serializers


class LoadDataDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoadDataDevice
        fields = ('PollCount', 'DevicesConnected', 'LoopTime', 'DevicesConnectedChannel1','DevicesConnectedChannel2','DevicesConnectedChannel3','VoltageChannel1','VoltageChannel2','VoltageChannel3','VoltagePower','DeviceName','HostName','MACAddress' )


