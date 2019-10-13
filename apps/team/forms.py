from django import forms
from django.forms import ModelForm
from apps.core.models import TeamMember
from apps.core.models import Team
from apps.core.models import Match
from apps.core.models import Player
class addMemberToTeamForm(ModelForm):
    class Meta:
        model=TeamMember
        exclude=('totalAssists',)



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

class updateTeamForm(ModelForm):
    """
    """
    pass

class deleteTeamForm(forms.Form):
    """
    """
    team_id= forms.ModelChoiceField(queryset=Team.objects.all(),label="Equipo representativo")

class addMemberToTeamForm(ModelForm):
    """
    """
    pass

class deleteTeamMemberForm(forms.Form):
    """
    """
    pass

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