import unittest
from charpy.chartjs.color import *


class TestColor(unittest.TestCase):
    def setUp(self):
        self.d = [-1, -2, 0, 1, 5]

    def test_is_positive_return_function(self):
        self.assertEqual(str(type(is_positive())), "<class 'function'>")

    def test_is_postive_true_positive(self):
        self.assertTrue(is_positive()(1))

    def test_is_postive_false_on_negative(self):
        self.assertFalse(is_positive()(-1))

    def test_is_postive_on_zero(self):
        self.assertTrue(is_positive()(0))

    def test_wrong_is_postive_letter(self):
        self.assertRaises(TypeError, is_positive(), "letter")

    def test_is_equal_return_function(self):
        self.assertEqual(str(type(is_equal(0))), "<class 'function'>")

    def test_wrong_is_equal_empty(self):
        self.assertRaises(TypeError, is_equal, (), 1)

    def test_is_equal_number(self):
        self.assertTrue(is_equal(1)(1))

    def test_is_not_equal_number(self):
        self.assertFalse(is_equal(1)(2))

    def test_is_equal_letter(self):
        self.assertTrue(is_equal("letter")("letter"))

    def test_is_not_equal_letter(self):
        self.assertFalse(is_equal("other")("letter"))

    def test_angle_to_hex_color(self):
        self.assertEqual(sin_to_hex(0, 0, 5), '80')
        self.assertEqual(sin_to_hex(0, 2 * math.pi / 3, 5), 'ed')
        self.assertEqual(sin_to_hex(0, 4 * math.pi / 3, 5), '12')

    def test_color_rainbow(self):
        rainbow_5 = ['#8012ed', '#f82165', '#cab301', '#35fe4c', '#079ade']
        self.assertEqual(color_rainbow(self.d), rainbow_5)

    def test_color_rainbow_empty(self):
        self.assertEqual(color_rainbow([]), [])

    def test_color_based_on_sign(self):
        output = ['red', 'red', 'green', 'green', 'green']
        self.assertEqual(color_based_on_sign(self.d), output)

    def test_color_based_on_value(self):
        output = ['lightgray', 'lightgray', 'lightgray', 'blue', 'lightgray']
        self.assertEqual(color_based_on_value(self.d, matching_value=1), output)


if __name__ == "__main__":
    unittest.main()
