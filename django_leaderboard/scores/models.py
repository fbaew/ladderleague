"""
Models for our scorekeeping app
"""
from django.db import models
from scores.exceptions import NonParticipantError, UndefinedOutcomeError

# Create your models here.

class Player(models.Model):
    """
    Model representing individual ping pong players
    """
    short_id = models.CharField(
        max_length=200, primary_key=True, default="CHUMP"
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    handle = models.CharField(max_length=200)
    regulation_wins = models.IntegerField(default=0)
    regulation_losses = models.IntegerField(default=0)
    elo_rating = models.FloatField(default=0)

    def __str__(self):
        return self.short_id

class Set(models.Model):
    """
    A series of games representing a challenge between two people.
    """
    set_id = models.IntegerField(primary_key=True, default=0)
    game_count = models.IntegerField()
    player1 = models.ForeignKey(Player, related_name='player1')
    player2 = models.ForeignKey(Player, related_name='player2')

    def __str__(self):
        combatants = self.player1.short_id + " vs. " + self.player2.short_id
        games = " "
        for game in self.game_set.all():
            games += game.__str__() + " "
        return combatants + games

    def winner(self):
        """
        Return the player who won this set. (Player who won more games)
        """
        p1_wins = 0
        p2_wins = 0
        for game in self.game_set.all():
            if game.player1_score > game.player2_score:
                p1_wins += 1
            elif game.player1_score < game.player2_score:
                p2_wins += 1
        if p1_wins > p2_wins:
            return self.player1
        elif p2_wins > p1_wins:
            return self.player2
        else:
           raise UndefinedOutcomeError 

    def outcome(self, player):
        """
        Returns a string describing how this set went for the given player.
        Possible returns:
            "win"
            "loss"
            "draw"
        Raise an exception if the player did not participate in the set.
        """
        winner = None
        try:
            winner = self.winner()
        except UndefinedOutcomeError:
            return "draw"

        if player != self.player1 and player != self.player2:
            raise NonParticipantError

        if winner == player:
            return "win"
        else:
            return "loss"


    def opponent(self, player):
        """
        Return the opposing player to a given player.
        Give back our favorite cat if the given player was not in the game...!?

        So lazy!
        """
        if player == self.player1:
            return self.player2
        elif player == self.player2:
            return self.player1
        else:
            raise KeyError

class Game(models.Model):
    '''
    Represents a single game (part of a larger set of
    games)

    For now, just records the final score of the game.
    In the future, we will also have an array showing
    who won each point.
    '''
    player1_score = models.IntegerField()
    player2_score = models.IntegerField()
    parent_set = models.ForeignKey(Set, null=True)

    def __str__(self):
        return (
            "["+str(self.player1_score)+" "+str(self.player2_score)+"]"
        )
