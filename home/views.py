from django.shortcuts import render

def inicio(request):
    categorias = [
        {
            "nombre": "Acción",
            "descripcion": "Persecuciones, explosiones y adrenalina pura.",
            "imagen": "images/accion.jpeg",
            "url": "accion",
        },
        {
            "nombre": "Comedia",
            "descripcion": "Las mejores películas para reír sin parar.",
            "imagen": "images/comedia.jpg",
            "url": "comedia",
        },
    ]
    return render(request, 'home/inicio.html', {"categorias": categorias})
