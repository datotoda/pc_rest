from rest_framework import viewsets
from cpu.models import Cpu
from cpu.serializers import CpuSerializer


class CpuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cpu.objects.select_related('manufacturer', 'series', 'socket', 'socket__socket_type')
    serializer_class = CpuSerializer
