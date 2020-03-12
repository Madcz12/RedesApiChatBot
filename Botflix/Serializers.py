from .models import Pregunta, Respuesta
from rest_framework import serializers



class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ('id', 'textoPregunta')

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = ('id', 'textoRespuesta')
