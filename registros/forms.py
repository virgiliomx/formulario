from django import forms
from .models import Registro, Requisito, Titulo, Contestacion, Resolucion


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['folio', 'titulo', 'solicitante',
                  'fecha_presentacion', 'apoderado', 'rgp']


class RequisitoForm(forms.ModelForm):
    class Meta:
        model = Requisito
        fields = ['tipo', 'folio', 'fecha']


class ResolucionForm(forms.ModelForm):
    class Meta:
        model = Resolucion
        fields = ['resolucion', 'folio', 'fecha']

    """def __init__(self, requisito, *args, **kwargs):
        super(RequisitoForm, self).__init__(*args, **kwargs)
        if requisito is None:
            self.fields['tipo'].choices = Requisito.TiposRequisitos.FORMA1, Requisito.TiposRequisitos.FORMAS
        if requisito == 'FORMA1':
            self.fields['tipo'].choices = Requisito.TiposRequisitos.FORMA2, Requisito.TiposRequisitos.FORMAS, Requisito.TiposRequisitos.FONDO1
        if requisito == 'FORMA2':
            self.fields['tipo'].choices = Requisito.TiposRequisitos.FORMAS, Requisito.TiposRequisitos.FONDO1
        if requisito == 'FORMAS':
            self.fields['tipo'].choices = Requisito.TiposRequisitos.FONDO1
        if requisito == 'FONDO1':
            self.fields['tipo'].choices = Requisito.TiposRequisitos.FONDO2
        if requisito == 'FONDO2':
            self.fields['tipo'].choices = Requisito.TiposRequisitos.FONDO3
        if requisito == 'FONDO3':
            self.fields['tipo'].choices = Requisito.TiposRequisitos.FONDO4"""


class ContestacionForm(forms.ModelForm):
    class Meta:
        model = Contestacion
        fields = ['fecha', 'folio']


class TituloForm(forms.ModelForm):
    class Meta:
        model = Titulo
        fields = ['numero', 'expedido', 'notificado']
