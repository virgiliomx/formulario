from django.urls import path
from . import views
app_name = 'inventores'

urlpatterns = [
    path('', views.listaInventores, name='listaInventores'),
    path('nuevo/', views.nuevoInventor, name='nuevoInventor'),
    path('carga-inventores/', views.cargaExcel, name='cargaExcel'),
    path('dependencia/', views.nuevaDependencia, name='nuevaDependencia'),
    path('<slug:slug>/correo/', views.nuevoCorreo, name='nuevoCorreo'),
    path('<slug:slug>/telefono/', views.nuevoTelefono, name='nuevoTelefono'),
    path('<slug:slug>/', views.detalleInventor, name='detalleInventor'),
    path('<slug:slug>/borraInventor/', views.borraInventor, name='borraInventor'),
    path('<int:correo_id>/borraCorreo/', views.borraCorreo, name='borraCorreo'),
    path('<int:telefono_id>/borraTelefono/',
         views.borraTelefono, name='borraTelefono'),
    path('<slug:slug>/registro/', views.nuevoRegistro, name='nuevoRegistro'),
]
