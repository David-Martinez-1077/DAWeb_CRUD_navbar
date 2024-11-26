from django.db import models

# Create your models here.

class Cliente(models.Model):
  genero_choices = (
    ("Mujer", "Mujer"),
    ("Hombre", "Hombre")
  )

  id_cliente = models.PositiveIntegerField();
  nombre = models.CharField(max_length=30, verbose_name="Nombre del cliente")
  apellido = models.CharField(max_length=30, verbose_name="Apellido del cliente")
  telefono = models.CharField(max_length=20, verbose_name="Telefono del cliente")
  fecha = models.DateField(verbose_name="Fecha", blank=False, null=False)
  edad = models.PositiveIntegerField()
  genero = models.CharField(verbose_name="Género", choices=genero_choices, default="Hombre", max_length=30)
  
  
  class Meta:
      verbose_name = "Cliente"
      verbose_name_plural = "Clientes"

  def __str__(self):
      return self.nombre


