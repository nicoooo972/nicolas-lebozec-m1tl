import unittest
from Controllers.TournamentController import TournamentController


class TestTournamentController(unittest.TestCase):

    def setUp(self):
        self.tournament_controller = TournamentController()


if __name__ == '__main__':
    unittest.main()
