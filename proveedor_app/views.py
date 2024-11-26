from django.shortcuts import render, redirect
from .models import Proveedor
# Create your views here.


def vista_indexProveedor(request):
    proveedor = Proveedor.objects.all()
    return render(request, "index_proveedor.html", {"proveedor": proveedor})


def registrarProveedor(request):
    id_proveedor = request.POST['txt_idproveedor']
    nombre = request.POST['txt_nombre']
    direccion = request.POST['num_direccion']
    tipo_prod = request.POST['num_tipo']
    cantidad = request.POST['txt_cantidad']
    contacto = request.POST['txt_contacto']
    fecha = request.POST['fecha']

    guardarproveedor = Proveedor.objects.create(id_proveedor = id_proveedor, nombre = nombre, direccion = direccion, tipo_prod=tipo_prod, cantidad=cantidad, contacto=contacto, fecha=fecha)
    return redirect("proveedor") 

def seleccionarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request, "editarProveedor.html", {"proveedor": proveedor})


def editarProveedor(request):
    id_proveedor = request.POST['txt_idproveedor']
    nombre = request.POST['txt_nombre']
    direccion = request.POST['num_direccion']
    tipo_prod = request.POST['num_tipo']
    cantidad = request.POST['txt_cantidad']
    contacto = request.POST['txt_contacto']
    fecha = request.POST['fecha']

    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre = nombre
    proveedor.direccion = direccion
    proveedor.tipo_prod = tipo_prod
    proveedor.cantidad = cantidad
    proveedor.contacto = contacto
    proveedor.fecha = fecha
    proveedor.save()
    return redirect("proveedor") 


def borrarProveedor(request,id_proveedor):
    prove = Proveedor.objects.get(id_proveedor=id_proveedor)
    prove.delete()
    
    return redirect("proveedor")