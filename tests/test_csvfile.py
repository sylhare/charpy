import unittest
import os
import csv
from tests import *
from charpy.data_import.CSVfile import CSVfile


def csv_data_testcases(file_data):
    """ """
    class CSVfileDataTestcase(unittest.TestCase):
        def setUp(self):
            """ Open the test file """
            with open("testfile.csv", 'w') as f:
                wr = csv.writer(f, quoting=csv.QUOTE_ALL)
                wr.writerows(file_data)
            self.file = open("testfile.csv", 'rU')

        def test_file_created(self):
            """ Make sure the test file is created and initialised well """
            self.assertTrue(list(csv.reader(self.file)) == file_data)

        def test_extract_csv_data(self):
            """  """
            csv_file = CSVfile(self.file)
            self.assertTrue(csv_file.get_values(CSVfile.ROW) == TEST_DATA_ROW)
            self.assertTrue(csv_file.get_values(CSVfile.COLUMN) == TEST_DATA_COLUMN)

        def tearDown(self):
            """ Close the file and remove it """
            self.file.close()
            os.remove("testfile.csv")

    return CSVfileDataTestcase


class CSVFileTestHeader(csv_data_testcases(TEST_DATA)):
    pass


class CSVFileTestNoHeader(csv_data_testcases(TEST_DATA_ROW)):
    pass


if __name__ == "__main__":
    unittest.main()
