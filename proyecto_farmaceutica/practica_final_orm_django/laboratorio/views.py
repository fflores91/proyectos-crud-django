from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio
from .forms import LaboratorioForm

def inicio(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'lista_laboratorios.html', {'laboratorios': laboratorios})

def insertar_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LaboratorioForm()
    return render(request, 'insertar_laboratorio.html', {'form': form})

def editar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'editar_laboratorio.html', {'form': form, 'laboratorio': laboratorio})

def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('inicio')
    return render(request, 'eliminar_laboratorio.html', {'laboratorio': laboratorio})

def redireccion_lista(request):
    return redirect('inicio')

def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'lista_laboratorios.html', {'laboratorios': laboratorios})

def detalle_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    return render(request, 'detalle_laboratorio.html', {'laboratorio': laboratorio})