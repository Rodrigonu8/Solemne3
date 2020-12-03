from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy



class RegistroUsuario(CreateView):
    model = User 
    template_name = "Usuario/registrar.html"
    form_class = RegistroForm 
    success_url = reverse_lazy('home') 
 
 
class UserList(ListView):
    model = User
    template_name = 'Usuario/listar_usuario.html'
    
