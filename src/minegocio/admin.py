from django.contrib import admin

# Register your models here.

from .models import Vendedor, Producto, Transaccion, Reporte   

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ("nombre","dni")

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ("dni","fecha","cantidad","producto","monto")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("categoria")

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ("dni","año","informe","periodo")