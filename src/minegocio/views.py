from django.shortcuts import render, redirect
from .forms import VendedorForm, TransaccionForm, ReporteForm
from .models import Vendedor, Transaccion, Reporte

# Create your views here.

def index(request):
    return render(request, "minegocio/index.html")

def about(request):
    return render(request,"minegocio/about.html")

def vendedor_list(request):
    query = Vendedor.objects.all()
    context = {"object_list": query}
    return render(request, "minegocio/vendedor_list.html", context)


def vendedor_create(request):
    if request.method == "GET":
        form = VendedorForm()
    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("minegocio:vendedor_list")
    return render(request, "minegocio/vendedor_form.html", {"form": form})


def transaccion_list(request):
    query = Transaccion.objects.all()
    context = {"object_list": query}
    return render(request, "minegocio/transaccion_list.html", context)


def transaccion_create(request):
    if request.method == "GET":
        form = TransaccionForm()
    if request.method == "POST":
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("minegocio:transaccion_list")
    return render(request, "minegocio/transaccion_form.html", {"form": form})


def reporte_list(request):
    query = Reporte.objects.all()
    context = {"object_list": query}
    return render(request, "minegocio/reporte_list.html", context)


def reporte_create(request):
    if request.method == "GET":
        form = ReporteForm()
    if request.method == "POST":
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("minegocio:reporte_list")
    return render(request, "minegocio/reporte_form.html", {"form": form})