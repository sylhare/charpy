import unittest
from tests import TEST_DATASET, TEST_SIMPLE_DATASET
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
        self.assertTrue(isinstance(Chart.title, property))

    def test_504x_wrong_None_title(self):
        with self.assertRaises(ValueError):
            self.chart.title = None

    def test_505x_wrong_empty_title(self):
        with self.assertRaises(ValueError):
            self.chart.title = ''

    def test_506_labels_not_setted_return_empty_list(self):
        self.assertEqual(self.chart.labels, [])

    def test_507_labels_can_be_setted(self):
        self.chart.labels = ["a", "b", "c"]
        self.assertEqual(self.chart.labels, ["a", "b", "c"])

    def test_508_labels_is_a_chart_attribute(self):
        self.assertTrue(hasattr(self.chart, 'labels'))
        self.assertTrue(isinstance(Chart.labels, property))

    def test_509x_wrong_not_list_labels(self):
        with self.assertRaises(TypeError):
            self.chart.labels = "Not a list"

    def test_510_toggle_legend(self):
        self.assertEqual(self.chart._legend_display, JS_CONVERT[False])
        self.chart.toggle_legend_display()
        self.assertEqual(self.chart._legend_display, JS_CONVERT[True])

    def test_511x_chart_with_wrong_legend_display_value(self):
        self.assertRaises(ValueError, Chart, 'bar', legend_display="random_stuff")

    def test_520_add_a_simple_dataset(self):
        self.chart.add_simple_dataset(data_label='numbers', data=[1, 2, 3])
        self.assertEqual(self.chart.datasets, TEST_SIMPLE_DATASET)

    def test_521_add_two_simple_dataset(self):
        self.chart.add_simple_dataset(data_label='numbers', data=[1, 2, 3])
        self.chart.add_simple_dataset(data_label='numbers', data=[1, 2, 3])
        self.assertEqual(self.chart.datasets, TEST_SIMPLE_DATASET*2)

    def test_522_add_dataset(self):
        self.d = Dataset([1, 2, 3], 'numbers')
        self.chart.add_dataset(self.d)
        self.assertEqual(self.chart.datasets, TEST_DATASET)

    def test_523_add_two_datasets(self):
        self.d = Dataset([1, 2, 3], 'numbers')
        self.chart.add_dataset(self.d)
        self.chart.add_dataset(self.d)
        self.assertEqual(self.chart.datasets, TEST_DATASET*2)

    def test_524_add_dataset_and_simple_dataset(self):
        self.d = Dataset([1, 2, 3], 'numbers')
        self.chart.add_simple_dataset(data_label='numbers', data=[1, 2, 3])
        self.chart.add_dataset(self.d)
        self.assertEqual(self.chart.datasets, TEST_SIMPLE_DATASET+TEST_DATASET)

    def test_530_render_chart_html(self):
        output_html = self.chart.render_chart()
        self.assertTrue("<canvas" in output_html)
        self.assertTrue("new Chart(document.getElementById" in output_html)

    def test_531_render_chart_html_chart_type(self):
        output_html = self.chart.render_chart()
        self.assertTrue("type: 'bar'" in output_html)

    def test_532_render_chart_html_labels(self):
        output_html = self.chart.render_chart()
        self.assertTrue("labels: []" in output_html)

    def test_533_render_chart_html_chart_type(self):
        output_html = self.chart.render_chart()
        self.assertTrue("datasets: [  ]" in output_html)

    def test_534_render_chart_html_options(self):
        output_html = self.chart.render_chart()
        self.assertTrue("legend: { display: false }," in output_html)
        self.assertTrue("display: false," in output_html)
        self.assertTrue("text: 'None'" in output_html)

    def test_535_render_chart_html_default_id(self):
        output_html = self.chart.render_chart()
        self.assertTrue("Chart(document.getElementById('chart')" in output_html)

    def test_536_render_chart_html_different_type(self):
        output_html = self.chart.render_chart('pie')
        self.assertTrue("type: 'pie'" in output_html)

    def test_537x_render_chart_html_not_chart_type(self):
        output_html = self.chart.render_chart('blob')
        self.assertTrue("type: 'bar'" in output_html)

    def test_540_render_chart_title_changed(self):
        self.chart.title = "test"
        output_html = self.chart.render_chart()
        self.assertTrue("display: true," in output_html)
        self.assertTrue("text: 'test'" in output_html)

    def test_541_render_chart_legend_toggled(self):
        self.chart.toggle_legend_display()
        output_html = self.chart.render_chart()
        self.assertTrue("legend: { display: true }," in output_html)

    def test_542_render_chart_labels_changed(self):
        self.chart.labels = ["a", "b", "c"]
        output_html = self.chart.render_chart()
        self.assertTrue("labels: ['a', 'b', 'c']" in output_html)

    def test_543_render_chart_datasets_changed(self):
        self.chart.add_simple_dataset(data_label='numbers', data=[1, 2, 3])
        output_html = self.chart.render_chart()
        self.assertTrue('datasets: [ ' + TEST_SIMPLE_DATASET + ' ]' in output_html)

    def test_544_render_chart_id_changed(self):
        self.chart.canvas_id = "new_id"
        output_html = self.chart.render_chart()
        self.assertTrue("document.getElementById('new_id')" in output_html)

    def test_545_render_chart_type_changed(self):
        self.chart.chart_type = 'pie'
        output_html = self.chart.render_chart()
        self.assertTrue("type: 'pie'," in output_html)

    def test_546_render_chart_with_simple_dataset(self):
        self.chart.add_simple_dataset(data_label='numbers', data=[1, 2, 3])
        output_html = self.chart.render_chart()
        self.assertTrue('datasets: [ ' + TEST_SIMPLE_DATASET + ' ]' in output_html)

    def test_547_render_chart_with_dataset(self):
        self.d = Dataset([1, 2, 3], 'numbers')
        self.chart.add_dataset(self.d)
        self.chart.add_simple_dataset(data_label='numbers', data=[1, 2, 3])
        output_html = self.chart.render_chart()
        self.assertTrue(TEST_DATASET+TEST_SIMPLE_DATASET in output_html)

    def test_550_render_full_html(self):
        output_html = self.chart.render_html()
        self.assertTrue("<!DOCTYPE html>" in output_html)
        self.assertTrue("<script src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js" in output_html)
        self.assertTrue("<canvas id='chart'" in output_html)
        self.assertTrue("new Chart(document.getElementById" in output_html)

    def test_551_render_full_html_two_charts(self):
        charts = self.chart.render_chart() + self.chart.render_chart('pie')
        output_html = Chart.render_raw(content=charts)
        self.assertTrue("type: 'pie'," in output_html)
        self.assertTrue("<canvas id='id_pie'" in output_html)
        self.assertTrue("type: 'bar'," in output_html)
        self.assertTrue("<canvas id='chart'" in output_html)


class TestDataset(unittest.TestCase):
    def setUp(self):
        self.d = Dataset([1, 2, 3], 'numbers')

    def test_600_tojson_dataset(self):
        self.assertEqual(self.d.to_json(), TEST_DATASET[:-1])

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
