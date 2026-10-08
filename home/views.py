from django.shortcuts import render

def inicio(request):
    categorias = [
        {
            "nombre": "Acción",
            "descripcion": "Persecuciones, explosiones y adrenalina pura.",
            "imagen": "images/accion.jpeg",
            "url": "categorias:accion",
        },
        {
            "nombre": "Comedia",
            "descripcion": "Las mejores películas para reír sin parar.",
            "imagen": "images/comedia.jpg",
            "url": "categorias:comedia",
        },
    ]
    return render(request, 'home/inicio.html', {"categorias": categorias})
