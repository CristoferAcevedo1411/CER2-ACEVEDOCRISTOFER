from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class LugarPatrimonial(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    anio_construccion = models.PositiveIntegerField(null=True, blank=True)
    imagen = models.URLField(max_length=500)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='lugares'
    )

    class Meta:
        verbose_name = 'lugar patrimonial'
        verbose_name_plural = 'lugares patrimoniales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre