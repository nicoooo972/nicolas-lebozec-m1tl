import unittest
from Controllers.MenuController import MenuController
from unittest.mock import patch


class MenuTest(unittest.TestCase):
    def setUp(self):
        self.controller = MenuController()

    @patch('builtins.input', side_effect=['1', 'John', 'Doe', '0'])
    def test_user_choice_add_player(self, mock_input):
        with self.assertRaises(SystemExit):
            self.controller.user_choice()
