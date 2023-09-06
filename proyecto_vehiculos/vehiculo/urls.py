from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_vehiculo, name='vehiculo_add'),
    path('listar/', views.listar_vehiculos, name='listar_vehiculos'),
]
