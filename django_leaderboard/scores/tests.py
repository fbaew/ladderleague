from django.test import TestCase
from scores.models import Set, Game, Player

# Create your tests here.



class SetTestCase(TestCase):
    """
    Test that Set objects correctly calculate the winner
    """
    
    def setUp(self):
        """
        Configure some test players
        """
        Player.objects.create(
            short_id="GREGG"
            , first_name="Gregg"
            , last_name="Lewis"
        )

        Player.objects.create(
            short_id="ENEMY"
            , first_name="John"
            , last_name="Dixon"
        )

    def test_two_game_outright_two_game_win(self):
        gregg = Player.objects.get(short_id="GREGG")
        opponent = Player.objects.get(short_id="ENEMY")

        test_set = Set.objects.create(
            player1=gregg,
            player2=opponent,
            game_count = 2
        )
        game1 = Game.objects.create(
            player1_score = 21,
            player2_score = 15,
            parent_set = test_set,
        )

        game2 = Game.objects.create(
            player1_score = 21,
            player2_score = 3,
            parent_set = test_set
        )

        self.assertTrue(test_set.winner() == self.gregg)
