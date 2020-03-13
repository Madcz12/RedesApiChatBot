from django.shortcuts import render
from rest_framework import generics
from StoreBot.Serializers import PreguntaSerializer, RespuestaSerializer
# Create your views here.

class PreguntaList(generics.ListCreateAPIView):
    queryset = StoreBot.objects.all()
    serializer_class = PreguntaSerializer

class RespuestaList(generics.ListCreateAPIView):
    queryset = StoreBot.objects.all()
    serializer_class = RespuestaSerializer