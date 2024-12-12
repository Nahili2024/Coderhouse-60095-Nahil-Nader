from django import forms

from .models import Vendedor, Transaccion, Reporte


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = "__all__"


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
        }


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = "__all__"