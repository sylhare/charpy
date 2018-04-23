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
        response = self.client.get('/chart_demo/hello/world/', content_type='html/text')
        self.assertTrue(b'hello world!' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_202_error_404_not_found(self):
        """ Check that the 404 is correctly rendered """
        response = self.client.get('/404', content_type='html/text')
        self.assertTrue(b'WAS NOT FOUND' in response.data)
        self.assertEqual(response.status_code, 404)

    def test_203_error_501_not_implemented(self):
        """ Check that the 404 is correctly rendered """
        response = self.client.get('/chart/populationgraph/', content_type='html/text')
        self.assertTrue(b'NOT IMPLEMENTED' in response.data)
        self.assertEqual(response.status_code, 501)

    def test_300_chart_with_static_data(self):
        """ Check that static demo is displayed with value """
        response = self.client.get('/chart_demo/static/', content_type='html/text')
        self.assertTrue(b'#F7464A' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_301_chart_with_input_data(self):
        """inital test. ensure flask was set up correctly"""
        response = self.client.get('/chart_demo/default/', content_type='html/text')
        self.assertTrue(b'pie' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_302_chart_with_chart_object(self):
        """ Check that static demo is displayed with value """
        response = self.client.get('/chart_demo/charpy/', content_type='html/text')
        self.assertTrue(b'bar' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_311_chart_api_with_type_bar(self):
        chart_type = chartjs.BAR
        response = self.client.get('/chart/' + chart_type + '/', content_type='html/text')
        self.assertTrue(chart_type in response.data)
        self.assertEqual(response.status_code, 200)

    def test_312_chart_api_with_type_pie(self):
        chart_type = chartjs.PIE
        response = self.client.get('/chart/' + chart_type + '/', content_type='html/text')
        self.assertTrue(chart_type in response.data)
        self.assertEqual(response.status_code, 200)

    def test_313_chart_api_with_type_radar(self):
        chart_type = chartjs.RADAR
        response = self.client.get('/chart/' + chart_type + '/', content_type='html/text')
        self.assertTrue(chart_type in response.data)
        self.assertEqual(response.status_code, 200)

    def test_314_chart_api_with_type_bubble(self):
        chart_type = chartjs.BUBBLE
        response = self.client.get('/chart/' + chart_type + '/', content_type='html/text')
        self.assertTrue(chart_type in response.data)
        self.assertEqual(response.status_code, 200)

    def test_315_chart_api_with_type_scatter(self):
        chart_type = chartjs.SCATTER
        response = self.client.get('/chart/' + chart_type + '/', content_type='html/text')
        self.assertTrue(chart_type in response.data)
        self.assertEqual(response.status_code, 200)

    def test_316_chart_api_with_type_polar(self):
        chart_type = chartjs.POLAR_AREA
        response = self.client.get('/chart/' + chart_type + '/', content_type='html/text')
        self.assertTrue(chart_type in response.data)
        self.assertEqual(response.status_code, 200)

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
        response = self.client.get('/dataframe/date/')
        self.assertEqual(response.status_code, 200)

    def test_403_is_data_json(self):
        """ Check that data collected is in json format """
        response = self.client.get('/dataframe/label/')
        self.assertEqual(response.mimetype, 'application/json')


if __name__ == "__main__":
    unittest.main()
