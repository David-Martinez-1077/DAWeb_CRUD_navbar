from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id_proveedor = models.PositiveIntegerField()
    nombre = models.CharField(max_length=30, verbose_name="Nombre del proveedor")
    direccion = models.CharField(verbose_name="Dirección del proveedor", max_length=50)
    tipo_prod = models.CharField(verbose_name="Tipo de producto", max_length=50)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad del producto")
    contacto= models.CharField(verbose_name="Contacto", max_length=15)
    fecha = models.DateField(verbose_name="fecha de entrega", null=False, blank=False)
    
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre


