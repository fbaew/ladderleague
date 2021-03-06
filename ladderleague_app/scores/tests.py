"""Test suite for scores package"""

from django.test import TestCase
from scores.models import Game, Player, Contest
from scores.exceptions import NonParticipantError, UndefinedOutcomeError
from scores.management.commands import load_users
import django.conf
import csv, os

class ContestWinnerTestCase(TestCase):
    """
    Test Contest.winner(), which should return the player who won more
    individual games.
    """
    def setUp(self):
        """
        Create some generic data to test against.
        """
        self.goodguy = Player.objects.create(
            short_id="GOODGUY",
            first_name="Good",
            last_name="Guy"
        )
        self.badguy = Player.objects.create(
            short_id="BADGUY",
            first_name="Bad",
            last_name="Guy"
        )

        self.contest = Contest.objects.create(
            challenger=self.goodguy,
            challengee=self.badguy
        )

    def test_obvious_winner(self):
        """
        If one person has a higher score in both of the only 2 games played as
        part of a contest, Contest.winner() should return that player.
        """
        game1 = Game.objects.create(
            challenger_score=21,
            challengee_score=15,
            parent_contest=self.contest
        )

        game2 = Game.objects.create(
            challenger_score=21,
            challengee_score=15,
            parent_contest=self.contest
        )

        self.assertTrue(self.contest.winner() == self.goodguy)

    def test_contested_winner(self):
        """
        If one player has won 2/3 of the games, Contest.winner() should return
        that player.
        :return:
        """
        game1 = Game.objects.create(
            challenger_score=21,
            challengee_score=15,
            parent_contest=self.contest
        )

        game2 = Game.objects.create(
            challenger_score=3,
            challengee_score=21,
            parent_contest=self.contest
        )

        game3 = Game.objects.create(
            challenger_score=21,
            challengee_score=19,
            parent_contest=self.contest
        )

        self.assertTrue(self.contest.winner() == self.goodguy)


class ContestOutcomeTestCase(TestCase):
    """
    Test Contest.outcome(Player), which should return "win", "loss", or 
    "draw" for a given player.
    """
    def setUp(self):
        """Create some generic data to test against."""
        self.goodguy = Player.objects.create(
            short_id="GOODGUY",
            first_name="Good",
            last_name="Guy"
        )

        self.badguy = Player.objects.create(
            short_id="BADGUY",
            first_name="Bad",
            last_name="Guy"
        )

        self.contest = Contest.objects.create(
            challenger=self.goodguy,
            challengee=self.badguy,
        )

    def test_player_is_winner(self):
        """
        If the given player won the contest, return "win"
        If the given player lost, return "loss"
        """

        game1 = Game.objects.create(
            challenger_score=21,
            challengee_score=15,
            parent_contest=self.contest
        )

        game2 = Game.objects.create(
            challenger_score=21,
            challengee_score=15,
            parent_contest=self.contest
        )
        self.assertTrue(self.contest.outcome(self.goodguy) == "win")
        self.assertTrue(self.contest.outcome(self.badguy) == "loss")

    def test_player_not_in_contest(self):
        """If the player is not in the contest, throw an exception."""
        third_party = Player.objects.create(
            short_id="INTRUDER",
            first_name="Random",
            last_name="Person"
        )
        with self.assertRaises(NonParticipantError):
            self.contest.outcome(third_party)

    def test_contest_was_a_draw(self):
        """If there was no winner, return "draw" """
        game1 = Game.objects.create(
            challenger_score=21,
            challengee_score=15,
            parent_contest=self.contest
        )

        game2 = Game.objects.create(
            challenger_score=11,
            challengee_score=21,
            parent_contest=self.contest
        )
        self.assertTrue(self.contest.outcome(self.goodguy) == "draw")
        self.assertTrue(self.contest.outcome(self.badguy) == "draw")


class OpponentTestCase(TestCase):
    """
    Test the Contest.opponent(Player) function
    """
    def test_contest_opponent(self):
        """
        Given a Contest and a Player, we should return a Player representing
        the given Player's opponent in the given Contest.
        """
        player1 = Player.objects.create(
            short_id="PLAYER1",
            first_name="Player",
            last_name="One"
        )
        player2 = Player.objects.create(
            short_id="PLAYER2",
            first_name="Player",
            last_name="Two"
        )
        contest = Contest.objects.create(
            challenger=player1,
            challengee=player2,
        )
        self.assertTrue(contest.opponent(player1) == player2)
        self.assertTrue(contest.opponent(player2) == player1)

    def test_contest_opponent_nonparticipant(self):
        """
        If the given player was not in this contest, raise an exception.
        """
        player1 = Player.objects.create(
            short_id="PLAYER1",
            first_name="Player",
            last_name="One"
        )
        player2 = Player.objects.create(
            short_id="PLAYER2",
            first_name="Player",
            last_name="Two"
        )
        player3 = Player.objects.create(
            short_id="PLAYER3",
            first_name="Player",
            last_name="Three"
        )
        contest = Contest.objects.create(
            challenger=player1,
            challengee=player2,
        )
        with self.assertRaises(NonParticipantError):
            contest.opponent(player3)

class CSVImportTestCase(TestCase):
    """
    Test the assorted utilities for populating the db
    """
    def update_user_helper(self, filename):
        util = load_users.Command()
        input_csv = os.path.join(
            django.conf.settings.DATA_DIR,
            "testdata",
            filename
        )

        try:
            with open(input_csv, 'r') as csvfile:
                reader = csv.reader(csvfile,delimiter=',')
                for row in reader:
                   util._update_user(row)

        except FileNotFoundError:
            print("Couldn't open {}; test failed.".format(input_csv))

    def test_create_user(self):
        self.assertTrue(len(Player.objects.all()) == 0)
        self.update_user_helper("single_player.csv")
        test_player = Player.objects.get(short_id="TESTUSER")
        self.assertTrue(len(Player.objects.all()) == 1)
        self.assertTrue(test_player.first_name == "Christopher")
        self.assertTrue(test_player.last_name == "Lloyd")
        self.assertTrue(test_player.handle == "Professor Plum")
        self.assertTrue(test_player.origin == "Stamford, Connecticut")

    def test_overwrite_user(self):
        """
        Tests the case where a user appears more than once in the CSV.
        Expected behaviour is that the existing user should be updated.

        n.b. this shouldn't have
        :return:
        """
        self.update_user_helper("duplicate_player.csv")
        test_player = Player.objects.get(short_id="TESTUSER")
        self.assertTrue(test_player.first_name == "Christopher")
        self.assertTrue(test_player.last_name == "Lloyd")
        self.assertTrue(test_player.handle == "Doc")
        self.assertTrue(test_player.origin == "Stamford, Connecticut")

    def test_malformed_user_file_missing_field(self):
        with self.assertRaises(IndexError):
            self.update_user_helper("malformed_file-missing_field.csv")
