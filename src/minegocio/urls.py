from django.urls import path
from .views import (index, about, vendedor_create, vendedor_list, transaccion_create, transaccion_list, reporte_create, reporte_list)

app_name = "minegocio"

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),path("vendedor/list/", vendedor_list, name="vendedor_list"),
    path("vendedor/create/", vendedor_create, name="vendedor_create"),
    path("transaccion/list/", transaccion_list, name="transaccion_list"),
    path("transaccion/create/", transaccion_create, name="transaccion_create"),
    path("reporte/list/", reporte_list, name="reporte_list"),
    path("reporte/create/", reporte_create, name="reporte_create"),
]
