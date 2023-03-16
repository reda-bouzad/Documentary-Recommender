from django.core.management.base import BaseCommand
from chatterbot.ext.django_chatterbot.models import Statement, Tag


class Command(BaseCommand):
    help = "Clear the database"

    def handle(self, *args, **options):
        Statement.objects.all().delete()
        Tag.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Successfull!"))