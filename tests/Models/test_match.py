import unittest

from Models.Player import Player
from Models.Match import Match


class MatchTests(unittest.TestCase):

    def test_serialize(self):
        player1 = Player("Alice", "Oui", "2000-01-01", "")
        player2 = Player("Alain", "Non", "1990-12-31", "")

        match = Match(player1, player2)

        serialized_match = match.serialize()

        # Assertions
        if serialized_match['winner'] is not None:
            self.assertEqual(serialized_match['winner'], player1)
