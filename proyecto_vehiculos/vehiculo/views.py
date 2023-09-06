from django.shortcuts import redirect, render
from .forms import VehiculoForm
from .models import Vehiculo

def index(request):
    return render(request, 'vehiculo/index.html')

# Vista para agregar un nuevo vehículo
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vehiculos')
    else:
        form = VehiculoForm()
    
    context = {'form': form}
    return render(request, 'vehiculo/agregar_vehiculo.html', context)

# Vista para listar los vehículos
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehiculos': vehiculos})