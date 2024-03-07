import unittest
from unittest.mock import patch
from Controllers.MatchController import MatchController
from Models.Match import Match


class TestMatchController(unittest.TestCase):

    def test_create_match_pairs(self):
        players = ["J1", "J2", "J3", "J4"]
        expected_pairs = [("J1", "J2"), ("J3", "J4")]
        actual_pairs = MatchController().create_match_pairs(players)

        self.assertEqual(expected_pairs, actual_pairs)

    def test_create_matches(self):
        pairs = [("J1", "J2"), ("J3", "J4")]
        expected_matches = [Match("J1", "J2"), Match("J3", "J4")]

        actual_matches = MatchController().create_matches(pairs)

        self.assertEqual(len(expected_matches), len(actual_matches))  # Check same length
        for expected_match, actual_match in zip(expected_matches, actual_matches):
            self.assertEqual(expected_match.player1, actual_match.player1)
            self.assertEqual(expected_match.player2, actual_match.player2)

    def test_pair_player(self):
        sorted_players = [
            {"first_name": "J1", "last_name": "oui", "score": 10},
            {"first_name": "J2", "last_name": "oui", "score": 7},
            {'first_name': 'J5', 'last_name': 'oui', 'score': 5},
            {"first_name": "J3", "last_name": "oui", "score": 4},
            {"first_name": "J4", "last_name": "oui", "score": 0},
        ]
        played_matches = []
        expected_pairs = [
            ({'first_name': 'J1', 'last_name': 'oui', 'score': 10},
             {'first_name': 'J2', 'last_name': 'oui', 'score': 7}),
            ({'first_name': 'J5', 'last_name': 'oui', 'score': 5},
             {'first_name': 'J3', 'last_name': 'oui', 'score': 4}),
        ]
        actual_pairs = MatchController().pair_players(sorted_players, played_matches)

        self.assertEqual(expected_pairs, actual_pairs)

    @patch('Controllers.MatchController.MatchController.has_played_together', return_value=True)
    def test_pair_players_all_opponents_met(self, mock_has_played_together):
        sorted_players = [
            {"first_name": "J1", "last_name": "oui", "score": 10},
            {"first_name": "J2", "last_name": "oui", "score": 7},
            {"first_name": "J3", "last_name": "oui", "score": 4},
            {"first_name": "J4", "last_name": "oui", "score": 0}
        ]
        played_matches = []
        expected_pairs = [
            ({'first_name': 'J1', 'last_name': 'oui', 'score': 10},
             {'first_name': 'J2', 'last_name': 'oui', 'score': 7}),
            ({'first_name': 'J3', 'last_name': 'oui', 'score': 4},
             {'first_name': 'J4', 'last_name': 'oui', 'score': 0})
        ]

        actual_pairs = MatchController().pair_players(sorted_players, played_matches)

        self.assertEqual(expected_pairs, actual_pairs)

    def test_has_played_together(self):
        match_controller = MatchController()
        played_matches = [
            [('J1 oui', 'J3'), ('J2 oui', 'J4')],
        ]
        player1 = {'first_name': 'J1', 'last_name': 'oui'}
        player2 = {'first_name': 'J2', 'last_name': 'oui'}
        self.assertTrue(match_controller.has_played_together(player1, player2, played_matches))


if __name__ == '__main__':
    unittest.main()
