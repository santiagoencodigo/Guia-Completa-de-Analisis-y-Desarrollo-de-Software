# Tenemos que importar path para poder usarlo.
from django.urls import path

# Importaremos todo lo que tengas las views/funciones
from . import views


urlpatterns=[
    # Las URL que esto va a tener.  
        # Estamos viendo el "futuro" 
        # Esto ira a path, ira a la views a la función index.
    path('', views.index, name='index'),
]