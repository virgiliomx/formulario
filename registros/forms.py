from django import forms
from .models import Registro, Requisito, Titulo


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['folio', 'titulo', 'solicitante',
                  'fecha_presentacion', 'apoderado', 'rgp']


class RequisitoForm(forms.ModelForm):
    class Meta:
        model = Requisito
        fields = ['tipo', 'folio', 'fecha']


class TituloForm(forms.ModelForm):
    class Meta:
        model = Titulo
        fields = ['numero', 'expedido', 'notificado']
