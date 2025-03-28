from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .inscripcionForm import InscripcionForm
from autenticacion.models import Instructor, Alumno
from servicios.models import Curso, Inscripcion

@login_required
# Create your views here.
def mis_cursos(request):
    alumno = request.session["alumno"]
    alumno_email = request.user.email
    user = Alumno.objects.get(correo=alumno_email)
    cursos = Curso.objects.all()
    instructores = Instructor.objects.all()
    inscripciones = Inscripcion.objects.filter(alumno=user).select_related('curso', 'instructor')
    return render(request, 'mis_cursos.html', {
        'alumno': alumno,
        'cursos': cursos,
        'instructores': instructores,
        'inscripciones': inscripciones
    })
def perfil(request):
    # alumno = request.session["alumno"]
    alumno_email = request.user.email
    alumno = Alumno.objects.get(correo=alumno_email)
    return render(request, 'perfil.html', {
        'alumno': alumno
    })

def registrar_inscripcion(request):
    if request.method == 'POST':
        curso_id = request.POST.get('curso')
        instructor_id = request.POST.get('instructor')

        curso = Curso.objects.get(id=curso_id)
        instructor = Instructor.objects.get(id=instructor_id)

        # Obtener el alumno correspondiente al usuario actual
        alumno = Alumno.objects.get(correo=request.user.email)

        Inscripcion.objects.create(
            alumno=alumno,
            instructor=instructor,
            curso=curso
        )

        return redirect('mis_cursos')
    else:
        form = InscripcionForm()

    return render(request, 'mis_cursos.html', {'form': form})

def eliminar_inscripcion(request):
    if request.method == 'POST':
        id = request.POST.get('id')

        Inscripcion.objects.get(id=id).delete()

        return redirect('mis_cursos')
    else:
        form = InscripcionForm()

    return render(request, 'mis_cursos.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')