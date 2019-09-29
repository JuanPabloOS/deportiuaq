from django import forms
from django.contrib.auth.hashers import check_password
from django.utils import timezone
# from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from .models import User

# from .models import Team
# from .models import Workshop
# from .models import TeamMember
# from .models import WsMember
# from .models import Match
# from .models import Player

class LoginForm(forms.Form):
    username = forms.CharField(label='Clave/Usuario', widget=forms.TextInput())    
    password = forms.CharField(label='Contraseña',widget=forms.TextInput(attrs={'type':'password'}))



class ConfirmPasswordForm(forms.ModelForm):
    """
    Confirmar contraseña para continuar
    """
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('confirm_password', )

    def clean(self):
        cleaned_data = super(ConfirmPasswordForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        if not check_password(confirm_password, self.instance.password):
            print("========================")
            print("el error")
            self.add_error('confirm_password', 'Password does not match.')
        print("================================")
        print("succes")

    def save(self, commit=True):
        user = super(ConfirmPasswordForm, self).save(commit)
        user.last_login = timezone.now()
        if commit:
            user.save()
        return user


