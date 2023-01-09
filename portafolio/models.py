from django.db import models

# Create your models here.
class Mensaje(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return '/'

    