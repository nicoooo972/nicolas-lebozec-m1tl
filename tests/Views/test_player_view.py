import unittest
from unittest.mock import patch
from Views.PlayerView import PlayerView


class TestPlayerView(unittest.TestCase):

    def setUp(self):
        self.player_view = PlayerView()

    @patch('builtins.input', side_effect=['Jonhny', 'john', '01/01/1990', ''])
    def test_get_player_info_with_valid_input(self, mock_input):
        result = self.player_view.get_player_info()
        self.assertEqual(result, ('Jonhny', 'john', '01/01/1990', ''))

    @patch('builtins.input', side_effect=['0', '5', '2'])
    def test_select_player_with_invalid_then_valid_input(self, mock_input):
        players = [
            {'first_name': 'Alice', 'last_name': 'Johnson',
             'birth_date': '01/01/1985', 'national_chess_id': 'ABC123'},
            {'first_name': 'Bob', 'last_name': 'Smith',
             'birth_date': '02/02/1990', 'national_chess_id': 'DEF456'}]
        result = self.player_view.select_player(players)
        self.assertEqual(result, 0)

    @patch('builtins.input', side_effect=['3', '1'])
    def test_select_player_with_out_of_range_then_valid_input(self, mock_input):
        players = [
            {'first_name': 'Alice', 'last_name': 'Johnson',
             'birth_date': '01/01/1985', 'national_chess_id': 'ABC123'},
            {'first_name': 'John', 'last_name': 'Smith',
             'birth_date': '02/02/1990', 'national_chess_id': 'DEF456'}]
        result = self.player_view.select_player(players)
        self.assertEqual(result, 1)
