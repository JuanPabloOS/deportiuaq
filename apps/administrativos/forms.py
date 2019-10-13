from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
#Modelos
from apps.core.models import User
from apps.core.models import Workshop


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