from django.core.management.base import BaseCommand
from django.db.models import Count

from motherboard.models import Motherboard


class Command(BaseCommand):
    help = 'Print motherboards count'

    def handle(self, *args, **options):
        count = Motherboard.objects.aggregate(count=Count('id'))['count']

        self.stdout.write(f'There are {count} motherboard{"s" if count > 1 else ""}')
