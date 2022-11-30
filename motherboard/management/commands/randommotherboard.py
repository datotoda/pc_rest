import json

from django.core.management.base import BaseCommand

from motherboard.models import Motherboard
from motherboard.serializers import MotherboardSerializer


class Command(BaseCommand):
    help = 'Print random motherboard'

    def add_arguments(self, parser):
        parser.add_argument('--no-indent', action="store_true")
        parser.add_argument('-i', '--indent', nargs='?', type=int)

    def handle(self, *args, **options):
        indent = None if options['no_indent'] else options['indent'] if options['indent'] else 4

        print(options)

        motherboard = Motherboard.objects.order_by('?').first()
        serializer = MotherboardSerializer(motherboard)

        self.stdout.write(json.dumps(serializer.data, indent=indent))
