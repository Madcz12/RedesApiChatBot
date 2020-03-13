from django.db import models

# Create your models here.
class Pregunta(models.Model):
    textoPregunta = models.CharField(max_length=200)
    def __str__(self):
        return self.textoPregunta

class Respuesta(models.Model):
    preg = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    textoRespuesta = models.CharField(max_length=200)
    def __str__(self):
        return self.textoRespuesta

class Pelicula(models.Model):
    nombrePelicula = models.CharField(max_length=200)
    detalle= models.CharField(max_length=200)
    genero = models.CharField(max_length=200)

    def __str__(self):
        return "Pelicula: {} genero: $ {}".format(self.nombrePelicula, self.genero)
