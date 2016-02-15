from django.core.management.base import BaseCommand
#from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import django.conf

from scores.models import Player, Game, Contest 
import csv
import os

class Command(BaseCommand):
    args = ""
    help = "Load scores.csv from the data directory. Don't overwrite existing scores!"

    def _getPlayer(self,short_id):
        try:
            print("Retrieving player with ID: {}".format(short_id.upper()))
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

    def _makeContest(self,row):
        print("processing: {}".format(row))


        player1 = self._getPlayer(row[1].upper())
        player2 = self._getPlayer(row[2].upper())
        game1 = self._getGame(row[3:5])
        game2 = self._getGame(row[5:7])
        game3 = self._getGame(row[7:9])
        games = [game1, game2, game3]

        contest = Contest(
            challenger=player1,
            challengee=player2,
            contest_id=int(row[0])
        )

        contest.game_count = 3
        if not game3:
            contest.game_count = 2
        if not game2:
            contest.game_count = 1

        contest.save()
        for game in games:
            if game:
                game.parent_set = contest 
                game.save()
        


    def handle(self, *args, **options):
        '''here we will load and parse the file...'''
        score_csv = os.path.join(django.conf.settings.DATA_DIR,'scores.csv')
        try:
            with open(score_csv,'r') as csvfile:
                reader = csv.reader(csvfile,delimiter=',')
                for row in reader: #Each row is a set
                   self._makeContest(row)
        except FileNotFoundError:
            print("Couldn't open {}, aborting.".format(score_csv))


