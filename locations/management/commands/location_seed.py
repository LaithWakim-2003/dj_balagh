from django.core.management.base import BaseCommand
from ...utils import generate_governorates,generate_syria_governorates_and_cities

class Command(BaseCommand):
    help = 'generate govenorates'
    def handle(self, *args, **options):
        generate_syria_governorates_and_cities()
        self.stdout.write(self.style.SUCCESS('Successfully created governorates and cities'))
