from django.shortcuts import render, redirect, get_object_or_404

# Toca importar la clase
from .models import Tarea 


# Create your views here.


# Consultar listas tareas
def listar_tareas(request):
    tareas=Tarea.objects.all()
    # Va a renderizar una carpeta en donde tenemos html
    return render(request,'tareas/lista.html',{'tareas':tareas})


# Crear Tarea
def crear_tarea(request):
    # Ahora iniciamos con los metodos get y post
    # Post: Oculta la información
    # se verifica que todos los registros hallan sido enviados con post.

    if request.method == "POST":
        titulo=request.POST['titulo']
        descripcion=request.POST['descripcion']

        # Estos dos objetos usaran las dos creaciones de objetos de la clase tareas
        Tarea.objects.create(titulo=titulo, descripcion=descripcion)

        # Lo de arriba es una creación, la idea es que se pueda devolver por ende:
            # Importante importar el redirect
        return redirect('lista')

    # Ahora tenemos que poner todo esto en una vista. Por ende las va a mostrar en:
    return render(request,'tareas/crear.html')


# Ahora continuamos con la edición:
    # Además de la request va a recibir otro parametro. Esto es porque no puedo eliminar todo.
    # Necesitamos un identificador unico: En este caso id

        # El ORM nos ayudara con todo el apartado de la base de datos.
def editar_tarea(request, id):
        # Debemos controlar en donde si no llega el id correcto, que muestre un mensaje de que no existe.
        # Esto es lo que se conoce como 404
        # Esto es un metodo especial y toca importarlo. (Primera linea de este documento.
    tarea=get_object_or_404(Tarea,id=id)
    if request.method == "POST":
        tarea.titulo=request.POST['titulo']
        tarea.descripcion=request.POST['descripcion']
        tarea.estado = 'estado' in request.POST

        # Cuando tenga toda esta información del post, salve la información
        tarea.save()

        # Que se rediriga a lista, donde la información va a estar.
        return redirect('lista')

    # Como tiene un HTML asociado:
    return render(request, 'tareas/editar.html', {'tarea':tarea})


# Ahora con eliminar tarea:

def eliminar_tarea(request, id):
    tarea=get_object_or_404(Tarea,id=id)
    tarea.delete()
    return redirect('lista')

# Esto es nuestra CRUD de tareas.

# Podemos agregar un filtro en donde solo nos muestre una consulta en donde solo esten las tareas completadas.




# Filtro de tareas completadas

def completadas(request):
    tareas=Tarea.objects.filter(estado = True)
    return render(request, 'tareas/lista.html', {'tareas':tareas})


