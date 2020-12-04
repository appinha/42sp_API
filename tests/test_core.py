import unittest
import requests
import json
from api.app import app

class TestDefault(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()
		self.response = self.app.get('/')

	def test_content_type(self):
		self.assertIn('text/html', self.response.content_type)
