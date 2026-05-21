from django.urls import path

# Importaremos lo que estaba en el view

    # Lo necesitamos porque aqui estan los metodos. Me permite llamar a las funciones.
from .import views

urlpatterns = [
    # Aqui viene la lista
        # El nombre de la ruta, la función que se va a ejecutar y el nombre de la ruta.
    path('', views.listar_tareas, name='lista'),
    path('crear/', views.crear_tarea, name='crear'),


    # Las dos rutas de arriba no necesitan ID, pero la de abajo si. 
    # Para decir que lo que va a pasar en esa url es un dato entero que es el id


    # Cuando hacemos trasnferencias de un lugar a otro por medio de una URL, necesitamos un ID.
        # Dice qué dato especifico se va a hacer con la edición.
    path('editar/<int:id>/', views.editar_tarea, name='editar'),
    
    # Lo mismo sucede con eliminación
    path('eliminar/<int:id>/', views.eliminar_tarea, name='eliminar'),
    
    path('completadas/', views.completadas, name='completadas'),
]