from django.urls import path
from . import views
urlpatterns=[
    path('addMemberToTeam/',views.addMemberToTeam,name='addMemberToTeam'),
]