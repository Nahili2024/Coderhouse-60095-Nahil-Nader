from django.shortcuts import get_object_or_404, redirect, render
from .forms import VendedorForm, TransaccionForm, ReporteForm
from .models import Vendedor, Transaccion, Reporte
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def index(request):
    return render(request, "minegocio/index.html")

def about(request):
    return render(request,"minegocio/about.html")

@login_required
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

def vendedor_edit(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, pk=vendedor_id)
    if request.method == "POST":
        form = VendedorForm(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            return redirect('minegocio:vendedor_list')
    else:
        form = VendedorForm(instance=vendedor)
    return render(request, "minegocio/vendedor_form.html", {"form": form})

def vendedor_delete(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, pk=vendedor_id)
    if request.method == "POST":
        vendedor.delete()
        return redirect('minegocio:vendedor_list')
    return render(request, "minegocio/vendedor_confirm_delete.html", {"vendedor": vendedor})

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

def transaccion_edit(request, transaccion_id):
    transaccion = get_object_or_404(Transaccion, pk=transaccion_id)
    if request.method == "POST":
        form = TransaccionForm(request.POST, instance=transaccion)
        if form.is_valid():
            form.save()
            return redirect('minegocio:transaccion_list')
    else:
        form = TransaccionForm(instance=transaccion)
    return render(request, "minegocio/transaccion_form.html", {"form": form})

def transaccion_delete(request, transaccion_id):
    transaccion = get_object_or_404(Transaccion, pk=transaccion_id)
    if request.method == "POST":
        transaccion.delete()
        return redirect('minegocio:transaccion_list')
    return render(request, "minegocio/transaccion_confirm_delete.html", {"transaccion": transaccion})



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




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('minegocio:index')
            else:
                form.add_error(None, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'minegocio/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('minegocio:login')
    else:
        form = UserCreationForm()
    return render(request, 'minegocio/signup.html', {'form': form})


