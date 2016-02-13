from django.core.management.base import BaseCommand
#from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


from scores.models import Player, Game, Set
import csv

class Command(BaseCommand):
    args = ""
    help = "Load players.csv from the data directory. Updates players with whatever is found there"

    def _updateUser(self, row):
        try:
            player = Player.objects.get(short_id=row[0])
        except ObjectDoesNotExist:
            print("No player with shortID {}".format(row[0])) 
            return
        player.first_name = row[1] 
        player.last_name = row[2]
        if row[3] != "":
            player.handle = row[3]
        player.hometown = row[4] + ", " + row[5]
        player.save()


    def handle(self, *args, **options):
        '''here we will load and parse the file...'''
        player_csv = '/home/gregg/devel/greggcorp/ladderleague/data/players.csv'
        with open(player_csv,'r') as csvfile:
            reader = csv.reader(csvfile,delimiter=',')
            for row in reader: #Each row is a set
               self._updateUser(row)


