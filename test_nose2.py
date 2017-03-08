import unittest

from hello import hello

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(hello('world'), 'Hello world')
