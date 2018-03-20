import unittest
import os
from charpy.data_import.converter import *
from tests import DEMO_DATA, DEMO_DATA_TRANSPOSED


class TestConverter(unittest.TestCase):

    def test_csv_transpose(self):
        """ Make sure that transpose can transpose the csv and put it back how it was """
        self.assertEquals(DEMO_DATA_TRANSPOSED, csv_transpose(DEMO_DATA))
        self.assertEquals(DEMO_DATA, csv_transpose(DEMO_DATA_TRANSPOSED))

    def test_readme_md_to_rst_not_empty(self):
        """ check that readme to rst generate a file not empty """
        self.assertTrue(readme_md_to_rst(), True)

    def test_readme_md_converted_to_rst(self):
        """ If it is really converted the first character should not be a # """
        self.assertFalse(readme_md_to_rst()[1:] == "#")


if __name__ == "__main__":
    unittest.main()
