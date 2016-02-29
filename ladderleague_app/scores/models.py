from django.db import models
from scores.exceptions import *

# Create your models here.


class Player(models.Model):
    """Represent an individual player."""
    short_id = models.CharField(
        max_length=100,
        primary_key=True,
        default="CHUMP"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    handle = models.CharField(max_length=100)
    origin = models.CharField(
        max_length=100,
        default="Parts unknown, Planet Earth"
    )

    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ladder_rank = models.FloatField(default=0)

    def __str__(self):
        return self.short_id


class Contest(models.Model):
    """Represet a series of games; a single contest between two players."""
    challenger = models.ForeignKey(Player, related_name='challenger_set')
    challengee = models.ForeignKey(Player, related_name='challengee_set')

    def __str__(self):
        """Describe the matchup."""
        return "{} vs {}".format(self.challenger, self.challengee)

    def winner(self):
        """
        Return the player that won this contest.
        :return: An instance of Player representing the player who won.
        """
        games = self.game_set.all()
        challenger_wins = 0
        challengee_wins = 0
        for game in games:
            if game.challenger_score > game.challengee_score:
                challenger_wins += 1
            elif game.challengee_score > game.challenger_score:
                challengee_wins += 1
        if challenger_wins > challengee_wins:
            return self.challenger
        elif challengee_wins > challenger_wins:
            return self.challengee
        else:
            raise UndefinedOutcomeError

    def outcome(self, player):
        if self.challenger != player and self.challengee != player:
            raise NonParticipantError

        try:
            if self.winner() == player:
                return "win"
            else:
                return "loss"
        except UndefinedOutcomeError:
            return "draw"

    def opponent(self, player):
        if player == self.challenger:
            return self.challengee
        elif player == self.challengee:
            return self.challenger
        else:
            raise NonParticipantError


class Game(models.Model):
    """Represent a single game (part of a larger Contest)"""
    challenger_score = models.IntegerField()
    challengee_score = models.IntegerField()
    parent_contest = models.ForeignKey(Contest, null=False)

    def __str__(self):
        """Describe the game"""
        return "{}/{}".format(self.challenger_score, self.challengee_score)
