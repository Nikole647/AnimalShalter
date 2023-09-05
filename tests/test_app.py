
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



