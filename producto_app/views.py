from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.


def vista_indexProducto(request):
    producto = Producto.objects.all()
    return render(request, "index_producto.html", {"producto": producto})


def registrarProducto(request):
    id_producto = request.POST['txt_idproducto']
    nombre_producto = request.POST['txt_nombre']
    precio = request.POST['num_precio']
    stock = request.POST['num_stock']
    categoria = request.POST['txt_categoria']
    descripcion = request.POST['txt_desc']
    fecha = request.POST['fecha']

    guardarmateria = Producto.objects.create(id_producto = id_producto, nombre_producto = nombre_producto, precio = precio, stock=stock, categoria=categoria, descripcion=descripcion, fecha=fecha)
    return redirect("producto") 

def seleccionarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    return render(request, "editarProducto.html", {"producto": producto})


def editarProducto(request):
    id_producto = request.POST['txt_idproducto']
    nombre_producto = request.POST['txt_nombre']
    precio = request.POST['num_precio']
    stock = request.POST['num_stock']
    categoria = request.POST['txt_categoria']
    descripcion = request.POST['txt_desc']
    fecha = request.POST['fecha']

    producto = Producto.objects.get(id_producto=id_producto)
    producto.nombre_producto = nombre_producto
    producto.precio = precio
    producto.stock = stock
    producto.categoria = categoria
    producto.descripcion = descripcion
    producto.fecha = fecha
    producto.save()
    return redirect("producto") 


def borrarProducto(request,id_producto):
    prod = Producto.objects.get(id_producto=id_producto)
    prod.delete()
    
    return redirect("producto")