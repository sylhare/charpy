import unittest
import os
import csv
from tests import *
from charpy.data_import.CSVfile import CSVfile


class CSVfileDataTest(object):

    def setUp(self):
        """ Open the test file """
        with open("testfile.csv", 'w') as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL)
            wr.writerows(self.FILE_DATA)
        self.file = open("testfile.csv", 'rU')

    def test_file_created(self):
        """ Make sure the test file is created and initialised well """
        self.assertTrue(list(csv.reader(self.file)) == self.FILE_DATA)

    def test_extract_csv_data(self):
        """  """
        csv_file = CSVfile(self.file)
        self.assertTrue(csv_file.get_values(CSVfile.ROW) == TEST_DATA_ROW)
        self.assertTrue(csv_file.get_values(CSVfile.COLUMN) == TEST_DATA_COLUMN)

    def tearDown(self):
        """ Close the file and remove it """
        self.file.close()
        os.remove("testfile.csv")


class CSVFileTestHeader(CSVfileDataTest, unittest.TestCase):
    FILE_DATA = TEST_DATA

    def test_get_header(self):
        """ Make sur the header is populated """
        csv_file = CSVfile(self.file)
        self.assertTrue(csv_file.data_header == TEST_DATA[0])


class CSVFileTestNoHeader(CSVfileDataTest, unittest.TestCase):
    FILE_DATA = TEST_DATA_ROW

    def test_no_header_found(self):
        """ Make sur the header is populated """
        csv_file = CSVfile(self.file)
        self.assertFalse(csv_file.has_header)


if __name__ == "__main__":
    unittest.main()
