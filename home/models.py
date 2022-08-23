from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=10)
    descripcion = models.TextField()
    usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)
    valoracion = models.IntegerField()
    fecha = models.DateField()

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)
    valoracion = models.IntegerField()
    fecha = models.DateField()

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    nivel = models.IntegerField()
    password = models.CharField(max_length=16)
    fotodeperfil = models.ImageField()