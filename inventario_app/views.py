from django.shortcuts import render, redirect
from .models import Inventario
# Create your views here.


def vista_indexInventario(request):
    inventario = Inventario.objects.all()
    return render(request, "index_inventario.html", {"inventario": inventario})


def registrarInventario(request):
    id_inventario = request.POST['txt_idinventario']
    producto = request.POST['txt_producto']
    tipo = request.POST['num_tipo']
    cantidad = request.POST['num_cantidad']
    categoria = request.POST['txt_categoria']
    id_producto = request.POST['txt_id_producto']
    disponible = request.POST['disponible']

    guardarinventario = Inventario.objects.create(id_inventario = id_inventario, producto = producto, tipo = tipo, cantidad=cantidad, categoria=categoria, id_producto=id_producto, disponible=disponible)
    return redirect("inventario") 

def seleccionarInventario(request, id_inventario):
    inventario = Inventario.objects.get(id_inventario=id_inventario)
    return render(request, "editarInventario.html", {"inventario": inventario})


def editarInventario(request):
    id_inventario = request.POST['txt_idinventario']
    producto = request.POST['txt_producto']
    tipo = request.POST['num_tipo']
    cantidad = request.POST['num_cantidad']
    categoria = request.POST['txt_categoria']
    id_producto = request.POST['txt_id_producto']
    disponible = request.POST['disponible']


    inventario = Inventario.objects.get(id_inventario=id_inventario)
    inventario.producto = producto
    inventario.tipo = tipo
    inventario.cantidad = cantidad
    inventario.categoria = categoria
    inventario.id_producto = id_producto
    inventario.disponible = disponible
    inventario.save()
    return redirect("inventario") 


def borrarInventario(request,id_inventario):
    inv = Inventario.objects.get(id_inventario=id_inventario)
    inv.delete()
    
    return redirect("inventario")