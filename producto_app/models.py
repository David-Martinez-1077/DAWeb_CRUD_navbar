from django.db import models

# Create your models here.

class Producto(models.Model):
  categoria_choices = (
    ("Traje de baño", "Traje de baño"),
    ("Accesorios", "Accesorios"),
    ("Lenceria","Lenceria")
  )

  id_producto = models.PositiveIntegerField()
  nombre_producto = models.CharField(max_length=30, verbose_name="Nombre del producto")
  precio = models.PositiveIntegerField(verbose_name="Precio del producto")
  stock = models.PositiveIntegerField(verbose_name="Stock del producto")
  categoria = models.CharField(verbose_name="Categoría del producto", max_length=300, choices=categoria_choices, default="Traje de baño")
  descripcion = models.TextField(verbose_name="Descripción del producto")
  fecha = models.DateField(verbose_name="fecha de publicación", null=False, blank=False)
  
  
  class Meta:
      verbose_name = "Producto"
      verbose_name_plural = "Productos"

  def __str__(self):
      return self.nombre_producto


