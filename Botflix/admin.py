from django.contrib import admin

# Register your models here.
from .models import Pregunta, Respuesta, Pelicula, Miembro
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Pelicula)
admin.site.register(Miembro)
