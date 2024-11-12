# urls de la aplicación project
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    # Gestion de Tareas
    
]