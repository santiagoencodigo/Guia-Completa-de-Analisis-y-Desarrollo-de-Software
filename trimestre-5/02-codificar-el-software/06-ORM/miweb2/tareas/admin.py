from django.contrib import admin

# Register your models here.
from .models import Tarea

# Esto es la preparación para cuando se use la interfaz administrativa
# hay se encuentre la tarea y poder revisar que tareas tiene.
admin.site.register(Tarea)
