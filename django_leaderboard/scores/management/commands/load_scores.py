from django.core.management.base import BaseCommand
#from django.utils import timezone
from scores.models import Player, Game, Set

class Command(BaseCommand):
    args = ""
    help = "Load scores.csv from the data directory. Don't overwrite existing scores!"

    def handle(self, *args, **options):
        '''here we will load and parse the file...'''
        print("Not yet implemented, dawg.")
        pass
