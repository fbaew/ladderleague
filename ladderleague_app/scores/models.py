from django.db import models

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
    hometown = models.CharField(
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
    game_count = models.IntegerField(null=False)

    def __str__(self):
        """Describe the matchup."""
        return "{} vs {}".format(self.challenger, self.challengee)
        #return "This is a contest"

class Game(models.Model):
    """Represent a single game (part of a larger Contest)"""
    challenger_score = models.IntegerField()
    challengee_score = models.IntegerField()
    parent_contest = models.ForeignKey(Contest, null=False)

    def __str__(self):
        """Describe the game"""
        return "{}/{}".format(self.challenger_score, self.challengee_score)
