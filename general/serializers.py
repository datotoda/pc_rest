from rest_framework import serializers
from general.models import Manufacturer, SocketType, Socket, FormFactor, MemoryType


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'title', 'link')


class SocketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocketType
        fields = ('id', 'title')


class SocketSerializer(serializers.ModelSerializer):
    socket_type = serializers.CharField(source='socket_type.title')

    class Meta:
        model = Socket
        fields = ('id', 'title', 'socket_type', 'pins')


class FormFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFactor
        fields = ('id', 'title')


class MemoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryType
        fields = ('id', 'title')
