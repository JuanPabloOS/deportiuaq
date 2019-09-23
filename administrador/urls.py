from django.urls import path
from . import views

urlpatterns=[
    path('registrarDocente/', views.createTeacher,name='registrarDocente'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
]