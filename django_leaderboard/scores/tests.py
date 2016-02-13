"""
Test suite for scores package
"""
from django.test import TestCase
from scores.models import Set, Game, Player
from scores.exceptions import NonParticipantError, UndefinedOutcomeError

# Create your tests here.


class SetOutcomeTestCase(TestCase):
    """
    Tests for the outcome() method, which should return "win",
    "loss", or "draw" given a specific player.
    """
    def setUp(self):
        """
        Configure test preconditions
        """
        self.gregg = Player.objects.create(
            short_id="GREGG"
            , first_name="Gregg"
            , last_name="Lewis"
        )

        self.opponent = Player.objects.create(
            short_id="ENEMY"
            , first_name="John"
            , last_name="Dixon"
        )
        self.test_set = Set.objects.create(
            player1=self.gregg,
            player2=self.opponent,
            game_count=2
        )

        game1 = Game.objects.create(
            player1_score=21,
            player2_score=15,
            parent_set=self.test_set,
        )
        game2 = Game.objects.create(
            player1_score=21,
            player2_score=3,
            parent_set=self.test_set
        )


    def test_player_is_winner(self):
        """
        If the given player won the set, return "draw"
        """
        self.assertTrue(self.test_set.outcome(self.gregg) == "win")
        
    def test_player_is_loser(self):
        """
        If the given player lost the set, return "loss"
        """
        self.assertTrue(self.test_set.outcome(self.opponent) == "loss")

    def test_no_contest(self):
        """
        If the given player was not in this set, throw an exception.
        """
        intruder = Player.objects.create(
            short_id="INTRUDER",
            first_name="Not",
            last_name="ARealPlayer"
        )
        with self.assertRaises(NonParticipantError):
            self.test_set.outcome(intruder)

class SetOutcomeErrorTestCase(TestCase):
    """
    Test cases where a tied Set is required.
    """
    def setUp(self):
        """
        Configure test preconditions
        """
        self.gregg = Player.objects.create(
            short_id="GREGG"
            , first_name="Gregg"
            , last_name="Lewis"
        )

        self.opponent = Player.objects.create(
            short_id="ENEMY"
            , first_name="John"
            , last_name="Dixon"
        )
        self.test_set = Set.objects.create(
            player1=self.gregg,
            player2=self.opponent,
            game_count=2
        )

    def test_no_winner(self):
        """
        If there was no winner, return "draw"
        """

        game1 = Game.objects.create(
            player1_score=21,
            player2_score=15,
            parent_set=self.test_set,
        )
        game2 = Game.objects.create(
            player1_score=15,
            player2_score=21,
            parent_set=self.test_set
        )

        self.assertTrue(self.test_set.outcome(self.opponent) == "draw")
        self.assertTrue(self.test_set.outcome(self.gregg) == "draw")
#
        pass



class SetWinnerTestCase(TestCase):
    """
    Test that Set objects correctly calculate the winner
    """

    def setUp(self):
        """
        Configure some test players
        """
        self.gregg = Player.objects.create(
            short_id="GREGG"
            , first_name="Gregg"
            , last_name="Lewis"
        )

        self.opponent = Player.objects.create(
            short_id="ENEMY"
            , first_name="John"
            , last_name="Dixon"
        )

    def test_outright_win(self):
        """
        See that Set.winner() returns the expected winner when
        the set is made up of 2 games
        """
        test_set = Set.objects.create(
            player1=self.gregg,
            player2=self.opponent,
            game_count=2
        )
        game1 = Game.objects.create(
            player1_score=21,
            player2_score=15,
            parent_set=test_set,
        )
        game2 = Game.objects.create(
            player1_score=21,
            player2_score=3,
            parent_set=test_set
        )
        self.assertTrue(test_set.winner() == self.gregg)

    def test_contested_win(self):
        """
        We should also return the right winner when the set includes a victory
        by the loser.
        """
        test_set = Set.objects.create(
            player1=self.gregg,
            player2=self.opponent,
            game_count=3
        )
        game1 = Game.objects.create(
            player1_score=21,
            player2_score=15,
            parent_set=test_set,
        )
        game2 = Game.objects.create(
            player1_score=21,
            player2_score=23,
            parent_set=test_set
        )
        game3 = Game.objects.create(
            player1_score=21,
            player2_score=3,
            parent_set=test_set
        )
        self.assertTrue(test_set.winner() == self.gregg)

    def test_draw(self):
        """
        We need some kind of safety here... either you shouldn't be able to
        call winner() on a set that was a draw, or we should raise an
        exception. We definitely SHOULDN'T fabricate a fake player with some
        kind of meta-significance... Yet, we are testing for exactly that.
        """
        test_set = Set.objects.create(
            player1=self.gregg,
            player2=self.opponent,
            game_count=2
        )
        game1 = Game.objects.create(
            player1_score=21,
            player2_score=15,
            parent_set=test_set,
        )
        game2 = Game.objects.create(
            player1_score=21,
            player2_score=23,
            parent_set=test_set
        )

        with self.assertRaises(UndefinedOutcomeError):
            test_set.winner()

class BulkJobTestCase(TestCase):
    """
    Tests to make sure we create objects like we think we will
    """
