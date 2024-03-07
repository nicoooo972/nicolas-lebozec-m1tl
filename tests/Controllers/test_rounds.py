import unittest
from unittest.mock import patch
from Controllers.RoundsController import RoundsController


class TestRoundsController(unittest.TestCase):

    def setUp(self):
        self.rounds_controller = RoundsController()

    @patch('builtins.input', side_effect=['1'])
    def test_sort_players_by_score(self, mock_input):
        players = [{'name': 'Player1', 'score': 3},
                   {'name': 'Player2', 'score': 2},
                   {'name': 'Player3', 'score': 3}
                   ]
        sorted_players = self.rounds_controller.sort_players_by_score(players)
        self.assertEqual(sorted_players, [{'name': 'Player1', 'score': 3}, {'name': 'Player3', 'score': 3},
                                          {'name': 'Player2', 'score': 2}])

    @patch('builtins.input', side_effect=['1'])
    def test_get_match_results(self, mock_input):
        with patch.object(self.rounds_controller.matchView, 'display_match_results', return_value=1):
            matches = [
                {'player1': {'first_name': 'Player1', 'last_name': 'Last1'},
                 'player2': {'first_name': 'Player2', 'last_name': 'Last2'}},
                {'player1': {'first_name': 'Player3', 'last_name': 'Last3'},
                 'player2': {'first_name': 'Player4', 'last_name': 'Last4'}}
            ]
            results = self.rounds_controller.get_match_results(matches, 1)
            self.assertEqual(results, [
                (['Player1 Last1', 1], ['Player2 Last2', 0]),
                (['Player3 Last3', 1], ['Player4 Last4', 0])
            ])


if __name__ == '__main__':
    unittest.main()
