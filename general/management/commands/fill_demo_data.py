from django.core.management.base import BaseCommand, CommandError
from pc_rest import demo_data


class Command(BaseCommand):
    help = 'Fill database with demo data'

    def add_arguments(self, parser):
        parser.add_argument('model_names', nargs='*', type=str)

    def handle(self, *args, **options):
        model_names = options['model_names']
        if len(model_names) == 0:
            self.stdout.write(self.style.SUCCESS('Filled database with demo data'))
            demo_data.main()
            return 0

        for model_name in model_names:
            formated_model_name = model_name.replace('_', '').lower()
            add_func = getattr(demo_data, f'add_{formated_model_name}', None)
            if add_func:
                self.stdout.write(self.style.SUCCESS(f'Fill database with {formated_model_name} model demo data'))
                add_func()
            else:
                raise CommandError(f'{model_name} does not exits')
