from django.db import models

# Create your models here.

class Inventario(models.Model):
  id_inventario = models.PositiveIntegerField()
  producto = models.CharField(max_length=30, verbose_name="Nombre del producto")
  tipo = models.CharField(verbose_name="Tipo del producto", max_length=40)
  cantidad = models.PositiveIntegerField(verbose_name="Cantidad del producto")
  categoria = models.CharField(verbose_name="Categoría del producto", max_length=300)
  id_producto = models.CharField(verbose_name="id del producto", max_length=30)
  disponible = models.CharField(verbose_name="Disponible", max_length=30)
  
  
  class Meta:
      verbose_name = "Inventario"
      verbose_name_plural = "Inventarios"

  def __str__(self):
      return self.producto


