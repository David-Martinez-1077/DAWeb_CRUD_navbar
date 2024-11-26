from django.db import models

# Create your models here.

class Trabajador(models.Model):
    id_trabajador = models.PositiveIntegerField()
    nombre = models.CharField(max_length=30, verbose_name="Nombre del trabajador")
    apellido = models.CharField(max_length=30, verbose_name="apellido del trabajador")
    telefono = models.CharField(max_length=15 ,verbose_name="Teléfono del trabajador")
    gmail = models.EmailField(verbose_name="Email del trabajador", max_length=50)
    curp = models.CharField(verbose_name="Curp del trabajador", max_length=40)
    rfc = models.CharField(verbose_name="RFC del trabajador", max_length=30)
    
    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

    def __str__(self):
        return self.nombre