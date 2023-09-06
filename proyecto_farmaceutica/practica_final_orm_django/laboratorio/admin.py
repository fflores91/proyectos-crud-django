from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

class DirectorGeneralInline(admin.StackedInline):
    model = DirectorGeneral

class ProductoInline(admin.TabularInline):
    model = Producto

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    inlines = [DirectorGeneralInline, ProductoInline]

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
