from rest_framework import serializers
from cpu.models import Cpu, Series
from general.serializers import ManufacturerSerializer, SocketTypeSerializer, SocketSerializer


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('id', 'title')


class CpuSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='__str__')
    manufacturer = ManufacturerSerializer(many=False)
    series = SeriesSerializer(many=False)
    socket = SocketSerializer(many=False)

    class Meta:
        model = Cpu
        fields = ('id', 'title', 'manufacturer', 'series', 'version', 'socket', 'cores', 'threads')


class CpuShortSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='__str__')
    socket = serializers.CharField(source='socket.title')

    class Meta:
        model = Cpu
        fields = ('id', 'title', 'socket', 'cores', 'threads')
