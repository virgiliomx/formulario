from django import forms
from .models import Dependencias, Inventor, Correo, Telefono


class DependenciasForm(forms.ModelForm):
    class Meta:
        model = Dependencias
        fields = ['nombre']


class InventorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dependencia'].queryset = Dependencias.objects.all()

    class Meta:
        model = Inventor
        fields = ['nombre', 'tipo', 'numero', 'dependencia']


class CorreoForm(forms.ModelForm):
    class Meta:
        model = Correo
        fields = ['correo']


class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ['telefono']
