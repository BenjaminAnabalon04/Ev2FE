from django.urls import path
from . import views


app_name="categorias"

urlpatterns = [
    path('comedia/', views.comedia, name='comedia'),
    path('accion/', views.accion, name='accion'),
]