import unittest
from charpy.chartjs.chart import *


class TestChart(unittest.TestCase):
    def setUp(self):
        self.chart = Chart('bar')

    def test_wrong_chart_type(self):
        self.assertRaises(TypeError, Chart, 'not a chart type')

    def test_title_can_be_setted(self):
        self.chart.title = "test"
        self.assertEqual(self.chart.title, "test")

    def test_wrong_None_title(self):
        with self.assertRaises(ValueError):
            self.chart.title = None

    def test_wrong_empty_title(self):
        with self.assertRaises(ValueError):
            self.chart.title = ''

    def test_toggle_legend(self):
        self.assertFalse(self.chart.legend_display)
        self.chart.toggle_legend()
        self.assertTrue(self.chart.legend_display)


class TestDataset(unittest.TestCase):
    def setUp(self):
        self.d = Dataset([1, 2, 3], 'nombres')

    def test_dataset_well_created(self):
        self.assertEqual(self.d.data, [1, 2, 3])
        self.assertEqual(self.d.label, 'nombres')
        self.assertEqual(self.d.borderColor, "white")
        self.assertEqual(self.d.backgroundColor, "royalBlue")

    def test_wrong_type_label(self):
        self.assertRaises(TypeError, self.d.set_label, 1)

    def test_wrong_type_numeric_data(self):
        self.assertRaises(TypeError, self.d.set_data, 1)

    def test_wrong_type_string_data(self):
        self.assertRaises(TypeError, self.d.set_data, 'abc')

    def test_wrong_type_tuple_or_dict_data(self):
        tupo = (1, 2)
        self.assertRaises(TypeError, self.d.set_data, tupo)

    def test_wrong_type_dict_data(self):
        dico = {'x': 1, 'y': 2}
        self.assertRaises(TypeError, self.d.set_data, dico)

if __name__ == "__main__":
    unittest.main()