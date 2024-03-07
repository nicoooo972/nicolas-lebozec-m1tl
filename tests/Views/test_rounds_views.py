import unittest
from unittest.mock import patch
from Views.RoundsView import RoundsView


class TestRoundsView(unittest.TestCase):

    def setUp(self):
        self.rounds_view = RoundsView()

    @patch('builtins.input', return_value='o')
    def test_ask_for_next_round_yes(self, mock_input):
        result = self.rounds_view.ask_for_next_round()
        self.assertEqual(result, 'o')

    @patch('builtins.input', return_value='n')
    def test_ask_for_next_round_no(self, mock_input):
        result = self.rounds_view.ask_for_next_round()
        self.assertEqual(result, 'n')

    @patch('builtins.input', return_value='invalid')
    def test_ask_for_next_round_invalid_input_then_yes(self, mock_input):
        result = self.rounds_view.ask_for_next_round()
        self.assertEqual(result, 'invalid')
