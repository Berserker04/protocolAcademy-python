from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('registrar', views.registrar, name='registrar'),
]