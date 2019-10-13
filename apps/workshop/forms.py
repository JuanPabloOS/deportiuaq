from django import forms
from django.forms import ModelForm

from apps.core.models import Workshop
from apps.core.models import WsMember

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
    
class addMemberToWorkshopForm(ModelForm):
    class Meta:
        model=WsMember
        exclude=('totalAssists',)

class deleteMemberToWorkshopForm(ModelForm):
    class Meta:
        model=WsMember
        fields=['idWS', 'expediente']

class updateWorkshopForm(ModelForm):
    class Meta:
        model=Workshop
        fields=['responsible', 'schedule','maxMembers']

        labels={
            'maxMembers':'Especifique un máximo de integrantes si lo hay'
        }