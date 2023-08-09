import unittest
import requests

class CounterServiceSystemTestCase(unittest.TestCase):
    BASE_URL = "http://ec2-18-194-132-45.eu-central-1.compute.amazonaws.com:80" # Replace with the actual URL of the deployed service

    def test_get_counter(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)

    def test_increment_counter(self):
        initial_response = requests.get(self.BASE_URL)
        initial_counter = initial_response.json()["counter"]
        for i in range(5):
            post_response = requests.post(self.BASE_URL)
            self.assertEqual(post_response.status_code, 200)
            self.assertEqual(post_response.json()["message"], "Counter incremented successfully")

            # Get the updated value of the counter
            get_response = requests.get(self.BASE_URL)
            self.assertEqual(get_response.status_code, 200)
            self.assertEqual(get_response.json()['counter'], initial_counter + i + 1)

    def test_unsupported_put_request(self):
        response = requests.put(self.BASE_URL)
        self.assertEqual(response.status_code, 405) # 405 Method Not Allowed

if __name__ == '__main__':
    unittest.main()
