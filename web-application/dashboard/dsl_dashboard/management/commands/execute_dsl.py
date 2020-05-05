from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Execute dsl commands through management commands"