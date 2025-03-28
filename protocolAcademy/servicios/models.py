from django.db import models
from autenticacion.models import Alumno, Instructor

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    descripcion = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    duracion = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.descripcion}"


class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.alumno} inscrito en {self.curso} con {self.instructor}"