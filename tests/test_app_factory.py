import unittest
from charpy.flask.factory import create_app
from charpy import chartjs


class TestAppFactory(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_200_index(self):
        """inital test. ensure flask was set up correctly"""
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_201_custom_route(self):
        """ Check that custom route works with the parameter """
        response = self.client.get('/demo/hello/world/', content_type='html/text')
        self.assertTrue(b'hello world!' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_202_error_404_not_found(self):
        """ Check that the 404 is correctly rendered """
        response = self.client.get('/404', content_type='html/text')
        self.assertTrue(b'WAS NOT FOUND' in response.data)
        self.assertEqual(response.status_code, 404)

    def test_203_chart_with_static_data(self):
        """ Check that static demo is displayed with value """
        response = self.client.get('/demo/static/', content_type='html/text')
        self.assertTrue(b'#F7464A' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_204_chart_with_input_data(self):
        """inital test. ensure flask was set up correctly"""
        response = self.client.get('/demo/default/', content_type='html/text')
        self.assertTrue(b'pie' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_205_chart_with_chart_simple_dataset(self):
        """ Check that static demo is displayed with value """
        response = self.client.get('/demo/simple_dataset/', content_type='html/text')
        self.assertTrue(b'bar' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_206_chart_with_two_charts(self):
        """ Check that static demo is displayed with value """
        response = self.client.get('/demo/two/', content_type='html/text')
        self.assertTrue(b'bar' in response.data)
        self.assertTrue(b'pie' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_207_chart_with_dataset(self):
        """ Check that static demo is displayed with value """
        response = self.client.get('/demo/dataset/', content_type='html/text')
        self.assertTrue(b'bar' in response.data)
        self.assertTrue(b'"backgroundColor":' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_310_chart_return_types(self):
        """ Check that static demo is displayed with value """
        response = self.client.get('/chart/types/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')

    def case_chart_api_with_type(self, chart_type):
        """ Case for the chart rendered of the good type with the api """
        response = self.client.get('/chart/draw/' + chart_type + '/', content_type='html/text')
        self.assertTrue(chart_type in str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_311_chart_api_with_type_bar(self):
        self.case_chart_api_with_type(chartjs.BAR)

    def test_312_chart_api_with_type_pie(self):
        self.case_chart_api_with_type(chartjs.PIE)

    def test_313_chart_api_with_type_radar(self):
        self.case_chart_api_with_type(chartjs.RADAR)

    def test_314_chart_api_with_type_bubble(self):
        self.case_chart_api_with_type(chartjs.BUBBLE)

    def test_315_chart_api_with_type_scatter(self):
        self.case_chart_api_with_type(chartjs.SCATTER)

    def test_316_chart_api_with_type_polar(self):
        self.case_chart_api_with_type(chartjs.POLAR_AREA)

    def test_317x_error_501_not_implemented(self):
        """ Check that the 404 is correctly rendered """
        response = self.client.get('/chart/draw/populationgraph/', content_type='html/text')
        self.assertTrue(b'NOT IMPLEMENTED' in response.data)
        self.assertEqual(response.status_code, 501)

    def test_400_dataframe_rendered(self):
        """ Check that custom route works with the parameter """
        response = self.client.get('/dataframe/html/', content_type='html/text')
        self.assertTrue(b'<table border="1" class="dataframe">' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_401_get_data_from_dataframe(self):
        """ Check that custom route works with the parameter """
        response = self.client.get('/dataframe/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_402_get_data_from_dataframe_column(self):
        """ Check that data is reachable """
        response = self.client.get('/dataframe/column/date/')
        self.assertEqual(response.status_code, 200)

    def test_403_is_data_json(self):
        """ Check that data collected is in json format """
        response = self.client.get('/dataframe/column/label/')
        self.assertEqual(response.mimetype, 'application/json')

    def test_404_wrong_column_raise_404(self):
        response = self.client.get('/dataframe/column/not a column name/')
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
