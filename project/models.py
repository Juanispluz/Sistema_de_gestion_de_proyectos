from django.db import models

# Create your models here.

class Usuarios(models.Model):
    correo = models.EmailField(max_length=254, primary_key=True)
    nombre = models.CharField(max_length=100)
    password = models.CharField(max_length=254)
    ROLES  = (
        ('A', 'Administrador'),
        ('L', 'Lider'),
        ('D', 'Desarrollador'),
    )
    rol = models.CharField(max_length=1, choices=ROLES)

class Tareas(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=False, blank=False)
    fecha_limite = models.DateField(help_text="Formato dd-mm-YYYY")
    PRIORI = (
        ('A', 'Alta'),
        ('M', 'Media'),
        ('B', 'Baja')
    )
    prioridad = models.CharField(max_length=1, choices=PRIORI)
    EST = (
        (1, 'Terminada'),
        (2, 'En proceso'),
        (3, 'Pendiente'),
        (4, 'Cancelada'),
    )
    estado = models.IntegerField(choices=EST)
    observaciones = models.TextField(null = False, blank=False)

class Equipos(models.Model):
    nombre_equipo = models.CharField(max_length=100, primary_key=True)
    lider_usuario_id = models.ForeignKey('Usuarios', on_delete=models.CASCADE)

    def __str__(self):
        return f"ID de líder: {self.lider_usuario_id}"

class Equipos_desarrollo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_equipo_id = models.ForeignKey('Equipos', on_delete=models.CASCADE)
    desarrollador_usuario_id = models.ForeignKey('Usuarios', on_delete=models.CASCADE)

    def __str__(self):
        return f"ID del desarrollador: {self.desarrollador_usuario_id} en el ID del equipo: {self.nombre_equipo_id}"

class Tareas_Equipos(models.Model):
    id = models.AutoField(primary_key=True)
    tarea_id = models.ForeignKey('Tareas', on_delete=models.CASCADE)
    equipos_desarrollo_id = models.ForeignKey('Equipos_desarrollo', on_delete=models.CASCADE)

    def __str__(self):
        return f"ID de la tarea: {self.tarea_id}\n del ID del equipo: {self.equipos_desarrollo_id}"
