from django.shortcuts import render
def accion(request):
    peliculas = [
        {"nombre": "Mad Max: Fury Road", "anio": 2015, "imagen": "images/accion/1.jpg"},
        {"nombre": "John Wick", "anio": 2014, "imagen": "images/accion/2.jpg"},
        {"nombre": "Die Hard", "anio": 1988, "imagen": "images/accion/3.jpg"},
        {"nombre": "The Dark Knight", "anio": 2008, "imagen": "images/accion/4.jpg"},
        {"nombre": "Gladiator", "anio": 2000, "imagen": "images/accion/5.jpg"},
        {"nombre": "Mission: Impossible - Fallout", "anio": 2018, "imagen": "images/accion/6.jpg"},
        {"nombre": "Top Gun: Maverick", "anio": 2022, "imagen": "images/accion/7.jpg"},
        {"nombre": "The Matrix", "anio": 1999, "imagen": "images/accion/8.jpg"},
        {"nombre": "Terminator 2", "anio": 1991, "imagen": "images/accion/9.jpg"},
        {"nombre": "Casino Royale", "anio": 2006, "imagen": "images/accion/10.jpg"},
    ]
    return render(request, 'categorias/accion.html', {"peliculas": peliculas})


def comedia(request):
    peliculas = [
        {"nombre": "Superbad", "anio": 2007, "imagen": "images/comedia/1.jpg"},
        {"nombre": "The Hangover", "anio": 2009, "imagen": "images/comedia/2.jpg"},
        {"nombre": "Step Brothers", "anio": 2008, "imagen": "images/comedia/3.jpg"},
        {"nombre": "Anchorman", "anio": 2004, "imagen": "images/comedia/4.jpg"},
        {"nombre": "Mean Girls", "anio": 2004, "imagen": "images/comedia/5.jpg"},
        {"nombre": "Bridesmaids", "anio": 2011, "imagen": "images/comedia/6.jpg"},
        {"nombre": "Dumb and Dumber", "anio": 1994, "imagen": "images/comedia/7.jpg"},
        {"nombre": "Ghostbusters", "anio": 1984, "imagen": "images/comedia/8.jpg"},
        {"nombre": "Home Alone", "anio": 1990, "imagen": "images/comedia/9.jpg"},
        {"nombre": "Napoleon Dynamite", "anio": 2004, "imagen": "images/comedia/10.jpg"},
    ]
    return render(request, 'categorias/comedia.html', {"peliculas": peliculas})