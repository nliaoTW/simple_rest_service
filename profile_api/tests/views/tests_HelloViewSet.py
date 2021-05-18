from django.test import TestCase
from rest_framework.test import APIRequestFactory
from profile_api.views.HelloViewSet import HelloViewSet

class HelloApiViewUnitTests(TestCase):

    def test_list(self):
        req = APIRequestFactory().get('/')
        resp = HelloViewSet.list(self, req)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['message'], 'Hello!')
        self.assertEqual(resp.data['a_viewset'], [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ])

    # def test_create(self):
    #     req = APIRequestFactory().post('/')
    #     resp = HelloViewSet.create(self, req)
    #
    #     self.assertEqual(resp.status_code, 200)

    def test_retrieve(self):
        req = APIRequestFactory().get('/')
        resp = HelloViewSet.retrieve(self, req)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, {'http_method': 'GET'})

    def test_update(self):
        req = APIRequestFactory().put('/')
        resp = HelloViewSet.update(self, req)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, {'http_method': 'PUT'})

    def test_partial_update(self):
        req = APIRequestFactory().patch('/')
        resp = HelloViewSet.partial_update(self, req)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, {'http_method': 'PATCH'})

    def test_destroy(self):
        req = APIRequestFactory().delete('/')
        resp = HelloViewSet.destroy(self, req)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, {'http_method': 'DELETE'})