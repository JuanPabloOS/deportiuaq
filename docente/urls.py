from django.urls import path
from . import views
urlpatterns=[
    path('registrarAlumnoE/',views.addMemberToTeam,name='registrarAlumnoE'),
    path('eliminarAlumnoE/',views.deleteTeamMember,name='eliminarAlumnoE'),
    path('registrarAlumnoT/',views.addMemberToWs,name='agregarAlumnoT'),
    path('eliminarAlumnoT/',views.deleteWsMember,name='eliminarAlumnoT'),
    path('actualizarTaller/',views.updateWorkshop,name='actualizarTaller'),
    path('actualizarEquipo/',views.updateTeam,name='actualizarEquipo'),
    path('callTheRoll/',views.callTheRoll,name='callTheRoll'),
    path('absolveWs/',views.absolveWs,name='absolveWs'),
    path('estadisticosAsistencia/',views.statisticsAttendance,name='estadisticosAsistencia'),
    path('estadisticosPartidos/',views.statisticsMatches,name='estadisticosestadisticosAsistencia'),
]