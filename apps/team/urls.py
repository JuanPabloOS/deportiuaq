from django.urls import path
from . import views

urlpatterns=[
    path('crearEquipo/',views.createTeam,name='crearEquipo'),
    path('eliminarEquipo/', views.deleteTeam, name='eliminarEquipo'), 
    path('actualizarEquipo/',views.updateTeam,name='actualizarEquipo'),
    path('callTheRollTeam/<int:idTeam>/',views.callTheRollTeam,name='callTheRollTeam'),
    path('estadisticosPartidos/',views.statisticsMatches,name='estadisticosPartidos'),
    path('registrarAlumnoE/',views.addMemberToTeam,name='registrarAlumnoE'),
    path('eliminarAlumnoE/',views.deleteTeamMember,name='eliminarAlumnoE'),
    path('estadisticosAsistencia/',views.statisticsAttendance,name='estadisticosAsistencia'),
]