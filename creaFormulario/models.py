import django
from django.db import models


class Formulario(models.Model):
    email_institucional = models.EmailField(null=True, )
    titulo = models.CharField(null=True, max_length=500)
    nombre = models.CharField(null=True, max_length=200)
    email = models.EmailField(null=True, )
    telefono = models.CharField(null=True, max_length=50)
    contacto = models.CharField(null=True, max_length=200)
    email_adicional = models.EmailField(null=True, )
    divulgacion = models.BooleanField(null=False, default=False)
    divulgacion_info = models.CharField(max_length=200)
    divulgacion_fecha_1 = models.DateField(
        null=True, default=django.utils.timezone.now)
    divulgacion_fecha_2 = models.DateField(
        null=True, default=django.utils.timezone.now)
    divulgacion_fecha_3 = models.DateField(
        null=True, default=django.utils.timezone.now)
    divulgacion_evidencia = models.URLField(null=True)
    keywords = models.CharField(null=True, max_length=500)
    area_aplicacion = models.CharField(null=True, max_length=100)
    tipo_invencion = models.CharField(null=True, max_length=100)
    descripcion = models.CharField(null=True, max_length=500)
    problematica = models.CharField(null=True, max_length=500)
    relevantes = models.CharField(null=True, max_length=500)
    ocurrencia = models.CharField(null=True, max_length=500)
    obvia = models.CharField(null=True, max_length=200)
    financiamiento = models.CharField(null=True, max_length=100)
    financiamiento_especifique = models.CharField(null=True, max_length=100)
    invencion_involucramiento = models.BooleanField(null=True, default=False)
    involucrameinto = models.CharField(null=True, max_length=200)
    convenios = models.BooleanField(null=True, default=False)
    convenios_tipo = models.CharField(null=True, max_length=200)
    necesidad = models.CharField(null=True, max_length=50)
    mercado = models.BooleanField(default=False)
    mercado_especifique = models.CharField(null=True, max_length=200)
    interes = models.BooleanField(null=True, default=False)
    interes_especifique = models.CharField(null=True, max_length=200)
    discovery = models.BooleanField(null=True, default=False)
    discovery_especifique = models.CharField(null=True, max_length=200)
    informacion_tecnica = models.URLField(null=True, )
    compromiso = models.BooleanField(null=True, default=True)
    contacto_empresa = models.BooleanField(null=True, default=False)
    contacto_especifique = models.CharField(null=True, max_length=500)

    class Meta:
        ordering = ['nombre', 'titulo']

    def __str__(self):
        return f'Formulario de invención del inventor {self.nombre} titulado {self.titulo}.'
