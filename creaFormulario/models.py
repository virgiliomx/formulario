import django
from django.db import models


class Formulario(models.Model):
    email_institucional = models.EmailField()
    titulo = models.CharField(max_length=500)
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    contacto = models.CharField(max_length=200)
    email_adicional = models.EmailField()
    divulgacion = models.BooleanField(blank=False, default=False)
    divulgacion_info = models.CharField(max_length=200)
    divulgacion_fecha_1 = models.DateField(blank=True, default=django.utils.timezone.now)
    divulgacion_fecha_2 = models.DateField(blank=True, default=django.utils.timezone.now)
    divulgacion_fecha_3 = models.DateField(blank=True, default=django.utils.timezone.now)
    divulgacion_evidencia = models.URLField(blank=True)
    keywords = models.CharField(max_length=500)
    area_aplicacion = models.CharField(max_length=100)
    tipo_invencion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    problematica = models.CharField(max_length=500)
    relevantes =  models.CharField(max_length=500)
    ocurrencia = models.CharField(max_length=500)
    obvia = models.CharField(max_length=200)
    financiamiento = models.CharField(max_length=100)
    financiamiento_especifique = models.CharField(max_length=100)
    invencion_involucramiento = models.BooleanField(default=False)
    involucrameinto = models.CharField(max_length=200)
    convenios = models.BooleanField(default=False)
    convenios_tipo = models.CharField(max_length=200)
    necesidad = models.CharField(max_length=50)
    mercado = models.BooleanField(default=False)
    mercado_especifique = models.CharField(max_length=200)
    interes = models.BooleanField(default=False)
    interes_especifique = models.CharField(max_length=200)
    discovery = models.BooleanField(default=False)
    discovery_especifique = models.CharField(max_length=200)
    informacion_tecnica = models.URLField()
    compromiso = models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre', 'titulo']

    def __str__(self):
        return f'Formulario de infención del inventor {self.nombre} titulado {self.titulo}.'
