print("Hello Jenkins")

# Doctest
def hello(str):
    """
    >>> hello("world")
    'Hello world'
    >>> hello("fail")
    'This is a Fail'
    """

    return "Hello %s" % (str)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

# unittest
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(hello('world'), 'Hello world')
 
#     def test_fail(self):
#         self.assertEqual(hello('world'), 'This is a fail')

# if __name__ == '__main__':
#    unittest.main()
