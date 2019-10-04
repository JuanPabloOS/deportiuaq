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
        fields=['idWs', 'expediente']

class deleteMemberToTeamForm(ModelForm):
    class Meta:
        model=TeamMember
        fields=['idTeam', 'expediente']

