from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('insertar/', views.insertar_laboratorio, name='insertar_laboratorio'),
    path('editar/<int:laboratorio_id>/', views.editar_laboratorio, name='editar_laboratorio'),
    path('eliminar/<int:laboratorio_id>/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
    path('redireccion_lista/', views.redireccion_lista, name='redireccion_lista'),  # Agregamos esta ruta
    path('listar/', views.listar_laboratorios, name='listar_laboratorios'),
    path('detalle_laboratorio/<int:laboratorio_id>/', views.detalle_laboratorio, name='detalle_laboratorio'),
]
