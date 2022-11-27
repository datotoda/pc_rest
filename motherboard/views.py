from rest_framework import viewsets
from motherboard.models import Motherboard
from motherboard.serializers import MotherboardSerializer, MotherboardShortSerializer


class MotherboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Motherboard.objects.select_related('manufacturer', 'socket', 'socket__socket_type',
                                                  'form_factor', 'memory_type', 'chipset')

    def get_serializer_class(self, detail=False):
        if self.action == 'retrieve':
            return MotherboardSerializer
        return MotherboardShortSerializer
