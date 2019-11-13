from django import forms
from django.forms import ModelForm
from .models import TeamMember
from .models import Team
from .models import Match
from .models import Player
from apps.core.models import User


    
class addMemberToTeamForm(ModelForm):
    class Meta:
        model=TeamMember
        exclude=('totalAttendances',)

class deleteMemberToTeamForm(ModelForm):
    class Meta:
        model=TeamMember
        fields=['idTeam', 'expediente']

class createTeamForm(ModelForm):
    """
    Crear un equipo representativo
    """
    schedule=forms.CharField(label='Horario', widget=forms.TextInput(attrs={'type':'datetime-local'}))
    class Meta:
        model=Team
        exclude=('schedule','totalAttendances','period')

class updateTeamForm(forms.Form):
    """
    """
    id=forms.IntegerField(label="", widget=forms.NumberInput(attrs={'hidden':True}))
    responsible=forms.ModelChoiceField(label='Responsable',
        queryset=User.objects.filter(userType='DC')
    )
    schedule=forms.CharField(label='Horario', widget=forms.TextInput(attrs={'type':'text'}))

class deleteTeamForm(forms.Form):
    """
    """
    team_id= forms.ModelChoiceField(queryset=Team.objects.all(),label="Equipo representativo")

class addMemberToTeamForm(ModelForm):
    """
    """
    class Meta:
        model=TeamMember
        exclude=('totalAttendances',)
        labels={
            'idTeam':''
        }
        widgets={
            'idTeams':forms.NumberInput(attrs={'hidden':True})
        }

class deleteTeamMemberForm(forms.Form):
    """
    """
    pass

class registerMatchForm(ModelForm):
    class Meta:
        model = Match
        exclude=('winned', 'period')
# class callTheRollWsForm(ModelForm):
#     class Meta:
#         model=Team
#         fields=['idUser', 'attended']

# class callTheRollTeamForm(ModelForm):
#     class Meta:
#         model=TeamMember
#         fields=['idUser', 'attended']

# class absolveWsForm(ModelForm):
#     class Meta:
#         model=WsMember
#         fields=['idUser','absolved']

#Pendiente:
#statisticsAttendance
#statisticsMatches