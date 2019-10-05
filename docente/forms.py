from django import forms
from django.forms import ModelForm
from core.models import TeamMember
from core.models import Workshop
from core.models import WsMember
from core.models import Team

class addMemberToTeamForm(ModelForm):
    class Meta:
        model=TeamMember
        exclude=('totalAssists',)

class addMemberToWorkshopForm(ModelForm):
    class Meta:
        model=WsMember
        exclude=('totalAssists',)

class deleteMemberToWorkshopForm(ModelForm):
    class Meta:
        model=WsMember
        fields=['idWS', 'expediente']

class deleteMemberToTeamForm(ModelForm):
    class Meta:
        model=TeamMember
        fields=['idTeam', 'expediente']

class updateWorkshopForm(ModelForm):
    class Meta:
        model=Workshop
        fields=['responsible', 'schedule']

class callTheRollWsForm(ModelForm):
    class Meta:
        model=Team
        fields=['idUser', 'attended']

class callTheRollTeamForm(ModelForm):
    class Meta:
        model=Team
        fields=['idUser', 'attended']

class absolveWsForm(ModelForm):
    class Meta:
        model=Team
        fields=['idUser','absolved']

#Pendiente:
#statisticsAttendance
#statisticsMatches