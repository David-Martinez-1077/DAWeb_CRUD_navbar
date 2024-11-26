from django.urls import path
from trabajadores_app import views

urlpatterns = [
    path("trabajador", views.vista_indexTrabajador, name="trabajador"),
    path("registrarTrabajador/", views.registrarTrabajador, name="registrarTrabajador"),
    path("seleccionarTrabajador/<id_trabajador>", views.seleccionarTrabajador, name="seleccionarTrabajador"),
    path("editarTrabajador/", views.editarTrabajador, name="editarTrabajador"),
    path("borrarTrabajador/<id_trabajador>", views.borrarTrabajador, name="borrarTrabajador"),
    
]

