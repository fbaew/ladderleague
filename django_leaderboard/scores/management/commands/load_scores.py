from django.core.management.base import BaseCommand
#from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


from scores.models import Player, Game, Set
import csv

class Command(BaseCommand):
    args = ""
    help = "Load scores.csv from the data directory. Don't overwrite existing scores!"

    def handle(self, *args, **options):
        '''here we will load and parse the file...'''
        score_csv = '/home/gregg/devel/scores/data/scores.csv'
        with open(score_csv,'r') as csvfile:
            reader = csv.reader(csvfile,delimiter=',')
            for row in reader: #Each row is a set
               self._makeSet(row)

    def _makeSet(self,row):
        print("processing: {}".format(row))
        player1 = self._getPlayer(row[1].upper())
        player2 = self._getPlayer(row[2].upper())

    def _getPlayer(self,short_id):
        try:
            player = Player.objects.get(short_id=short_id.upper())
        except ObjectDoesNotExist as e:
            print("Player {} does not exist; Creating.".format(short_id.upper()))
            player = Player()
            player.short_id = short_id.upper()
            player.save()    

