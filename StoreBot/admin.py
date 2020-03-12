from django.contrib import admin

# Register your models here.
from .models import Pregunta, Respuesta, Producto, Miembro
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Producto)
admin.site.register(Miembro)

