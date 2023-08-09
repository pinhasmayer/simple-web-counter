import unittest
import requests

class CounterServiceSystemTestCase(unittest.TestCase):
    BASE_URL = "http://ec2-ip-address" # Replace with the actual URL of the deployed service

    def test_get_counter(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"counter": 6})

    def test_increment_counter(self):
        response = requests.post(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Counter incremented successfully"})

        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"counter": 1})

    def test_unsupported_put_request(self):
        response = requests.put(self.BASE_URL)
        self.assertEqual(response.status_code, 405) # 405 Method Not Allowed

if __name__ == '__main__':
    unittest.main()
