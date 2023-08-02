from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.


class Registro(models.Model):

    class Estatus(models.TextChoices):
        TRAMITE = 'T', 'EN TRÁMITE'
        ABANDONADA = 'A', 'ABANDONADA'
        DESISTIDA = 'D', 'DESISTIDA'
        NEGADA = 'N', 'NEGADA'
        OTORGADA = 'O', 'OTORGADA'

    folio = models.CharField(max_length=20, blank=False,
                             default='MX/x/yyyy/000000', unique=True)
    slug = models.SlugField(max_length=20, unique=True, null=True)
    titulo = models.CharField(max_length=500, blank=False, default='')
    solicitante = models.CharField(
        max_length=200, blank=False, default='Universidad Autónoma de Nuevo León')
    fecha_presentacion = models.DateField(default=timezone.now, blank=False)
    apoderado = models.CharField(max_length=10, default='LNGP')
    rgp = models.CharField(max_length=20, default='DDAJ-000163/2023')
    figura = models.CharField(max_length=15, default='Patente')
    forma = models.CharField(max_length=12, blank=True, null=True)
    forma_folio = models.IntegerField(null=True, blank=True)
    forma_fecha = models.DateField(null=True, blank=True)
    resolucion = models.CharField(
        max_length=1, choices=Estatus.choices, default=Estatus.TRAMITE)

    class Meta:
        ordering = ['-folio', '-fecha_presentacion']
        indexes = [models.Index(fields=['figura'])]

    def __str__(self):
        return f'{self.figura} titulada {self.titulo} con número de expediente {self.folio}'

    def get_absolute_url(self):
        return reverse('datalleRegistro', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:

            self.slug = slugify(self.folio).replace("/", "-")
        return super().save(*args, **kwargs)


class Requisito(models.Model):
    tipo = models.CharField(max_length=20, blank=False)
    folio = models.IntegerField(blank=False)
    fecha = models.DateField(blank=False, default=timezone.now)
    registro = models.ForeignKey(
        Registro, on_delete=models.CASCADE, related_name='requisito')

    def __str__(self):
        return f'Examen de {self.tipo} con número de folio {self.folio} recibido en fecha {self.fecha} del expediente {self.registro}.'


class Titulo(models.Model):
    numero = models.IntegerField(blank=False, null=False)
    expedido = models.DateField()
    notificado = models.DateField()
    registro = models.ForeignKey(
        Registro, on_delete=models.CASCADE, related_name="titulo_no")

    def __str__(self):
        return f'Título del expediente {self.registro} No. {self.numero}'
