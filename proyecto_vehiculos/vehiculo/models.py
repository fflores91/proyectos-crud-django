from django.db import models
from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

@receiver(post_save, sender=User)
def assign_visualizar_catalogo_permission(sender, instance, created, **kwargs):
    if created:
        content_type = ContentType.objects.get_for_model(instance)
        codename = 'visualizar_catalogo'
        name = 'Visualizar Catálogo de Vehículos'
        try:
            permission = Permission.objects.get(content_type=content_type, codename=codename)
        except Permission.DoesNotExist:
            permission = Permission.objects.create(content_type=content_type, codename=codename, name=name)
        instance.user_permissions.add(permission)
        
class VehiculoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehiculo'

    def ready(self):
        # Crear el permiso "visualizar_catalogo"
        content_type = ContentType.objects.get_for_model(Vehiculo)
        Permission.objects.get_or_create(
            codename='visualizar_catalogo',
            name='Visualizar Catálogo de Vehículos',
            content_type=content_type,
        )

class Vehiculo(models.Model):
    MARCA_CHOICES = (
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    )

    CATEGORIA_CHOICES = (
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    )

    marca = models.CharField(max_length=20, choices=MARCA_CHOICES, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.marca} - {self.modelo}"
    

