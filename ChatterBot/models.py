from django.db import models

# Create your models here.

class Pregunta(models.Model):
    textoPregunta1 = models.CharField(max_length=200)
    def __str__(self):
        return self.textoPregunta1

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    textoRespuesta = models.CharField(max_length=200)
    def __str__(self):
        return self.textoRespuesta


class TipoPregunta(models.Model):
    primeraPersona = models.CharField(max_length=200)
    terceraPersona = models.CharField(max_length=200)
