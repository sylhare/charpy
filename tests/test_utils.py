import unittest
from charpy.utils import *


class TestConverter(unittest.TestCase):

    def test_readme_md_to_rst_not_empty(self):
        """ check that readme to rst generate a file not empty """
        self.assertTrue(readme_md_to_rst(), True)

    def test_readme_md_converted_to_rst(self):
        """ If it is really converted the first character should not be a # """
        self.assertFalse(readme_md_to_rst()[1:] == "#")

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
