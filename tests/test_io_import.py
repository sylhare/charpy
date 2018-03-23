import unittest
from charpy.data_import.io_import import *
from tests import DEMO_DATA


class TestIOImport(unittest.TestCase):

    def test_get_demo_data(self):
        """ Make sure we get the demo data from a csv file and transposed """
        self.assertEqual(DEMO_DATA, get_demo_data())

    def test_get_readme_rst(self):
        """ check if you can retrieve the rst file and that a file is not created """
        result = get_readme_rst()
        self.assertFalse(result == "")

    def test_reate_readme_rst(self):
        """ check that readme to rst generate a file not empty """
        os.remove(README_RST_PATH)
        create_readme_rst()
        self.assertTrue(os.path.isfile(README_RST_PATH))
        self.assertTrue(os.path.getsize(README_RST_PATH) > 0)


if __name__ == "__main__":
    unittest.main()
