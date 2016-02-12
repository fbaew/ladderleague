from django.core.management.base import BaseCommand
#from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from scores.exceptions import *

from scores.models import Player, Game, Set
import csv

class Command(BaseCommand):
    args = ""
    help = "Calculates basic statistics for all players"

    def handle(self, *args, **options):
        '''Clear everyone's regulation wins, and repopulate.'''
        for player in Player.objects.all():
            player.regulation_wins = 0
            player.regulation_losses = 0
            player.save()
        for contest in Set.objects.all():
            try:
                winner = contest.winner()
                loser = contest.opponent(winner)
                print("winner: {}".format(winner))
                winner.regulation_wins += 1
                winner.save()
                loser.regulation_losses += 1
                loser.save()
            except UndefinedOutcomeError:
                pass

        for player in Player.objects.all():
            player.elo_rating = \
                (player.regulation_wins+1.0)/(player.regulation_losses+1.0)
            player.save()
