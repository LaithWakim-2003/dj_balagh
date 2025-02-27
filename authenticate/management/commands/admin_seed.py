from django.core.management.base import BaseCommand
from ...utils import create_super_user

class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        create_super_user()
        self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
