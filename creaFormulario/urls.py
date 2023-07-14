from django.urls import path
from . import views
app_name = 'creaFormulario'

urlpatterns = [
    path('', views.formulario_list, name='listaFormulario'),
    path('carga/', views.cargaExcel, name='cargaExcel'),
]
