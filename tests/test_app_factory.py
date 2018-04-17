import unittest
from charpy.flask.factory import create_app


class TestAppFactory(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_index(self):
        """inital test. ensure flask was set up correctly"""
        response = self.client.get('/chart/demo', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_chart_with_data(self):
        """ Check that static demo is displayed with value """
        response = self.client.get('/chart/static', content_type='html/text')
        self.assertTrue(b'#F7464A' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_dataframe_rendered(self):
        """ Check that custom route works with the parameter """
        response = self.client.get('/v1/dataframe', content_type='html/text')
        self.assertTrue(b'<table border="1" class="dataframe">' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_data_from_dataframe(self):
        """ Check that data is reachable """
        response = self.client.get('/v1/dataframe/date/')
        self.assertEqual(response.status_code, 200)

    def test_is_data_json(self):
        """ Check that data collected is in json format """
        response = self.client.get('/v1/dataframe/label/')
        self.assertEqual(response.mimetype, 'application/json')

    def test_custom_route(self):
        """ Check that custom route works with the parameter """
        response = self.client.get('/hello/world/', content_type='html/text')
        self.assertTrue(b'hello world!' in response.data)
        self.assertEqual(response.status_code, 200)

    def test_404_not_found(self):
        """ Check that the 404 is correctly rendered """
        response = self.client.get('/404', content_type='html/text')
        self.assertTrue(b'WAS NOT FOUND' in response.data)
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
