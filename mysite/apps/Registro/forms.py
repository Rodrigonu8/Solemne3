from django import forms
from .models import Bicicleta, Portico


class porticoForm(forms.ModelForm):
    class Meta:
        model = Portico
        fields = ['id_portico', 'ubicacion']

        labels = {
            'id_portico': 'ID Pórtico',
            'ubicacion': 'Ubicacion',

        }
        widgets = {
            'id_portico': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
           
        }

class bicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = ['id_bicicleta', 'id_portico', 'modelo', 'candado']

        labels = {
            'id_bicicleta': 'ID Bicicleta', 
            'id_portico': 'ID Pórtico', 
            'modelo': 'Modelo', 
            'candado': 'Candado',

        }
        widgets = {
            'id_bicicleta': forms.TextInput(attrs={'class': 'form-control'}),
            'id_portico': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'candado': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
