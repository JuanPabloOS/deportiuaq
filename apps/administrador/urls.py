from django.urls import path
from . import views

urlpatterns=[
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('registrarDocente/', views.createTeacher,name='registrarDocente'),
    path('registrarBecario/', views.createBecario, name='registrarBecario'),
    path('registrarAdmin/',views.createAdmin, name='registrarAdmin'),
    path('crearTaller/',views.createWorkshop, name='crearTaller'),
    path('crearEquipo/',views.createTeam,name='crearEquipo'),
    path('eliminarAdmin/',views.deleteAdmin, name='eliminarAdmin'),
    path('eliminarDocente/',views.deleteTeacher, name='eliminarDocente'),
    path('eliminarBecario/',views.deleteBecario, name='eliminarBecario'),
    path('eliminarTaller/', views.deleteWorkshop, name='eliminarTaller'),
    path('eliminarEquipo/', views.deleteTeam, name='eliminarEquipo'), 
]