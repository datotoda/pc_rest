from django.db.models import F, Count, Max, Min
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cpu.models import Cpu
from cpu.serializers import CpuSerializer, CpuShortSerializer


class CpuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cpu.objects.select_related('manufacturer', 'series', 'socket', 'socket__socket_type')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CpuSerializer
        return CpuShortSerializer

    @action(detail=False)
    def hyperthread(self, request):
        hyperthread_qs = self.get_queryset().filter(threads=F('cores') * 2)
        serializer = self.get_serializer(hyperthread_qs, many=True)

        additional_data = [
            hyperthread_qs.aggregate(count=Count('id'), min_threads=Min('threads'), max_threads=Max('threads')),
            hyperthread_qs.annotate(brand=F('manufacturer__title')).values('brand').annotate(count=Count('id')),
        ]

        return Response([{'additional_data': additional_data}] + serializer.data)
