import os
import unittest
from charpy import DATA_PATH, cruncher
from tests import *


class TestConverter(unittest.TestCase):

    def test_is_csv_delimiter_agnostic(self):
        """ The csv file can be opened however the delimiter """
        preset = cruncher.Orc(os.path.join(DATA_PATH, "demo.csv"), sep=',').df.columns.tolist()
        comma = cruncher.Orc(os.path.join(DATA_PATH, "demo.csv")).df.columns.tolist()
        semicolon = cruncher.Orc(os.path.join(DATA_PATH, "demo-semicolon.csv")).df.columns.tolist()
        self.assertEqual(semicolon, comma)
        self.assertEqual(preset, comma)

    def test_is_date_formatted(self):
        file = cruncher.Orc(os.path.join(DATA_PATH, "demo.csv"), sep=',', header=0)
        file.format_date(0)
        semicolon = cruncher.Orc(os.path.join(DATA_PATH, "demo-semicolon.csv"), header=0)
        semicolon.format_date('Month')
        self.assertEqual(file.df['Month'].all(), semicolon.df[semicolon.df.columns[0]].all())
        self.assertEqual(file.df['Month'].tolist(), TEST_MONTH_FORMATTED)


if __name__ == "__main__":
    unittest.main()
