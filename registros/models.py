from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse


class Registro(models.Model):
    folio_regex = r'^(MX\/[afu]\/[0-9]{4}\/[0-9]{6})$'
    folio_validator = RegexValidator(
        regex=folio_regex, message='Formato del folio no válido', code='invalid_folio')

    folio = models.CharField(max_length=20, blank=False, validators=[folio_validator],
                             default='MX/x/yyyy/000000', unique=True)
    slug = models.SlugField(max_length=20, unique=True, null=True)
    titulo = models.CharField(max_length=500, blank=False, default='')
    solicitante = models.CharField(
        max_length=200, blank=False, default='Universidad Autónoma de Nuevo León')
    fecha_presentacion = models.DateField(default=timezone.now, blank=False)
    apoderado = models.CharField(max_length=10, default='LNGP')
    rgp = models.CharField(max_length=20, default='DDAJ-000163/2023')
    figura = models.CharField(max_length=15, default='Patente')
    added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-folio', '-fecha_presentacion', '-added']
        indexes = [models.Index(fields=['figura'])]

    def __str__(self):
        return f'{self.folio}'

    def get_absolute_url(self):
        return reverse('datalleRegistro', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.folio).replace("/", "-")
        return super().save(*args, **kwargs)


class Requisito(models.Model):
    class TiposRequisitos(models.TextChoices):
        FORMA1 = 'FORMA1', '1er. Requisito del Examen de Forma'
        FORMA2 = 'FORMA2', '2do. Requisito del Examen de Forma'
        FORMAS = 'FORMAS', 'SATISFECHO'
        FONDO1 = 'FONDO1', '1er. Requisito del Examen de Fondo'
        FONDO2 = 'FONDO2', '2do. Requisito del Examen de Fondo'
        FONDO3 = 'FONDO3', '3er. Requisito del Examen de Fondo'
        FONDO4 = 'FONDO4', '4to. Requisito del Examen de Fondo'
        OTORGADA = 'OTORGADA', 'OTORGADA'
        DESISTIDA = 'DESISTIDA', 'DESISTIDA'
        NEGADA = 'NEGADA', 'NEGADA'
        ABANDONADA = 'ABANDONADA', 'ABANDONADA'

    tipo = models.CharField(
        max_length=34, choices=TiposRequisitos.choices, default=TiposRequisitos.FORMA1)
    folio = models.IntegerField(blank=False)
    fecha = models.DateField(blank=False, default=timezone.now)
    registro = models.ForeignKey(
        Registro, on_delete=models.CASCADE, related_name='requisito')

    def __str__(self):
        return f'{self.tipo} con número de folio {self.folio} recibido en fecha {self.fecha} del expediente {self.registro}.'


class Contestacion(models.Model):
    fecha = models.DateField(blank=False, default=timezone.now)
    folio = models.CharField(
        max_length=20, blank=False, default='MX/E/2023/000000')
    requisito = models.ForeignKey(
        Requisito, on_delete=models.CASCADE, related_name='contestacion')

    def __str__(self):
        return f'Contestación al Oficio IMPI-{self.requisito.folio}'


class Titulo(models.Model):
    numero = models.IntegerField(blank=False, null=False)
    expedido = models.DateField()
    notificado = models.DateField()
    registro = models.ForeignKey(
        Registro, on_delete=models.CASCADE, related_name="titulo_no")

    def __str__(self):
        return f'Título del expediente {self.registro} No. {self.numero}'
