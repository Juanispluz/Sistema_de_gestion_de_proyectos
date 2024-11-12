from django.contrib import admin
from .models import *

# Register your models here.

class Usuarios_Admin(admin.ModelAdmin):
    list_display = ["correo", "nombre", "rol"]

class Tareas_Admin(admin.ModelAdmin):
    list_display = ["id", "titulo", "descripcion", "fecha_limite", "prioridad", "estado", "observaciones"]

class Equipos_Admin(admin.ModelAdmin):
    list_display = ["nombre_equipo", "lider_usuario_id"]

class Equipos_desarrollo_Admin(admin.ModelAdmin):
    list_display = ["id", "nombre_equipo_id", "desarrollador_usuario_id"]

class Tareas_Equipos_Admin(admin.ModelAdmin):
    list_display = ["id", "tarea_id", "equipos_desarrollo_id"]

admin.site.register(Usuarios, Usuarios_Admin)
admin.site.register(Tareas, Tareas_Admin)
admin.site.register(Equipos, Equipos_Admin)
admin.site.register(Equipos_desarrollo, Equipos_desarrollo_Admin)
admin.site.register(Tareas_Equipos, Tareas_Equipos_Admin)