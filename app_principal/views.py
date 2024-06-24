from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from .forms import EventoForm

def home(request):
    return render(request, 'app_principal/home.html')

# Create

def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm()
    return render(request, 'app_principal/evento_form.html', {'form': form})

# Read
def evento_list(request):
    eventos = Evento.objects.all()
    return render(request, 'app_principal/evento_list.html', {'eventos': eventos})

# Update
def evento_update(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'app_principal/evento_form.html', {'form': form})

# Delete
def evento_delete(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento_list')
    return render(request, 'app_principal/evento_confirm_delete.html', {'evento': evento})