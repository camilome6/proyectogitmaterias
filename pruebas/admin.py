from django.contrib import admin

# Register your models here.
from pruebas.models import Estudiante, Materia

admin.site.register(Estudiante)
admin.site.register(Materia)

