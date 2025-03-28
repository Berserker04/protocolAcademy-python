from django.urls import path
from . import views

urlpatterns = [
    path('/mis_cursos', views.mis_cursos, name='mis_cursos'),
    path('/perfil', views.perfil, name='perfil'),
    path('registrar_inscripcion', views.registrar_inscripcion, name='registrar_inscripcion'),
    path('eliminar_inscripcion', views.eliminar_inscripcion, name='eliminar_inscripcion'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
]