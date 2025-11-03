import unittest
import json
import os
from app import create_app
from flask_cors import CORS

class ApiFinalizationTestCase(unittest.TestCase):

    def setUp(self):
        # Set environment variable for CORS testing
        os.environ['CORS_ALLOWED_ORIGINS'] = 'http://allowed-origin.com'
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        # Clean up environment variable after tests
        del os.environ['CORS_ALLOWED_ORIGINS']

    def test_cors_allowed_origin(self):
        headers = {'Origin': 'http://allowed-origin.com'}
        response = self.client.get('/', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Access-Control-Allow-Origin', response.headers)
        self.assertEqual(response.headers['Access-Control-Allow-Origin'], 'http://allowed-origin.com')

    def test_cors_unauthorized_origin(self):
        headers = {'Origin': 'http://unauthorized-origin.com'}
        response = self.client.get('/', headers=headers)
        self.assertNotIn('Access-Control-Allow-Origin', response.headers)

    def test_health_endpoint_operational(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'operational'})

    def test_health_endpoint_degraded(self):
        # This test will require mocking the dependency check within the /health endpoint
        # For now, it will pass if the endpoint exists and returns a default operational status
        # Actual degraded state testing will be implemented once the dependency check logic is in place
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'operational'})
