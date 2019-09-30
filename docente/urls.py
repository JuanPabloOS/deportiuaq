from django.urls import path
from . import views
urlpatterns=[
    path('addMemberToTeam/',views.addMemberToTeam,name='addMemberToTeam'),
    path('deleteTeamMember/',views.deleteTeamMember,name='deleteTeamMember'),
    path('addMemberToWs/',views.addMemberToWs,name='addMemberToWs'),
    path('deleteWsMember/',views.deleteWsMember,name='deleteWsMember'),
    path('updateWorkshop/',views.updateWorkshop,name='updateWorkshop'),
    path('updateTeam/',views.updateTeam,name='updateTeam'),
    path('callTheRoll/',views.callTheRoll,name='callTheRoll'),
    path('absolveWs/',views.absolveWs,name='absolveWs'),
    path('statisticsAttendance/',views.statisticsAttendance,name='statisticsAttendance'),
    path('statisticsMatches/',views.statisticsMatches,name='statisticsMatches'),
]