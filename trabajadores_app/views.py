from django.shortcuts import render, redirect
from .models import Trabajador
# Create your views here.


def vista_indexTrabajador(request):
    trabajador = Trabajador.objects.all()
    return render(request, "index_trabajador.html", {"trabajador": trabajador})


def registrarTrabajador(request):
    id_trabajador = request.POST['txt_idtrabajador']
    nombre = request.POST['txt_nombre']
    apellido = request.POST['txt_apellido']
    telefono = request.POST['txt_telefono']
    gmail = request.POST['txt_gmail']
    curp = request.POST['txt_curp']
    rfc = request.POST['txt_rfc']

    guardarmtrabajador = Trabajador.objects.create(id_trabajador = id_trabajador, nombre = nombre, apellido = apellido, telefono=telefono, gmail=gmail, curp=curp, rfc=rfc)
    return redirect("trabajador") 

def seleccionarTrabajador(request, id_trabajador):
    trabajador = Trabajador.objects.get(id_trabajador=id_trabajador)
    return render(request, "editartrabajador.html", {"trabajador": trabajador})


def editarTrabajador(request):
    id_trabajador = request.POST['txt_idtrabajador']
    nombre = request.POST['txt_nombre']
    apellido = request.POST['txt_apellido']
    telefono = request.POST['txt_telefono']
    gmail = request.POST['txt_gmail']
    curp = request.POST['txt_curp']
    rfc = request.POST['txt_rfc']

    trabajador = Trabajador.objects.get(id_trabajador=id_trabajador)
    trabajador.nombre = nombre
    trabajador.apellido = apellido
    trabajador.telefono = telefono
    trabajador.gmail = gmail
    trabajador.curp = curp
    trabajador.rfc = rfc
    trabajador.save()
    return redirect("trabajador") 


def borrarTrabajador(request,id_trabajador):
    trab = Trabajador.objects.get(id_trabajador=id_trabajador)
    trab.delete()
    
    return redirect("trabajador")