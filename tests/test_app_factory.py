import unittest
from charpy.flask.factory import create_app


class TestAppFactory(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_200_index(self):
        """inital test. ensure flask was set up correctly"""
        response = self.client.get('/chart/demo', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_201_custom_route(self):
        """ Check that custom route works with the parameter """
        response = self.client.get('/hello/world/', content_type='html/text')
        self.assertTrue(b'hello world!' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_202_error_404_not_found(self):
        """ Check that the 404 is correctly rendered """
        response = self.client.get('/404', content_type='html/text')
        self.assertTrue(b'WAS NOT FOUND' in response.data)
        self.assertEqual(response.status_code, 404)

    def test_300_chart_with_data(self):
        """ Check that static demo is displayed with value """
        response = self.client.get('/chart/static', content_type='html/text')
        self.assertTrue(b'#F7464A' in response.data)
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
