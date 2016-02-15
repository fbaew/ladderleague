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

    def __str__(self):
        return self.short_id

class Contest(models.Model):
    """Represet a series of games; a single contest between two players."""
    contest_id = models.IntegerField(primary_key=True)
    challenger = models.ForeignKey(Player)
    challengee = models.ForeignKey(Player)

    def __str__(self):
        """Describe the matchup."""
        return "{} vs {}".format(challenger, chalengee)

class Game(models.Model):
    """Represent a single game (part of a larger Contest)"""
    challenger_score = models.integerField()
    chalengee_score = models.integerField()
    parent_contest = modelsForeignKey(Set, null=False)

    def __str__(self):
        """Describe the game"""
        return "{}/{}".format(self.challenger_score, self.challengee_score)
