
#import requests

# def test_ping_server():
#     # change the test
#     url = 'http://172.28.1.3:5000/'
#
#     # Send a GET request to the server
#     response = requests.get(url)
#
#     # Check if the response status code is 200 (OK)
#     assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

import pytest
from flask_testing import TestCase
from Server.Server import app

class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index(self):
        response = self.client.get('/')
        self.assert_template_used('index.html')
        self.assert200(response)  # Check if the response is successful (status code 200)

if __name__ == '__main__':
    pytest.main()



