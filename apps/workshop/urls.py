from django.urls import path, re_path
from . import views

urlpatterns=[
    path('',views.talleres_view, name='talleres'),
    path('verTaller/<int:idTaller>/', views.verTaller_view , name='verTaller'),
    path('verAlumnosTaller/<int:idTaller>/', views.verAlumnosTaller_view,name='verAlumnosTaller'),
    path('crearTaller/',views.createWorkshop, name='crearTaller'),
    path('eliminarTaller/', views.deleteWorkshop, name='eliminarTaller'),
    path('actualizarTaller/<int:idTaller>/',views.updateWorkshop,name='actualizarTaller'),
    path('registrarAlumnoT/',views.addMemberToWs,name='registrarAlumnoT'),
    path('eliminarAlumnoT/',views.deleteWsMember,name='eliminarAlumnoT'),
    path('callTheRollWs/',views.callTheRollWs,name='callTheRollWs'),
    path('absolveWs/',views.absolveWs,name='absolveWs'),
]