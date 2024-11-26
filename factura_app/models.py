from django.db import models

# Create your models here.

class Factura(models.Model):
  id_factura = models.PositiveIntegerField()
  id_cliente = models.CharField(max_length=30, verbose_name="Id del cliente")
  id_producto = models.CharField(verbose_name="Id del producto", max_length=30)
  metodo_pago = models.CharField(verbose_name="Método de pago", max_length=30)
  total = models.PositiveIntegerField(verbose_name="Total")
  id_trabajador = models.CharField(verbose_name="Id del trabajador", max_length=30)
  fecha = models.DateField(verbose_name="fecha de realización", null=False, blank=False)
  
  
  class Meta:
      verbose_name = "Factura"
      verbose_name_plural = "Facturas"

  def __str__(self):
      return self.metodo_pago


