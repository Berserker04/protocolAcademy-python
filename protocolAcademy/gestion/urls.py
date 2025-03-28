from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestion, name='gestion'),
    path('registrar_inscripcion', views.registrar_inscripcion, name='registrar_inscripcion'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
]