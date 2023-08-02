from django.urls import path
from . import views
app_name = 'creaFormulario'

urlpatterns = [
    path('', views.formulario_list, name='listaFormulario'),
    path('carga/', views.cargaExcel, name='cargaExcel'),
    path('<int:formulario_id>/creaFormulario/',
         views.generaFormulario, name='generaFormulario'),
    path('<int:formulario_id>/borrarFormulario/',
         views.deleteFormulario, name='deleteFormulario'),
    path('<int:formulario_id>/ingresaFormulario/',
         views.ingresaFormulario, name='ingresaFormulario'),
]
