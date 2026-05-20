from django.shortcuts import render

# Create your views here.

# Cuando llamen a la función home.
    
def home(request):
    # Ya no usaremos http request sino render:
        # Todavia no hemos creado el archivo HTML, pero aqui lo ponemos.
    return render(request, 'inicio/home.html')

# Copiar y pegar para los demas

def about(request):
    return render(request, 'inicio/about.html')

def blog(request):
    return render(request, 'inicio/blog.html')

def contacto(request):
    return render(request, 'inicio/contacto.html')