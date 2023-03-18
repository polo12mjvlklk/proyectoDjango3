from django.db import models

# Create your models here.
class categoria(models.Model):
    descripCategoria = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.descripCategoria

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categoria de producto'

class producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=300, null=True)
    precioUnitario = models.DecimalField(max_digits=8, decimal_places=2)
    unidad = models.CharField(max_length=10, null=False)
    existencia = models.IntegerField(null=True)
    imgGrande = models.ImageField(upload_to='productos', null=True)
    imgpeque = models.ImageField(upload_to='iconos', null=True)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre
