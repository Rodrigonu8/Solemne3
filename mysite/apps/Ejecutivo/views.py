from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Ejecutivo
from .forms import EjecutivoForm
# Create your views here.

class EjecutivoList (ListView):                    
    model = Ejecutivo
    template_name = 'Ejecutivo/ejecutivo_list.html'

class EjecutivoCreate (CreateView):
    model = Ejecutivo
    form_class = EjecutivoForm
    template_name = 'Ejecutivo/ejecutivo_form.html'
    success_url = reverse_lazy('ejecutivo_list')

class EjecutivoUpdate(UpdateView):
    model = Ejecutivo
    form_class = EjecutivoForm
    template_name = 'Ejecutivo/ejecutivo_form.html'
    success_url = reverse_lazy('ejecutivo_list')

class EjecutivoDelete(DeleteView):
    model = Ejecutivo
    template_name = 'Ejecutivo/ejecutivo_borrar.html'
    success_url = reverse_lazy('ejecutivo_list')