from django.db import models

# Create your models here.

class Player(models.Model):
    short_id = models.CharField(max_length=200, primary_key=True,default="CHUMP")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    handle = models.CharField(max_length=200)

class Set(models.Model):
    '''
    A series of games representing a challenge between two people.
    '''
    set_count = models.IntegerField() 
    player1 = models.ForeignKey(Player, related_name='player1')
    player2 = models.ForeignKey(Player, related_name='player2')

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
    parent_set = models.ForeignKey(Set,null=True)

   
