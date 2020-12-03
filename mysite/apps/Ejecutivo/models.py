from django.db import models


class Ejecutivo (models.Model):
    fotografia = models.ImageField(upload_to='ejecutivos')
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(
        max_length=70, blank=True, null=True, unique=True)


def _str_(self):
    return str(self.fotografia)
