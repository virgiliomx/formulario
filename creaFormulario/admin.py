from django.contrib import admin
from .models import Formulario

# Register your models here.

class FormularioInfo(admin.ModelAdmin):
    list_display = ('nombre', 'titulo', 'divulgacion')


admin.site.register(Formulario, FormularioInfo)
