from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .inscripcionForm import InscripcionForm

@login_required
# Create your views here.
def gestion(request):
    alumno = request.session["alumno"]  # lo eliminamos después de usar
    return render(request, 'gestion.html', {'alumno': alumno})

def registrar_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion')
    else:
        form = InscripcionForm()

    return render(request, 'gestion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')