from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
#Modelos
from apps.core.models import User
from apps.core.models import Team
from apps.core.models import Workshop
from apps.core.models import TeamMember
from apps.core.models import WsMember
from apps.core.models import Match
from apps.core.models import Player

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
        labels = {
            'username':'Expediente/Folio',
            'first_name':'Nombre',
            'last_name':'Apellidos',            
            'email':'Correo electrónico',            
        }
        widgets = {
            'username':forms.TextInput(attrs ={'type':'text','min':'100000'}),                          
            'first_name': forms.TextInput(attrs = {'class':'validate'}),
            'last_name': forms.TextInput(attrs = {'class':'validate'}),
            'email': forms.TextInput(attrs = {'class':'validate'}),
        }
        help_texts = {
            'username': None,
        }

class deleteUserForm(forms.Form):
    """
    Pide una clave la cual puede s
    """
    username=forms.CharField()


class createWorkshopForm(ModelForm):
    """
    Formulario para crear un equipo representativo
    """
    schedule=forms.CharField(label='Horario', widget=forms.TextInput(attrs={'type':'datetime-local'}))
    class Meta:
        model= Workshop
        exclude=['schedule','totalAttendances','period']

class deleteWorkshopForm(forms.Form):
    """
    Formulario para eliminar un equipo representativo
    """
    workshop_id= forms.ModelChoiceField(queryset=Workshop.objects.all(),label="Taller deportivo")
    


class updateWorkshopForm(ModelForm):
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

class addMemberToWsForm(ModelForm):
    """
    """
    pass

class deleteWsMemberForm(forms.Form):
    """
    """
    pass