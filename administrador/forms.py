from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
#Modelos
from core.models import User
from core.models import Team
from core.models import Workshop
from core.models import TeamMember
from core.models import WsMember
from core.models import Match
from core.models import Player

class resetPasswordForm(forms.Form):
    """
    Resetear la contraseña de cualquier usuario
    """
    username = forms.CharField(label='Clave/Nombre de usuario', widget=forms.TextInput(attrs={'type':'text','placeholder':''}))
    passwordAdministrador = forms.CharField(label='Contraseña administrador', widget=forms.TextInput(attrs={'type':'password','placeholder':''}))
    

class createUserForm(ModelForm):
    """
    Registrar becario, teacher, administrador
    """
    class Meta:
        model= User
        fields=['username','first_name','last_name','email']

class deleteSomethingForm(forms.Form):
    username=forms.CharField()


class createWorkshopForm(ModelForm):
    """
    Formulario para crear un equipo representativo
    """
    schedule=forms.CharField(label='Horario', widget=forms.TextInput(attrs={'type':'datetime-local'}))
    class Meta:
        model= Workshop
        exclude=['schedule','totalAttendances']
    

class updateWorkshopForm(ModelForm):
    """
    """
    pass

class deleteWorkshopForm(forms.Form):
    """
    """
    pass

class createTeamForm(ModelForm):
    """
    Crear un equipo representativo
    """
    schedule=forms.CharField(label='Horario', widget=forms.TextInput(attrs={'type':'datetime-local'}))
    class Meta:
        model=Team
        exclude=('schedule','totalAttendances')

class updateTeamForm(ModelForm):
    """
    """
    pass

class deleteTeamForm(forms.Form):
    """
    """
    pass

class addMemberToTeamForm(ModelForm):
    """
    """
    pass

class deleteTeamMemberForm(forms.Form):
    """
    """
    pass

class addMemberToWsForm(ModelForm):
    """
    """
    pass

class deleteWsMemberForm(forms.Form):
    """
    """
    pass