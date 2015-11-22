from django.core.management.base import BaseCommand
#from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


from scores.models import Player, Game, Set
import csv

class Command(BaseCommand):
    args = ""
    help = "Load scores.csv from the data directory. Don't overwrite existing scores!"

    def _getPlayer(self,short_id):
        try:
            player = Player.objects.get(short_id=short_id.upper())
        except ObjectDoesNotExist as e:
            print("Player {} does not exist; Creating.".format(short_id.upper()))
            player = Player()
            player.short_id = short_id.upper()
            player.save()
        return player

    def _getGame(self,scores):
        if scores == ['',''] or scores == ['0','0']:
            return None
        else:
            game = Game()
            game.player1_score = scores[0]
            game.player2_score = scores[1]
            return game

        print("Got scores: {}... {}".format(scores,scores == ['','']))
        pass

    def _makeSet(self,row):
        print("processing: {}".format(row))


        player1 = self._getPlayer(row[1].upper())
        player2 = self._getPlayer(row[2].upper())
        game1 = self._getGame(row[3:5])
        game2 = self._getGame(row[5:7])
        game3 = self._getGame(row[7:9])
        games = [game1, game2, game3]

        s = Set(player1=player1,player2=player2)

        s.game_count = 3
        if not game3:
            s.game_count = 2
        if not game2:
            s.game_count = 1

        s.save()
        for game in games:
            if game:
                game.parent_set = s
                game.save()
        


    def handle(self, *args, **options):
        '''here we will load and parse the file...'''
        score_csv = '/home/gregg/devel/scores/data/scores.csv'
        with open(score_csv,'r') as csvfile:
            reader = csv.reader(csvfile,delimiter=',')
            for row in reader: #Each row is a set
               self._makeSet(row)


