from django.db import models

# Create your models here.

class Portico(models.Model):
    id_portico = models.IntegerField(primary_key=True)
    ubicacion = models.TextField()

    def _str_(self):
        return str(self.id_portico)


class Bicicleta(models.Model):
    
    id_bicicleta = models.IntegerField(primary_key=True)
    id_portico = models.ForeignKey(Portico,null=False , on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    candado = models.BooleanField(default=False)

    def _str_(self):
        return str(self.id_bicicleta)