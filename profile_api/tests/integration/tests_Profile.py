from django.test import TestCase
from rest_framework.test import APIClient

class ProfileIntegrationTest(TestCase):

    def test_get(self):
        self.client = APIClient();
        self.uri = '/api/profile/'

        resp = self.client.get(self.uri)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, [])

    def test_post(self):
        post_data = { 'email': 'test_user@test.com', 'name': 'test_user', 'password': 'test_password' }
        self.client = APIClient();
        self.uri = '/api/profile/'

        resp = self.client.post(self.uri, post_data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data['id'], 1)
        self.assertEqual(resp.data['email'], 'test_user@test.com')
        self.assertEqual(resp.data['name'], 'test_user')