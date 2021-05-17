from django.test import TestCase, RequestFactory
from profile_api.views.HelloApiView import HelloApiView

class HelloAPiView(TestCase):

    def test_get(self):
        status_code = 200
        view_class = HelloApiView

        # req = RequestFactory().get('/')
        # resp = view_class.get()(req, *[], **{})
        # self.assertEqual(resp.status_code, 200)

