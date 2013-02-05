from django.db import models

SABORES = (('fr','Fresa'),('nj','Naranja'),('choc','Chocolate'),('li','Limon'),('vai','Vainilla'),)

class Helado(models.Model):
    nombre = models.CharField(max_length=200)
    sabor = models.CharField(max_length=200,choices=SABORES)
    imagen = models.ImageField(upload_to='helados_images',blank=False,null=False)
    descripcion = models.TextField(max_length=300,blank=True)
    def __str__(self):
        return self.nombre
