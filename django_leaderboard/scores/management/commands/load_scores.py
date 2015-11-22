from django.core.management.base import BaseCommand
#from django.utils import timezone
from scores.models import Player, Game, Set
import csv

class Command(BaseCommand):
    args = ""
    help = "Load scores.csv from the data directory. Don't overwrite existing scores!"

    def handle(self, *args, **options):
        '''here we will load and parse the file...'''

        with open('/home/gregg/devel/scores/data/scores.csv','r') as csvfile:
            reader = csv.reader(csvfile,delimiter=',')
            for row in reader:
                print(row)
