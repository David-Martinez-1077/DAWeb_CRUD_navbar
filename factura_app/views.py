from django.shortcuts import render, redirect
from .models import Factura
# Create your views here.


def vista_indexFactura(request):
    factura = Factura.objects.all()
    return render(request, "index_factura.html", {"factura": factura})


def registrarFactura(request):
    id_factura = request.POST['txt_idfactura']
    id_cliente = request.POST['txt_idcliente']
    id_producto = request.POST['num_idproducto']
    metodo_pago = request.POST['num_metodo']
    total = request.POST['num_total']
    id_trabajador = request.POST['txt_idtrabajador']
    fecha = request.POST['fecha']

    guardarfactura = Factura.objects.create(id_factura = id_factura, id_cliente = id_cliente, id_producto = id_producto, metodo_pago=metodo_pago, total=total, id_trabajador=id_trabajador, fecha=fecha)
    return redirect("factura") 

def seleccionarFactura(request, id_factura):
    factura = Factura.objects.get(id_factura=id_factura)
    return render(request, "editarFactura.html", {"factura": factura})


def editarFactura(request):
    id_factura = request.POST['txt_idfactura']
    id_cliente = request.POST['txt_idcliente']
    id_producto = request.POST['num_idproducto']
    metodo_pago = request.POST['num_metodo']
    total = request.POST['num_total']
    id_trabajador = request.POST['txt_idtrabajador']
    fecha = request.POST['fecha']


    factura = Factura.objects.get(id_factura=id_factura)
    factura.id_cliente = id_cliente
    factura.id_producto = id_producto
    factura.metodo_pago = metodo_pago
    factura.total = total
    factura.id_trabajador = id_trabajador
    factura.fecha = fecha
    factura.save()
    return redirect("factura") 


def borrarFactura(request,id_factura):
    fac = Factura.objects.get(id_factura=id_factura)
    fac.delete()
    
    return redirect("factura")