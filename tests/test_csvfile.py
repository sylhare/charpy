import unittest
import os
import csv
from tests import *
from charpy.data_import.CSVfile import CSVfile


class FlaskTest(unittest.TestCase):
    def setUp(self):
        """ Create a test file with test data and leave it open """
        with open("testfile.csv", 'w') as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL)
            wr.writerows(TEST_DATA)
        self.file = open("testfile.csv", 'rU')

    def test_file_created(self):
        """ Make sure the test file is created and initialised well """
        self.assertTrue(list(csv.reader(self.file)) == TEST_DATA)

    def test_extract_csv_data(self):
        """  """
        csv_file = CSVfile(self.file)
        self.assertTrue(csv_file.data_rows == TEST_DATA_ROW)
        self.assertTrue(csv_file.data_columns == TEST_DATA_COLUMN)

    def tearDown(self):
        """ Close the file and remove it """
        self.file.close()
        os.remove("testfile.csv")


if __name__ == "__main__":
    unittest.main()
