import unittest
import os

print("Current working directory:", os.getcwd())
print("Content of '../app':", os.listdir('../app'))

import sys
sys.path.append('../app')
from app import app

class CounterServiceTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_get_request(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Counter:', response.data)

    def test_post_request(self):
        response = self.client.post('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'counter incremented', response.data)

    def test_counter_increment(self):
        for i in range(5):
            response = self.client.post('/')
            self.assertIn(f'Counter: {i + 1}'.encode(), response.data)

if __name__ == '__main__':
    unittest.main()

