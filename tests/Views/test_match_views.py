import unittest
from unittest.mock import patch
from Views.MatchView import MatchView


class TestMatchView(unittest.TestCase):

    def setUp(self):
        self.match_view = MatchView()

    @patch('builtins.input', side_effect=['invalid', '4', '2'])
    def test_get_user_choice_invalid_then_valid(self, mock_input):
        result = self.match_view.get_user_choice()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['abc', '1'])
    def test_get_user_choice_non_numeric_then_valid(self, mock_input):
        result = self.match_view.get_user_choice()
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=['5', '2'])
    def test_get_user_choice_out_of_range_then_valid(self, mock_input):
        result = self.match_view.get_user_choice()
        self.assertEqual(result, 2)

    @patch('builtins.input', return_value='3')
    def test_get_user_choice_valid(self, mock_input):
        result = self.match_view.get_user_choice()
        self.assertEqual(result, 3)
