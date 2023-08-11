from django.urls import path
from . import views
app_name = 'registros'

urlpatterns = [
    path('', views.listaRegistros, name='listaRegistros'),
    path('nuevo/', views.nuevoRegistro, name='nuevoRegistro'),
    path('<int:requisito_id>/contestacion/',
         views.nuevaContestacion, name='nuevaContestacion'),
    path('<slug:slug>/requisito/', views.nuevoRequisito, name='nuevoRequisito'),
    path('<slug:slug>/resolucion/', views.nuevaResolucion, name='nuevaResolucion'),
    path('<slug:slug>/', views.detalleRegistro, name='detalleRegistro'),
    path('<slug:slug>/borraRegistro/', views.borraRegistro, name='borraRegistro'),

]
