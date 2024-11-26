from django.urls import path
from cliente_app import views

urlpatterns = [
  path("cliente", views.vista_indexCliente, name="cliente"),
  path("registrarCliente/", views.registrarMateria, name="registrarMateria"),
  path("seleccionarCliente/<id_cliente>", views.seleccionarCliente, name="seleccionarCliente"),
  path("editarCliente/", views.editarCliente, name="editarCliente"),
  path("borrarCliente/<id_cliente>", views.borrarCliente, name="borrarCliente"),
    
]

