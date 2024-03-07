import unittest
from unittest.mock import patch
from Views.ReportView import ReportView


class TestReportView(unittest.TestCase):

    def setUp(self):
        self.report_view = ReportView()

    @patch('builtins.print')
    def test_display_players_alphabetical(self, mock_print):
        players = [{'first_name': 'Johny', 'last_name': 'Jons',
                    'national_chess_id': 'ABC123'},
                   {'first_name': 'Alice', 'last_name': 'Johnson',
                    'national_chess_id': 'DEF456'}]

        self.report_view.display_players_alphabetical(players)

        mock_print.assert_called_with(
            'Johnson Alice (INE: DEF456)'
        )

    @patch('builtins.print')
    def test_display_tournaments(self, mock_print):
        tournaments = [{'name': 'Tournament1'},
                       {'name': 'Tournament2'}
                       ]

        self.report_view.display_tournaments(tournaments)

        mock_print.assert_called_with(
            'Tournament2'
        )
