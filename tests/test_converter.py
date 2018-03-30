import unittest
import datetime
from charpy.data_import.converter import *
from tests import TEST_DATA_COLUMN, TEST_DATA_ROW


class TestConverter(unittest.TestCase):

    def test_csv_transpose(self):
        """ Make sure that transpose can transpose the csv and put it back how it was """
        self.assertEqual(TEST_DATA_ROW, transpose(TEST_DATA_COLUMN))
        self.assertEqual(TEST_DATA_COLUMN, transpose(TEST_DATA_ROW))

    def test_readme_md_to_rst_not_empty(self):
        """ check that readme to rst generate a file not empty """
        self.assertTrue(readme_md_to_rst(), True)

    def test_readme_md_converted_to_rst(self):
        """ If it is really converted the first character should not be a # """
        self.assertFalse(readme_md_to_rst()[1:] == "#")

    def test_string_to_date(self):
        """ If it is really converted the first character should not be a # """
        self.assertTrue(string_to_date("18/04/2018") == datetime.date(2018, 4, 18))

    def test_string_to_float(self):
        """ If it is really converted the first character should not be a # """
        self.assertTrue(string_to_float("1234.5678") == 1234.5678)


if __name__ == "__main__":
    unittest.main()
