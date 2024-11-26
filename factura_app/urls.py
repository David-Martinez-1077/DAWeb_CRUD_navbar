from django.urls import path
from factura_app import views

urlpatterns = [
  path("factura", views.vista_indexFactura, name="factura"),
  path("registrarFactura/", views.registrarFactura, name="registrarFactura"),
  path("seleccionarFactura/<id_factura>", views.seleccionarFactura, name="seleccionarFactura"),
  path("editarFactura/", views.editarFactura, name="editarFactura"),
  path("borrarFactura/<id_factura>", views.borrarFactura, name="borrarFactura"),
    
]

