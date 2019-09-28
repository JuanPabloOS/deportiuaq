from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse

# import forms
from .forms import addMemberToTeamForm

# Create your views here.
def addMemberToTeam(request):
    """
    Agregar miembro al equipo
    """
    if request.method == 'POST':
        form = addMemberToTeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registro completado')
            return redirect('addMemberToTeam')
        else:
            messages.error(request,'Error: revisa que los datos sean correctos')
            return render(request,'exclusiveTeacher/addMemberToTeam.html',{'form':form})
    else:
        form = addMemberToTeamForm()
        return render(request,'exclusiveTeacher/addMemberToTeam.html',{'form':form})

def deleteTeamMember(request):
    """
    Eliminar miembro del equipo
    """
    pass

def addMemberToWs(request):
    """
    Agregar miembro al taller
    """
    pass

def deleteWsMember(request):
    """
    Eliminar miembro del taller
    """
    pass

def updateWorkshop(request):
    """
    Editar taller deportivo
    """
    pass

def updateTeam(request):
    """
    Editarequipo representativo
    """
    pass

def callTheRoll(request):
    """
    Pasar lista
    """
    pass


def absolveWs(request):
    """
    Liberación de taller
    """
    pass

def statisticsAttendance(request):
    pass

def statisticsMatches(request):
    pass