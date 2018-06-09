from paste.fixture import TestApp
from nose.tools import *
import unittest
from main import app


class TestWeb(unittest.TestCase):

    def test_test(self):
        r = app.request('/test', method='GET')
        # return_data = r.data
        self.assertEqual('200 OK', r.status)
        # self.assertEqual(b'The server is running now !', return_data)


if __name__ == '__main__':
    unittest.main()
