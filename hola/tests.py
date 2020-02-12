from django.test import TestCase

# Create your tests here.
class TestSmoke(TestCase):
	"""docstring for TestSmoke"""
	def test_smoke_Test(self):
		self.assertEquals(2+2,4)
		