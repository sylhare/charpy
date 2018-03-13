"""
Flask TDD:
https://github.com/mjhea0/flaskr-tdd

"""
import unittest
from charpy import app


class FlaskTest(unittest.TestCase):

    def test_index(self):
        """inital test. ensure flask was set up correctly"""
        tester = app.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_chart_with_data(self):
        """inital test. ensure flask was set up correctly"""
        tester = app.app.test_client(self)
        response = tester.get('/chart', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_custom_route(self):
        """inital test. ensure flask was set up correctly"""
        tester = app.app.test_client(self)
        response = tester.get('/hello/world/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
