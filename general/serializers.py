from rest_framework import serializers
from general.models import Manufacturer, SocketType, Socket


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'title', 'link')


class SocketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocketType
        fields = ('id', 'title')


class SocketSerializer(serializers.ModelSerializer):
    socket_type = SocketTypeSerializer(many=False)

    class Meta:
        model = Socket
        fields = ('id', 'title', 'socket_type', 'pins')
