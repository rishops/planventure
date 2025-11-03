import unittest
import json
from app import create_app, db
from models import User

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register(self):
        response = self.client.post('/auth/register', data=json.dumps({
            'email': 'test@example.com',
            'password': 'password'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.post('/auth/register', data=json.dumps({
            'email': 'test@example.com',
            'password': 'password'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        self.client.post('/auth/register', data=json.dumps({
            'email': 'test@example.com',
            'password': 'password'
        }), content_type='application/json')

        response = self.client.post('/auth/login', data=json.dumps({
            'email': 'test@example.com',
            'password': 'password'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.get_json())

        response = self.client.post('/auth/login', data=json.dumps({
            'email': 'test@example.com',
            'password': 'wrong_password'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 401)