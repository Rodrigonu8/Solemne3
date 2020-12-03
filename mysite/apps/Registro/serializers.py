from rest_framework import serializers
from .models import Portico, Bicicleta
 
class PorticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portico
        fields = '__all__'

class BicicletaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Bicicleta
        fields = ('id_bicicleta','id_portico', 'modelo', 'candado')