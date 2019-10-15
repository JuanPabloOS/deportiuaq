from django import forms
from django.forms import ModelForm

from .models import Workshop
from .models import WsMember
from apps.core.models import User

class createWorkshopForm(ModelForm):
    """
    Formulario para crear un equipo representativo
    """
    #schedule=forms.CharField(label='Horario', widget=forms.TextInput(attrs={'type':'datetime-local'}))
    responsible=forms.ModelChoiceField(
        queryset=User.objects.filter(userType='DC')
    )
    class Meta:
        model= Workshop
        exclude=['totalAttendances','period','responsible']

        labels={
            'maxMembers':'Especifique un máximo de integrantes si es el caso'
        }

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

class updateWorkshopForm(forms.Form):
    id=forms.IntegerField(label="", widget=forms.NumberInput(attrs={'hidden':True}))
    responsible=forms.ModelChoiceField(label='Responsable',
        queryset=User.objects.filter(userType='DC')
    )
    schedule=forms.CharField(label='Horario', widget=forms.TextInput(attrs={'type':'text'}))
    maxMembers=forms.IntegerField(label='Especifique un máximo de integrantes si es el caso')
    # class Meta:
    #     model=Workshop
    #     fields=['workshop_id','responsible', 'schedule','maxMembers']

    #     labels={
    #         'maxMembers':'Especifique un máximo de integrantes si es el caso'
    #     }
    #