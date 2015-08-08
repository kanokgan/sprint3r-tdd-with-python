import unittest
from app import app

class TestFizzBuzzAPI(unittest.TestCase):
	def test_root(self):
		self.app = app.test_client()
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)
#		self.assertEqual('Hello world', response.data)
	def test_test_it_should_return_fizz_when_number_is_3(self):
		self.app = app.test_client()
		response = self.app.get('/fizzbuzz/3')
		self.assertEqual(response.status_code, 200)
		self.assertEqual('fizz', response.data)


