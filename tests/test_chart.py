import unittest
from charpy.chartjs.chart import *


class TestChart(unittest.TestCase):
    def setUp(self):
        self.chart = Chart('bar')

    def test_500x_wrong_chart_type(self):
        self.assertRaises(TypeError, Chart, 'not a chart type')

    def test_501_title_not_setted_return_None(self):
        self.assertEqual(self.chart.title, None)

    def test_502_title_can_be_setted(self):
        self.chart.title = "test"
        self.assertEqual(self.chart.title, "test")
        self.assertTrue(self.chart._title_display)

    def test_503_title_is_a_chart_attribute(self):
        self.assertTrue(hasattr(self.chart, 'title'))

    def test_504x_wrong_None_title(self):
        with self.assertRaises(ValueError):
            self.chart.title = None

    def test_505x_wrong_empty_title(self):
        with self.assertRaises(ValueError):
            self.chart.title = ''

    def test_510_toggle_legend(self):
        self.assertEqual(self.chart._legend_display, JS_CONVERT[False])
        self.chart.toggle_legend_display()
        self.assertEqual(self.chart._legend_display, JS_CONVERT[True])

    def test_511x_chart_with_wrong_legend_display_value(self):
        self.assertRaises(ValueError, Chart, 'bar', legend_display="random_stuff")

    def test_520_add_a_simple_dataset(self):
        self.chart.add_simple_dataset(data_label='numbers', data=[1, 2, 3])
        self.chart.datasets


class TestDataset(unittest.TestCase):
    def setUp(self):
        self.d = Dataset([1, 2, 3], 'numbers')

    def test_600_tojson_dataset(self):
        d_json = '{"backgroundColor": "royalBlue", "borderColor": "white", "data": [1, 2, 3], "label": "numbers"}'
        self.assertEqual(self.d.to_json(), d_json)

    def test_601_dataset_well_created(self):
        self.assertEqual(self.d.data, [1, 2, 3])
        self.assertEqual(self.d.label, 'numbers')
        self.assertEqual(self.d.borderColor, "white")
        self.assertEqual(self.d.backgroundColor, "royalBlue")

    def test_610_set_label(self):
        label = "the label"
        self.d.set_label(label)
        self.assertEqual(self.d.label, label)

    def test_611x_wrong_type_label(self):
        self.assertRaises(TypeError, self.d.set_label, 1)

    def test_620_set_data(self):
        data = [4, 5, 6]
        self.d.set_data(data)
        self.assertEqual(self.d.data, data)

    def test_621x_wrong_type_numeric_data(self):
        self.assertRaises(TypeError, self.d.set_data, 1)

    def test_622x_wrong_type_string_data(self):
        self.assertRaises(TypeError, self.d.set_data, 'abc')

    def test_623x_wrong_type_tuple_or_dict_data(self):
        tupo = (1, 2)
        self.assertRaises(TypeError, self.d.set_data, tupo)

    def test_624x_wrong_type_dict_data(self):
        dico = {'x': 1, 'y': 2}
        self.assertRaises(TypeError, self.d.set_data, dico)


if __name__ == "__main__":
    unittest.main()
