from django import forms
from .models import Vendedor, Transaccion, Reporte
from django.contrib.auth.models import User


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dni'].queryset = Vendedor.objects.all()
        self.fields['dni'].label_from_instance = lambda obj: obj.dni


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = "__all__"


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']