from django.urls import path
from . import views

urlpatterns=[
    path('', views.equipos_view, name='equipos'),
    path('crearEquipo/',views.createTeam,name='crearEquipo'),
    path('verEquipo/<int:idTeam>/', views.verEquipo_view, name='verEquipo'),
    path('verAlumnosEquipo/<int:idTeam>/', views.verAlumnosEquipo_view, name="verAlumnosEquipo"),
    path('eliminarEquipo/', views.deleteTeam, name='eliminarEquipo'), 
    path('actualizarEquipo/<int:idTeam>/',views.updateTeam,name='actualizarEquipo'),
    path('seleccionar-Equipo-Pase-De-Lista/', views.seleccionarEquipo, name="seleccionarEquipoPaseDeLista"),
    path('callTheRollTeam/<int:idTeam>/',views.callTheRollTeam,name='callTheRollTeam'),
    path('estadisticosPartidos/',views.statisticsMatches,name='estadisticosPartidos'),
    path('registrarAlumnoE/',views.addMemberToTeam,name='registrarAlumnoE'),
    path('eliminarAlumnoE/',views.deleteTeamMember,name='eliminarAlumnoE'),
    path('estadisticosAsistencia/',views.statisticsAttendance,name='estadisticosAsistencia'),
    path('registrarPartido/', views.registerMatch_view, name='registrarPartido'),
    path('getMiembrosTeam/<int:idTeam>/', views.getMiembrosTeam, name='getMiembrosTeam')
    
]