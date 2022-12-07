from django.core.management.base import BaseCommand
from django.db.models import Count

from cpu.models import Cpu


class Command(BaseCommand):
    help = 'Print cpus count'

    def handle(self, *args, **options):
        count = Cpu.objects.aggregate(count=Count('id'))['count']

        self.stdout.write(f'There are {count} cpu{"s" if count > 1 else ""}')
