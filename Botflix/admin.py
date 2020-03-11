from django.contrib import admin

# Register your models here.
from .models import Pregunta, Respuesta, TipoPregunta
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(TipoPregunta)
