from django.conf.urls import url
from ChatterBot.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from StoreBot import views

urlpatterns = [
    url(r'^bot/','bot'),
    url(r'^bot/$', views.PreguntaList.as_view()),
    url(r'^bot/$', views.RespuestaList.as_view()),
    #TraerListPalabras de la clase bot
]