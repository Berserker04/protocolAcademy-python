from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms.registrarForm import RegistrarForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['alumno'] = f"{user.first_name} {user.last_name}"
            return redirect('gestion')  # Cambia 'gestion' por tu vista protegida
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    return render(request, 'login.html')

def registrar(request):
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            alumno = form.save()
            nombres = alumno.nombres
            apellidos = alumno.apellidos
            correo = alumno.correo
            contraseña = alumno.contraseña

            # Creamos el usuario usando create_user
            usuario = User.objects.create_user(
                username=correo,  # username obligatorio (puede ser igual al correo)
                email=correo,
                password=contraseña,
                first_name=nombres,
                last_name=apellidos
            )
            user = authenticate(request, username=alumno.correo, password=alumno.contraseña)
            if user:
                login(request, user)
                return redirect('gestion')
            # return redirect('gestion', {'nombres': form.nombres, 'apellidos': form.apellidos})
    else:
        form = RegistrarForm()

    # lista_alumnos = Alumno.objects.all()
    # return render(request, 'registrar.html', {'form': form, 'alumnos': lista_alumnos})
    return render(request, 'registrar.html', {'form': form})
