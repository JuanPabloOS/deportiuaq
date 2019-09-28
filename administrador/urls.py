from django.urls import path
from . import views

urlpatterns=[
    path('registrarDocente/', views.createTeacher,name='registrarDocente'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('registrarBecario/', views.createBecario, name='registrarBecario'),
    path('registrarAdmin/',views.createAdmin, name='registrarAdmin'),
    path('eliminarAdmin/',views.deleteAdmin, name='eliminarAdmin'),
    path('crearTaller/',views.createWorkshop, name='crearTaller'),
    path('crearEquipo/',views.createTeam,name='crearEquipo'),
]