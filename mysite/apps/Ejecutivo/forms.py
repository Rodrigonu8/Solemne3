from .models import Ejecutivo
from django import forms

class EjecutivoForm(forms.ModelForm):
    class Meta:
        model = Ejecutivo
        fields = (
            'fotografia',
            'rut',
            'nombre',
            'email'
        )
        labels = {
            'fotografia':'Fotografia',
            'rut':'RUN',
            'nombre':'Nombre',
            'email':'Correo electronico'
        }
        widgets = {
            # 'fotografia':forms.FileInput(attrs={'class':'form-control','type':'file'}),
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }