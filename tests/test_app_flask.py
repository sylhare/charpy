"""
Flask TDD:
https://github.com/mjhea0/flaskr-tdd

"""
import unittest
import pytest
from charpy.app import app


class FlaskTest(unittest.TestCase):

    def test_index(self):
        """ inital test. ensure flask was set up correctly """
        tester = app.test_client(self)
        app.testing = True
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #@pytest.mark.skip(reason="no way of currently testing this")
    def test_chart_with_data(self):
        """ inital test. ensure flask was set up correctly """
        tester = app.test_client(self)
        response = tester.get('/chart', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_custom_route(self):
        """ inital test. ensure flask was set up correctly """
        tester = app.test_client(self)
        response = tester.get('/hello/world/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_404_not_found(self):
        """ inital test. ensure flask was set up correctly """
        tester = app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
