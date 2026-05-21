from django.db import models

# Create your models here.

# Se esta importando una libreria para hacer esa transición con los modelos
class Tarea(models.Model):

    # Esto es lo que representaria una tabla apra la base de datos.

    # Cuando alguien lo llame, haga la construcción de la variable/campos
    titulo=models.CharField(max_length=200)
    descripcion=models.TextField(blank=True)
    estado=models.BooleanField(default=False)

    # django tiene demasiados tipos de datos, a medida de que pase el tiempo iremos viendo.

    # Esto hace que se guarde la fecha y hora en la que se creo la tarea
    fecha=models.DateTimeField(auto_now_add=True) 
    
    # Vamos con los metodos.
    def __str__(self):
        # Cada tarea es un objeto.
        return self.titulo