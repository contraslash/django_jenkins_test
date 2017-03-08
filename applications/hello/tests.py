from django.test import TestCase, Client
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

from hello_jenkins import conf
# Create your tests here.


class HelloTests(TestCase):

    def test_hello_return_hello(self):

        client = Client()
        response = client.get(reverse(conf.HELLO_URL_NAME))

        self.assertEqual(render_to_string("hello.html"), response.content)
        # This test is going to fail
        # self.assertEqual(1, 2)