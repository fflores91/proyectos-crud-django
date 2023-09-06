from django.contrib import admin
from django.urls import path, include
from laboratorio import views as laboratorio_views  # Importar la vista de redirección

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', laboratorio_views.redireccion_lista),  # URL para la redirección
    path('laboratorio/', include('laboratorio.urls')),
]
