from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Portico, Bicicleta
from .forms import porticoForm, bicicletaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# listar porticos y bicicletas


def listar_porticos(request):
    porticos = Portico.objects.all()
    return render(request, "Registro/listar_porticos.html", {'porticos': porticos})


def listar_bicicletas(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, "Registro/listar_bicicletas.html", {'bicicletas': bicicletas})

 # agregar portico


def agregar_portico(request):
    if request.method == "POST":
        form = porticoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_portico")
    else:
        form = porticoForm()
        return render(request, "Registro/agregar_portico.html", {'form': form})


# borrar portico

def borrar_portico(request, portico_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Portico.objects.get(id=portico_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_portico')

# editar porticco


def editar_portico(request, portico_id):
    # Recuperamos la instancia de la carrera
    instancia = Portico.objects.get(id=portico_id)

    # Creamos el formulario con los datos de la instancia
    form = porticoForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = porticoForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_portico.html", {'form': form})


# clases crear portico

class PorticoCreate(CreateView):
    model = Portico
    form_class = porticoForm
    template_name = 'Registro/agregar_portico.html'
    success_url = reverse_lazy("list_portico")

# clase listar portico


class PorticoList(ListView):
    model = Portico
    template_name = 'Registro/listar_porticos_filtros.html'

# clase modificar portico


class PorticoUpdate(UpdateView):
    model = Portico
    form_class = porticoForm
    template_name = 'Registro/editar_portico.html'
    success_url = reverse_lazy('listar_porticos')

# clase borrar portico


class PorticoDelete(DeleteView):
    model = Portico
    template_name = 'Registro/portico_delete.html'
    success_url = reverse_lazy('listar_porticos')


# agregar bicicleta

def agregar_bicicleta(request):
    if request.method == "POST":
        form = bicicletaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_bicicleta")
    else:
        form = bicicletaForm()
        return render(request, "Registro/agregar_bicicleta.html", {'form': form})


# borrar bicicleta

def borrar_bicicleta(request, bicicleta_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Bicicleta.objects.get(id=bicicleta_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_bicicletas')

# editar bicicleta


def editar_bicicleta(request, bicicleta_id):
    # Recuperamos la instancia de la carrera
    instancia = Bicicleta.objects.get(id=bicicleta_id)

    # Creamos el formulario con los datos de la instancia
    form = bicicletaForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = bicicletaForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_bicicleta.html", {'form': form})


# clases crear bicicleta

class BicicletaCreate(CreateView):
    model = Bicicleta
    form_class = bicicletaForm
    template_name = 'Registro/agregar_bicicleta.html'
    success_url = reverse_lazy("listar_bicicletas")

# clase listar bicicleta


class BicicletaList(ListView):
    model = Bicicleta
    template_name = 'Registro/listar_bicicletas.html'

# clase modificar bicicleta


class BicicletaUpdate(UpdateView):
    model = Bicicleta
    form_class = bicicletaForm
    template_name = 'Registro/editar_bicicleta.html'
    success_url = reverse_lazy('listar_bicicletas')

# clase borrar bicicleta


class BicicletaDelete(DeleteView):
    model = Bicicleta
    template_name = 'Registro/bicicleta_delete.html'
    success_url = reverse_lazy('listar_bicicletas')

# filtros


def ListBicicleta(request):
    lista = Bicicleta.objects.all()
    id_bicicleta = request.GET.get('id-bicicleta')

    if 'btn-id-bicicleta' in request.GET:
        if id_bicicleta:
            lista = Bicicleta.objects.filter(id_bicicleta__icontains=id_bicicleta)
    data = {
        'object_list': lista
    }
    return render(request, 'Registro/listar_bicicleta_filtros.html', data)
