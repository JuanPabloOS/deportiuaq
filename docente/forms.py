from django import forms
from django.forms import ModelForm
from core.models import TeamMember
from core.models import Workshop

class addMemberToTeamForm(ModelForm):
    class Meta:
        model=TeamMember
        exclude=('totalAssists',)
