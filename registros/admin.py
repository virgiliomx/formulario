from django.contrib import admin
from .models import Registro, Requisito, Titulo


class RegistroInfo(admin.ModelAdmin):
    list_display = ('folio', 'titulo')


class RequisitoInfo(admin.ModelAdmin):
    list_display = ('folio', 'registro')


class TituloInfo(admin.ModelAdmin):
    list_display = ('numero', 'registro')


admin.site.register(Registro, RegistroInfo)
admin.site.register(Requisito, RequisitoInfo)
admin.site.register(Titulo, TituloInfo)
