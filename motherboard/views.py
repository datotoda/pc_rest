from django.db.models import Count, Q, F, Value
from django.db.models.functions import Concat
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from motherboard.models import Motherboard
from motherboard.serializers import MotherboardSerializer, MotherboardShortSerializer


class MotherboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Motherboard.objects.select_related('manufacturer', 'socket', 'socket__socket_type',
                                                  'form_factor', 'memory_type', 'chipset')

    def get_serializer_class(self, detail=False):
        if self.action in ['retrieve', 'random_motherboard']:
            return MotherboardSerializer
        return MotherboardShortSerializer

    @action(detail=False)
    def random_motherboard(self, request):
        all_motherboard_qs = self.get_queryset()
        random_motherboard_qs = all_motherboard_qs.order_by('?').first()
        serializer = self.get_serializer(random_motherboard_qs, many=False)

        additional_data = all_motherboard_qs.aggregate(
            same_manufacturer_motherboards_count=Count('id', Q(manufacturer=random_motherboard_qs.manufacturer)),
            same_socket_motherboards_count=Count('id', Q(socket=random_motherboard_qs.socket)),
            same_memory_type_motherboards_count=Count('id', Q(memory_type=random_motherboard_qs.memory_type)),
            same_form_factor_motherboards_count=Count('id', Q(form_factor=random_motherboard_qs.form_factor)),
            same_chipset_motherboards_count=Count('id', Q(chipset=random_motherboard_qs.chipset)),
        )

        return Response({'additional_data': additional_data, 'motherboard': serializer.data})

    @action(detail=False)
    def summary(self, request):

        all_motherboard_qs = self.get_queryset()

        result = {
            'by_manufacturer': all_motherboard_qs.values('id').annotate(manufacturer=F('manufacturer__title'))
            .values('manufacturer').annotate(count=Count('manufacturer')),
            'by_socket': all_motherboard_qs.values('id').annotate(socket=F('socket__title'))
            .values('socket').annotate(count=Count('socket')),
            'by_form_factor': all_motherboard_qs.values('id').annotate(socket=F('form_factor__title'))
            .values('form_factor').annotate(count=Count('form_factor')),
            'by_memory_type': all_motherboard_qs.values('id').annotate(socket=F('memory_type__title'))
            .values('memory_type').annotate(count=Count('memory_type')),

        }

        return Response(result)

    @action(detail=True)
    def compatible_parts(self, request, pk=None):

        motherboard = self.get_object()

        result = {
            'cpus': motherboard.socket.cpus.select_related('manufacturer', 'series').annotate(
                title=Concat(F('manufacturer__title'), Value(' '), F('series__title'), Value(' '), F('version'))
            ).values('id', 'title')
        }

        return Response(result)
