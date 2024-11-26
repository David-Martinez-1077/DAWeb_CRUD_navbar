from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.


def vista_indexCliente(request):
  cliente = Cliente.objects.all()
  return render(request, "index_luxurylingerie.html", {"cliente": cliente})


def registrarMateria(request):
    id_cliente = request.POST['txt_idcliente']
    nombre = request.POST['txt_nombre']
    apellido = request.POST['txt_apellido']
    telefono = request.POST['txt_telefono']
    fecha = request.POST['fecha']
    edad = request.POST['edad']
    genero = request.POST['genero']

    guardarmateria = Cliente.objects.create(id_cliente = id_cliente, nombre = nombre, apellido = apellido, telefono=telefono, fecha=fecha, edad=edad, genero=genero)
    return redirect("cliente") 

def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarCliente.html", {"cliente": cliente})


def editarCliente(request):
    id_cliente = request.POST['txt_idcliente']
    nombre = request.POST['txt_nombre']
    apellido = request.POST['txt_apellido']
    telefono = request.POST['txt_telefono']
    fecha = request.POST['fecha']
    edad = request.POST['edad']
    genero = request.POST['genero']

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.apellido = apellido
    cliente.telefono = telefono
    cliente.fecha = fecha
    cliente.edad = edad
    cliente.genero = genero
    cliente.save()
    return redirect("cliente") 


def borrarCliente(request,id_cliente):
    mat = Cliente.objects.get(id_cliente=id_cliente)
    mat.delete()
    
    return redirect("cliente")