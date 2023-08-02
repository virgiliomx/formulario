from django.urls import path
from . import views
app_name = 'registros'

urlpatterns = [
    path('', views.listaRegistros, name='listaRegistros'),
    path('nuevo/', views.nuevoRegistro, name='nuevoRegistro'),
    path('<slug:slug>/', views.detalleRegistro, name='detalleRegistro'),
    # path('<int:formulario_id>/creaFormulario/',
    #     views.generaFormulario, name='generaFormulario'),
    # path('<int:formulario_id>/borrarFormulario/',
    #     views.deleteFormulario, name='deleteFormulario'),
    # path('<int:formulario_id>/ingresaFormulario/',
    #     views.ingresaFormulario, name='ingresaFormulario'),
]
