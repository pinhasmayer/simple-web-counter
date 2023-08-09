import unittest
from app import app, counter

class CounterServiceTestCase(unittest.TestCase):
    def setUp(self):
        global counter # Declare counter as global
        counter = 0    # Reset the counter before each test
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_get_request(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"counter": 0})

    def test_post_request(self):
        response = self.client.post('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Counter incremented successfully"})

    def test_counter_increment(self):
        for i in range(5):
            response = self.client.post('/')
            self.assertEqual(response.get_json(), {"message": "Counter incremented successfully"})
            get_response = self.client.get('/')
            self.assertEqual(get_response.status_code, 200)
            self.assertEqual(get_response.json(), {"counter": i + 1})
        
    def test_unsupported_put_request(self):
        response = self.client.put('/')
        self.assertEqual(response.status_code, 405) # 405 Method Not Allowed

if __name__ == '__main__':
    unittest.main()

