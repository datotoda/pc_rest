from rest_framework import serializers
from cpu.models import Cpu, Manufacturer, Series, SocketType, Socket


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'title', 'link')


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('id', 'title')


class SocketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocketType
        fields = ('id', 'title')


class SocketSerializer(serializers.ModelSerializer):
    socket_type = SocketTypeSerializer(many=False)

    class Meta:
        model = Socket
        fields = ('id', 'title', 'socket_type', 'pins')


class CpuSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='__str__')
    manufacturer = ManufacturerSerializer(many=False)
    series = SeriesSerializer(many=False)
    socket = SocketSerializer(many=False)

    class Meta:
        model = Cpu
        fields = ('id', 'title', 'manufacturer', 'series', 'version', 'socket', 'cores', 'threads')
