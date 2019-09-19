from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(label='Clave/Usuario', widget=forms.TextInput())    
    password = forms.CharField(label='Contraseña',widget=forms.TextInput(attrs={'type':'password'}))
