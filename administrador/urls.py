from django.urls import path
from . import views

urlpatterns=[
    path('registrarDocente', views.createTeacher,'registrarDocente'),
]