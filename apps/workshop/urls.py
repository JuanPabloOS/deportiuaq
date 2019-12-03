from django.urls import path, re_path
from . import views

urlpatterns=[
    path('',views.talleres_view, name='talleres'),
    path('verTaller/<int:idTaller>/', views.verTaller_view , name='verTaller'),
    
    path('crearTaller/',views.createWorkshop, name='crearTaller'),
    path('eliminarTaller/', views.deleteWorkshop, name='eliminarTaller'),
    path('actualizarTaller/<int:idTaller>/',views.updateWorkshop,name='actualizarTaller'),
    path('registrarAlumnoT/',views.addMemberToWs,name='registrarAlumnoT'),
    path('eliminarAlumnoT/',views.deleteWsMember,name='eliminarAlumnoT'),
    path('callTheRollWs/<int:idTaller>/',views.callTheRollWs,name='callTheRollWs'),
    path('seleccionar-Taller-Pase-De-Lista/', views.seleccionarEquipo, name="seleccionarTallerPaseDeLista"),
    path('liberaciones/<int:idTaller>/', views.liberaciones_view,name='liberaciones'),
    path('absolverAlumnos/<int:idTaller>/',views.absolverAlumnos,name='absolverAlumnos'),
    path('showPdf/<int:idTaller>/',views.showPdf,name='showPdf'),
]