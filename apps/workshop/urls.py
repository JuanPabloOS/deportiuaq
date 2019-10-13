from django.urls import path
from . import views

urlpatterns=[
    path('talleres/',views.talleres, name='talleres'),
    path('crearTaller/',views.createWorkshop, name='crearTaller'),
    path('eliminarTaller/', views.deleteWorkshop, name='eliminarTaller'),
    path('actualizarTaller/',views.updateWorkshop,name='actualizarTaller'),
    path('registrarAlumnoT/',views.addMemberToWs,name='agregarAlumnoT'),
    path('eliminarAlumnoT/',views.deleteWsMember,name='eliminarAlumnoT'),
    path('callTheRollWs/',views.callTheRollWs,name='callTheRollWs'),
    path('absolveWs/',views.absolveWs,name='absolveWs'),
]