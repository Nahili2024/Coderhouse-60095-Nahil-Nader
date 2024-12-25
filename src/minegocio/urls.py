from django.urls import path
from .views import (index, about, vendedor_create, vendedor_list, 
                    transaccion_create, transaccion_list, 
                    reporte_create, reporte_list, vendedor_detail,
                    vendedor_edit, vendedor_delete,transaccion_detail, 
                    transaccion_edit, transaccion_delete,
                    login_view, signup_view)
from django.contrib.auth.views import LogoutView

app_name = "minegocio"

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path("vendedor/list/", vendedor_list, name="vendedor_list"),
    path("vendedor/create/", vendedor_create, name="vendedor_create"),
    path("vendedor/detail/<int:vendedor_id>/", vendedor_detail, name="vendedor_detail"),
    path("vendedor/edit/<int:vendedor_id>/", vendedor_edit, name="vendedor_edit"),
    path("vendedor/delete/<int:vendedor_id>/", vendedor_delete, name="vendedor_delete"),
    path("transaccion/list/", transaccion_list, name="transaccion_list"),
    path("transaccion/create/", transaccion_create, name="transaccion_create"),
    path("transaccion/detail/<int:transaccion_id>/", transaccion_detail, name="transaccion_detail"),
    path("transaccion/edit/<int:transaccion_id>/", transaccion_edit, name="transaccion_edit"),
    path("transaccion/delete/<int:transaccion_id>/", transaccion_delete, name="transaccion_delete"),
    path("reporte/list/", reporte_list, name="reporte_list"),
    path("reporte/create/", reporte_create, name="reporte_create"),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

