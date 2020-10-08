from django.shortcuts import render
from .models import Usuario, Clase, ClaseAlumno


def index(request):
    
    # Función vista para la página inicio del sitio.
    
    # Genera contadores de algunos de los objetos principales

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
    )


# Create your views here.

