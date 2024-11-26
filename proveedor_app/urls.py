from django.urls import path
from proveedor_app import views

urlpatterns = [
    path("proveedorsss", views.vista_indexProveedor, name="proveedor"),
    path("registrarProveedor/", views.registrarProveedor, name="registrarProveedor"),
    path("seleccionarProveedor/<id_proveedor>", views.seleccionarProveedor, name="seleccionarProveedor"),
    path("editarProveedor/", views.editarProveedor, name="editarProveedor"),
    path("borrarProveedor/<id_proveedor>", views.borrarProveedor, name="borrarProveedor"),
]
