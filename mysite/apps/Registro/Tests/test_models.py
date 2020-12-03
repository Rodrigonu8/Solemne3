from django.test import TestCase
from django.template.defaultfilters import slugify
from apps.Registro.models import Portico

class PorticoTestCase(TestCase):
    def setUp(self):
        Portico.objects.create(id_portico=1101,ubicacion="AAAA")
        Portico.objects.create(id_portico=1102,ubicacion="BBBB")

    def test_ingresar_portico(self):
        """Los porticos se han registrado correctamente en la BD"""
        portico_1 = Portico.objects.get(id_portico=1101)
        portico_2 = Portico.objects.get(id_portico=1102)
        self.assertEqual(portico_1.ubicacion, "AAAA")
        self.assertEqual(portico_2.ubicacion, "BBBB")
