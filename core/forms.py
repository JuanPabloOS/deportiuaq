from django import forms
# from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from .models import User
# from .models import Team
# from .models import Workshop
# from .models import TeamMember
# from .models import WsMember
# from .models import Match
# from .models import Player

class LoginForm(forms.Form):
    username = forms.CharField(label='Clave/Usuario', widget=forms.TextInput())    
    password = forms.CharField(label='Contraseña',widget=forms.TextInput(attrs={'type':'password'}))

