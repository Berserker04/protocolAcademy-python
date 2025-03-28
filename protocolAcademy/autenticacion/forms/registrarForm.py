from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ..models import Alumno

class RegistrarForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombres', 'apellidos', 'documento', 'correo', 'contraseña']