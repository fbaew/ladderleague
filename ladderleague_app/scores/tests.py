"""Test suite for scores package"""

from django.test import TestCase
from scores.models import Game, Player, Contest
from scores.exceptions import NonParticipantError, UndefinedOutcomeError

class OutcomeTestCase(TestCase):
    """
    Test Contest.outcome(Player), which should return "win", "loss", or 
    "draw" for a given player.
    """
    def test_player_is_winner(self):
        """If the given player won the contest, return "win" """
        goodguy = Player.objects.create(
            short_id="GOODGUY",
            first_name = "Good",
            last_name = "Guy"
        )

        badguy = Player.objects.create(
            short_id="BADGUY",
            first_name = "Bad",
            last_name = "Guy"
        )

        test_contest = Contest.objects.create(
            challenger=goodguy,
            challengee=badguy,
            game_count=2
        )
        game1 = Game.objects.create(
            challenger_score=10,
            challengee_score=21,
            parent_contest=test_contest
        )
        #game1 = Game.objects.create(
        #    challenger_score=21,
        #    challengee_score=15,
        #    parent_contest=self.contest
        #)

       # game2 = Game.objects.create(
       #     challenger_score=21,
       #     challengee_score=15,
       #     parent_contest=self.contest
       #)
       # self.assertTrue(self.contest.outcome(self.goodguy) == "win")
        pass

    def test_player_is_loser(self):
        """If the given player lost the contest, return "loss" """
        self.assertTrue(False)

    def test_player_not_in_contest(self):
        """If the player is not in the contest, throw an exception."""
        with self.assertRaises(NonParticipantError):
            pass

    def test_contest_was_a_draw(self):
        """If there was no winner, return "draw" """
        self.assertTrue(False)
