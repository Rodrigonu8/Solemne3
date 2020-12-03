from django.test import TestCase
from django.test import Client

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """La página raíz se carga correctamente"""
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)