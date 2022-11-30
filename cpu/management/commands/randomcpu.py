import json

from django.core.management.base import BaseCommand

from cpu.models import Cpu
from cpu.serializers import CpuSerializer


class Command(BaseCommand):
    help = 'Print random cpu'

    def add_arguments(self, parser):
        parser.add_argument('--no-indent', action="store_true")
        parser.add_argument('-i', '--indent', default=4, type=int)

    def handle(self, *args, **options):
        indent = None if options['no_indent'] else options['indent']

        print(options)

        cpu = Cpu.objects.order_by('?').first()
        serializer = CpuSerializer(cpu)

        self.stdout.write(json.dumps(serializer.data, indent=indent))
