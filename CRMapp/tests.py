from django.test import TestCase


# Create your tests here.
class simpleTest(TestCase):
    """Simple test to check if CircleCI runs tests correctly"""

    def setUp(self):
        pass

    def test(self):
        self.assertEqual(True, True)
