from django.contrib import admin
from .models import Inventor, Dependencias, Correo, Telefono

# Register your models here.


class InventorInfo(admin.ModelAdmin):
    list_display = ('nombre', 'dependencia', 'tipo', 'numero')


class CorreoInfo(admin.ModelAdmin):
    list_display = ('correo', 'inventor')


class TelefonoInfo(admin.ModelAdmin):
    list_display = ('telefono', 'inventor')


admin.site.register(Inventor, InventorInfo)
admin.site.register(Dependencias)
admin.site.register(Correo, CorreoInfo)
admin.site.register(Telefono, TelefonoInfo)
