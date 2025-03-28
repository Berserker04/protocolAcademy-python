from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
class Instructor(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"