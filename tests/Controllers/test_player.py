import unittest
from unittest import mock
from Controllers.PlayerController import PlayerController
import io


class PlayerControllerTests(unittest.TestCase):
    def setUp(self):
        self.controller = PlayerController()

    @mock.patch('builtins.input', side_effect=['John', 'Doe', '01/01/1990', 'ABC12345', ''])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_add_player(self, mock_input, mock_stdout):
        self.controller.add_player()
        self.assertIn('Joueur ajouté à la base de donnée avec succès !', mock_stdout.getvalue())
