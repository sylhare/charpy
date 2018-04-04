import os
import unittest
from charpy import DATA_PATH
from charpy.cruncher import Orc
from tests import *


class TestConverter(unittest.TestCase):

    def setUp(self):
        self.file = Orc(os.path.join(DATA_PATH, "demo.csv"), sep=',', header=0)
        self.semicolon = Orc(os.path.join(DATA_PATH, "demo-semicolon.csv"), header=0)

    def test_is_csv_delimiter_agnostic(self):
        """ The csv file can be opened however the delimiter """
        preset = self.file.df.columns.tolist()
        comma = Orc(os.path.join(DATA_PATH, "demo.csv"), header=0).df.columns.tolist()
        semicolon = self.semicolon.df.columns.tolist()
        self.assertEqual(semicolon, comma)
        self.assertEqual(preset, comma)

    def test_is_date_formatted_default(self):
        """ The date should be formatted in month """
        self.file.format_column_date(0)
        self.semicolon.format_column_date('Month')
        self.assertEqual(self.file.df['Month'].all(), self.semicolon.df[self.semicolon.df.columns[0]].all())

    def test_is_date_formatted_month(self):
        """ Change data format to default then back to Month and make sure it is still ok """
        self.file.format_column_date(0)
        self.file.format_column_date(0, formatting='%B')
        self.assertEqual(self.file.df['Month'].tolist(), TEST_DATA_COLUMN[0])

    def test_is_list_formatted(self):
        """ test column if formatted to list """
        self.file.format_column_list(2, regex=r'#')
        self.assertTrue(type(self.file.df['Colors'][0]) == list)
        self.assertTrue(len(self.file.df['Colors'][0]) == 2)


if __name__ == "__main__":
    unittest.main()
