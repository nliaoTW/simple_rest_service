from django.test import TestCase
from rest_framework.test import APIClient

class HelloViewIntegrationTests(TestCase):

    def test_get(self):
        self.client = APIClient();
        self.uri = '/api/hello-view/'
        resp = self.client.get(self.uri)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['message'], 'Hello!')
        self.assertEqual(resp.data['an_apiview'], [
            'Users HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ])

    def test_post(self):
        self.client = APIClient();
        self.uri = '/api/hello-view/'
        post_data = {'name': 'test'}

        resp = self.client.post(self.uri, post_data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['message'], 'Hello test')

    def test_put(self):
        self.client = APIClient();
        self.uri = '/api/hello-view/'
        resp = self.client.put(self.uri)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['method'], 'PUT')

    def test_patch(self):
        self.client = APIClient();
        self.uri = '/api/hello-view/'
        resp = self.client.patch(self.uri)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['method'], 'PATCH')

    def test_delete(self):
        self.client = APIClient();
        self.uri = '/api/hello-view/'
        resp = self.client.delete(self.uri)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['method'], 'DELETE')
