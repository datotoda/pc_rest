from rest_framework import serializers

from general.serializers import ManufacturerSerializer, SocketSerializer, MemoryTypeSerializer, FormFactorSerializer
from motherboard.models import Motherboard, Chipset


class ChipsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chipset
        fields = ('id', 'title')


class MotherboardSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='__str__')
    manufacturer = ManufacturerSerializer(many=False)
    socket = SocketSerializer(many=False)
    form_factor = FormFactorSerializer(many=False)
    memory_type = MemoryTypeSerializer(many=False)
    chipset = ChipsetSerializer(many=False)

    class Meta:
        model = Motherboard
        fields = ('id', 'title', 'manufacturer', 'socket', 'form_factor', 'chipset',
                  'memory_type', 'memory_slots', 'max_memory')


class MotherboardShortSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='__str__')
    socket = serializers.CharField(source='socket.title')
    form_factor = serializers.CharField(source='form_factor.title')
    memory_type = serializers.CharField(source='memory_type.title')

    class Meta:
        model = Motherboard
        fields = ('id', 'title', 'socket', 'form_factor', 'memory_type')
