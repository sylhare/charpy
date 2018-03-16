import unittest
import charpy.data_import.io_import as io
from tests import DEMO_DATA


class TestIOImport(unittest.TestCase):

    def test_get_demo_data(self):
        """ Make sure we get the demo data from a csv file and transposed """
        self.assertEquals(DEMO_DATA, io.get_demo_data())


if __name__ == "__main__":
    unittest.main()
