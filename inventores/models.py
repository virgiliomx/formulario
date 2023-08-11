from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# from ..registros.models import Registro


class Dependencias(models.Model):
    nombre = models.CharField(
        max_length=150, unique=True, blank=False, null=False)

    class Meta:
        ordering = ['-nombre']

    def __str__(self):
        return f'{self.nombre}'


class Inventor(models.Model):
    class Tipos(models.TextChoices):
        EMPLEADO = 'E', 'Empleado'
        ALUMNO = 'A', 'Alumno'

    nombre = models.CharField(
        max_length=200, unique=True, blank=False, null=False)
    tipo = models.CharField(
        max_length=8, choices=Tipos.choices, default=Tipos.EMPLEADO)
    numero = models.IntegerField(
        blank=False, default=0, null=False, unique=True)
    dependencia = models.ForeignKey(
        Dependencias, on_delete=models.CASCADE, related_name='dependencia')
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-nombre', '-dependencia',]
        indexes = [models.Index(fields=['nombre', 'tipo'])]

    def get_absolute_url(self):
        return reverse("detalleInventor", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        return super().save(*args, **kwargs)


class Correo(models.Model):
    correo = models.EmailField(max_length=100, blank=False, null=False)
    inventor = models.ForeignKey(Inventor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.correo} del inventor {self.inventor}'


class Telefono(models.Model):
    telefono = models.EmailField(max_length=100, blank=False, null=False)
    inventor = models.ForeignKey(Inventor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.telefono} del inventor {self.inventor}'
