import os
import unittest
import datetime
from charpy import MOCK_PATH, SQL_PATH, TEST_DATABASE_URI
from charpy.cruncher import Orc, check_path
from tests import *


class TestConverter(unittest.TestCase):

    def setUp(self):
        self.file = Orc(os.path.join(MOCK_PATH, "demo.csv"), sep=',', header=0)
        self.semicolon = Orc(os.path.join(MOCK_PATH, "demo-semicolon.csv"), header=0)

    def test_000_is_csv_delimiter_agnostic_comma(self):
        """ The csv file can be opened however the delimiter """
        preset = self.file.df.columns.tolist()
        comma = Orc(os.path.join(MOCK_PATH, "demo.csv"), header=0).df.columns.tolist()
        self.assertEqual(preset, comma)

    def test_001_is_csv_delimiter_agnostic_semicolon(self):
        """ The csv file can be opened however the delimiter """
        preset = self.file.df.columns.tolist()
        semicolon = self.semicolon.df.columns.tolist()
        self.assertEqual(preset, semicolon)

    def test_002_is_default_header(self):
        """ When no header parameters, the default one is taken """
        comma = Orc(os.path.join(MOCK_PATH, "demo.csv")).df
        self.assertFalse(comma.columns.values.all() == self.file.df.columns.values.all())
        self.assertTrue(list(comma) == Orc.DEFAULT_NAMES)

    def test_003_open_from_directory(self):
        """ Path can be a directory """
        self.file = Orc(os.path.join(MOCK_PATH))
        self.assertTrue(self.file.df.shape[0] == 33)

    def test_004_get_colum_values_as_list(self):
        """ Make sure we get the column values from a csv file """
        self.assertEqual(TEST_DATA_COLUMN, self.file.get_column_values())

    def test_010x_is_wrong_path_empty(self):
        """ Wrong path type give typeError """
        print('\n\nWrong path input raise exception')
        self.assertRaises(TypeError, check_path([]))

    def test_011x_is_wrong_path_numeric(self):
        """ Wrong path type give typeError """
        self.assertRaises(TypeError, check_path(2))

    def test_120_is_date_formatted_default(self):
        """ The date should be formatted in month """
        self.file.format_column_date(0)
        self.semicolon.format_column_date('Month')
        self.assertEqual(self.file.df['Month'].all(), self.semicolon.df[self.semicolon.df.columns[0]].all())

    def test_121_is_date_formatted_month(self):
        """ Change data format to default then back to Month and make sure it is still ok """
        self.file.format_column_date(0)
        self.file.format_column_date(0, formatting='%B')
        self.assertEqual(self.file.df['Month'].tolist(), TEST_DATA_COLUMN[0])

    def test_122_is_new_date_column_created_day(self):
        """ Test if the new date column is created using the right format """
        self.file.create_from_date_column(formatting="day", input_date_column=0, output_column_name="date-day")
        self.assertTrue(self.file.df["date-day"].str.contains('day').all())
        self.assertTrue(len(self.file.df.columns) == 4)

    def test_123_is_new_date_column_created_month(self):
        """ Test if the new date column is created using the right format """
        self.file.create_from_date_column(formatting="month", input_date_column=0, output_column_name="date-month")
        self.assertTrue(list(self.file.df["date-month"]), TEST_DATA_COLUMN[0])
        self.assertTrue(len(self.file.df.columns) == 4)

    def test_124_is_new_date_column_created_year(self):
        """ Test if the new date column is created using the right format """
        self.file.create_from_date_column(formatting="year", input_date_column=0, output_column_name="date-year")
        self.assertTrue(self.file.df["date-year"].str.contains(str(datetime.date.today().year)).all())
        self.assertTrue(len(self.file.df.columns) == 4)

    def test_130_is_list_formatted(self):
        """ test column if formatted to list """
        self.file.format_column_list(2, regex=r'#')
        self.assertTrue(len(self.file.df['Colors'][0]) == 2 and type(self.file.df['Colors'][0]) == list)

    def test_131_are_new_column_created(self):
        """ Make sure columns are created """
        self.file.format_column_list(2, regex=r'#')
        self.assertTrue(len(self.file.df.columns) == 3)
        self.file.create_from_list_column(2, names=['hashtag', 'hexa'])
        self.assertTrue(len(self.file.df.columns) == 5)

    def test_132_are_more_column_created(self):
        """ Make sure the right amount of column is created eventhough there's not enough data """
        self.file.format_column_list(2, regex=r'#')
        self.file.create_from_list_column(2, names=['hashtag', 'hexa', 'stuff'])
        self.assertTrue(len(self.file.df.columns) == 6)

    def test_140x_wrong_column_string(self):
        """ Raise an error is a wrong column identifier is put """
        print('\n\nWrong column input raise exception')
        self.assertRaises(ValueError, self.file.format_column_date('test'))

    def test_141x_wrong_column_negative_number(self):
        """ Raise an error is a wrong column identifier is put """
        self.assertRaises(TypeError, self.file.format_column_date(-1))

    def test_142x_wrong_column_number(self):
        """ Raise an error is a wrong column identifier is put """
        self.assertRaises(IndexError, self.file.format_column_date(100))

    def test_143x_wrong_date_format_number(self):
        """ Raise an error is a wrong column identifier is put """
        print('\n\nWrong format input raise exception')
        self.assertRaises(TypeError, self.file.format_column_date(0, formatting=1))

    def test_144x_wrong_date_format_string(self):
        """ Raise an error is a wrong column identifier is put """
        self.assertRaises(ValueError, self.file.format_column_date(0, formatting="not a format"))

    def test_145x_wrong_not_list_column(self):
        """ Raise an error when the column has no list object for creation """
        print('\n\nWrong not list column raise exception')
        self.assertRaises(TypeError, self.file.create_from_list_column(2, names=['hashtag', 'hexa']))

    def test_150_is_database_created(self):
        """ Check if the db is created """
        test_db_path = TEST_DATABASE_URI
        self.file.create_sql_db(db_path=test_db_path)
        self.assertTrue(os.path.exists(test_db_path))


if __name__ == "__main__":
    unittest.main()
