import unittest
from charpy.data_import.converter import csv_transpose
from tests import DEMO_DATA, DEMO_DATA_TRANSPOSED


class TestConverter(unittest.TestCase):

    def test_csv_transpose(self):
        """ Make sure that transpose can transpose the csv and put it back how it was """
        self.assertEquals(DEMO_DATA_TRANSPOSED, csv_transpose(DEMO_DATA))
        self.assertEquals(DEMO_DATA, csv_transpose(DEMO_DATA_TRANSPOSED))


if __name__ == "__main__":
    unittest.main()
