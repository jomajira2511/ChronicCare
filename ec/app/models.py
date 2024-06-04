from django.db import models
from django.contrib.auth.models import User


    
CATEGORY_CHOICE = [
    ('AR', 'Articulos'),
    ('RE', 'Revistas'),
    ('VI', 'Videos')
    # otros valores posibles
]

class Product(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fuente = models.CharField(max_length=100)
    idioma = models.CharField(max_length=100)
    fecha_publi = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(choices=CATEGORY_CHOICE, max_length=3, default='AR')
    imagen_producto = models.ImageField(upload_to='product')

    def __str__(self):
        return self.titulo


class Customer(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE) #user
    nombre = models.CharField(max_length=200) #name
    fecha = models.CharField(max_length=50)
    bitacora = models.CharField(max_length=500)
    def _str_(self,):
        return self.nombre