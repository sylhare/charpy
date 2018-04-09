import os
import unittest
from charpy import DATA_PATH
from charpy.cruncher import Orc, check_path
from tests import *


class TestConverter(unittest.TestCase):

    def setUp(self):
        self.file = Orc(os.path.join(DATA_PATH, "demo.csv"), sep=',', header=0)
        self.semicolon = Orc(os.path.join(DATA_PATH, "demo-semicolon.csv"), header=0)

    def test_000_is_csv_delimiter_agnostic(self):
        """ The csv file can be opened however the delimiter """
        preset = self.file.df.columns.tolist()
        comma = Orc(os.path.join(DATA_PATH, "demo.csv"), header=0).df.columns.tolist()
        semicolon = self.semicolon.df.columns.tolist()
        self.assertEqual(semicolon, comma)
        self.assertEqual(preset, comma)

    def test_001_is_default_header(self):
        """ When no header parameters, the default one is taken """
        comma = Orc(os.path.join(DATA_PATH, "demo.csv")).df
        self.assertFalse(comma.columns.values.all() == self.file.df.columns.values.all())
        self.assertTrue(list(comma) == Orc.DEFAULT_NAMES)

    def test_002_open_from_directory(self):
        """ Path can be a directory """
        self.file = Orc(os.path.join(DATA_PATH))
        self.assertTrue(self.file.df.shape[0] == 33)

    def test_x10_wrong_column(self):
        """ Raise an error is a wrong column identifier is put """
        print('\n\nWrong column input raise exception')
        self.assertRaises(TypeError, self.file.format_column_date(-1))
        self.assertRaises(TypeError, self.file.format_column_date('test'))

    def test_x11_is_wrong_path_typeError(self):
        """ Wrong path type give typeError """
        print('\n\nWrong path input raise exception')
        self.assertRaises(TypeError, check_path(2))

    def test_020_is_date_formatted_default(self):
        """ The date should be formatted in month """
        self.file.format_column_date(0)
        self.semicolon.format_column_date('Month')
        self.assertEqual(self.file.df['Month'].all(), self.semicolon.df[self.semicolon.df.columns[0]].all())

    def test_021_is_date_formatted_month(self):
        """ Change data format to default then back to Month and make sure it is still ok """
        self.file.format_column_date(0)
        self.file.format_column_date(0, formatting='%B')
        self.assertEqual(self.file.df['Month'].tolist(), TEST_DATA_COLUMN[0])

    def test_030_is_list_formatted(self):
        """ test column if formatted to list """
        self.file.format_column_list(2, regex=r'#')
        self.assertTrue(type(self.file.df['Colors'][0]) == list)
        self.assertTrue(len(self.file.df['Colors'][0]) == 2)

    def test_031_are_new_column_created(self):
        """ Make sure columns are created """
        self.file.format_column_list(2, regex=r'#')
        self.assertTrue(len(self.file.df.columns) == 3)
        self.file.create_columns_from_list_column(2, names=['hashtag', 'hexa'])
        self.assertTrue(len(self.file.df.columns) == 5)

    def test_032_are_more_column_created(self):
        """ Make sure the right amount of column is created eventhough there's not enough data """
        self.file.format_column_list(2, regex=r'#')
        self.file.create_columns_from_list_column(2, names=['hashtag', 'hexa', 'stuff'])
        self.assertTrue(len(self.file.df.columns) == 6)

    def test_x33_wrong_not_list_column(self):
        """ Raise an error when the column has no list object for creation """
        print('\n\nWrong not list column raise exception')
        self.assertRaises(TypeError, self.file.create_columns_from_list_column(2, names=['hashtag', 'hexa']))


if __name__ == "__main__":
    unittest.main()
