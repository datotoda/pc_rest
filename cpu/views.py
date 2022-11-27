from django.db.models import F, Count, Max, Min, Value, Case, When, Q, Subquery, OuterRef
from django.db.models.functions import Concat
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cpu.models import Cpu
from cpu.serializers import CpuSerializer, CpuShortSerializer
from motherboard.models import Motherboard


class CpuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cpu.objects.select_related('manufacturer', 'series', 'socket', 'socket__socket_type')

    def get_serializer_class(self, detail=False):
        if self.action in ['retrieve', 'random_cpu']:
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

        return Response({'additional_data': additional_data, 'cpus': serializer.data})

    @action(detail=False)
    def cores_detail(self, request):
        cores_detail_data = self.get_queryset().annotate(
                title=Concat(F('manufacturer__title'), Value(' '), F('series__title'), Value(' '), F('version'))
            ).values('id', 'title', 'threads').annotate(
                performance_cores=F('threads') - F('cores'),
                efficient_cores=Case(
                    When(Q(manufacturer__title='Intel') & (Q(version__startswith='13') | Q(version__startswith='12')),
                         then=F('cores') * 2 - F('threads')),
                    default=None
                )
            )

        return Response(cores_detail_data)

    @action(detail=False)
    def random_cpu(self, request):
        all_cpu_qs = self.get_queryset()
        random_cpu_qs = all_cpu_qs.order_by('?').first()
        serializer = self.get_serializer(random_cpu_qs, many=False)

        additional_data = all_cpu_qs.aggregate(
            same_manufacturer_cpus_count=Count('id', Q(manufacturer=random_cpu_qs.manufacturer)),
            same_series_cpus_count=Count('id', Q(series=random_cpu_qs.series)),
            same_socket_cpus_count=Count('id', Q(socket=random_cpu_qs.socket))
        )

        return Response({'additional_data': additional_data, 'cpu': serializer.data})

    @action(detail=False)
    def compatible_motherboards(self, request):
        all_cpu_qs = self.get_queryset()

        motherboards_sb_qs = Motherboard.objects.filter(socket=OuterRef('socket')).values('id').annotate(
            title=Concat(F('manufacturer__title'), Value(' '), F('title'))
        ).order_by('?')

        result = all_cpu_qs.values('id').annotate(
            cpu=Concat(F('manufacturer__title'), Value(' '), F('series__title'), Value(' '), F('version')),
            motherboard=Subquery(motherboards_sb_qs.values('title')[:1])
        )

        return Response(result)
