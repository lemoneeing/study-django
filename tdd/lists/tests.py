from django.test import TestCase

# Create your tests here.
class smokeTest(TestCase):
    def test_bad_match(self):
        self.assertEquals(1+1, 1)