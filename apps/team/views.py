from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
#modelos
from .models import Team
from .models import TeamMember
from .models import Match
from .models import Player
from .models import CallTheRollTeam
#formularios
from .forms import createTeamForm
from .forms import deleteTeamForm
from .forms import addMemberToTeamForm
from .forms import deleteMemberToTeamForm

 #decorador
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_http_methods   #admitir determinados tipos de petición

import datetime
# Create your views here.
def setPeriod():
    """
    Obtener el periodo actual
    """
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    period=''
    if 0<month<8: #el primer período termina en julio
        period=str(year)+'-1'
    else:
        period=str(year)+'-2'
    return period

@login_required
@user_passes_test(lambda user: user.userType=='AD')
def createTeam(request):
    """
    Crear equipo representativo
    """
    if request.method == 'POST':
        try:
            exists = Team.objects.get(sport=request.POST['sport'], branch=request.POST['branch'], period=setPeriod())
            messages.error(request,'Ya existe ese equipo')
            return redirect('crearEquipo')
        except ObjectDoesNotExist:
            form=createTeamForm(request.POST)
            if form.is_valid():
                team=form.save(commit=False)
                team.period = setPeriod()
                team.save()
                messages.success(request,'Registro completado')
                return render(request, 'team/createTeam.html',{'form':form})
            else:
                messages.error(request,'Error: revisa que todos los datos sean correctos')
                return render(request, 'team/createTeam.html',{'form':form})
        #return render(request, 'team/createTeam.html',{'form':form})
    else:
        form = createTeamForm()
        return render(request, 'team/createTeam.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='AD')
def deleteTeam(request):
    """
    Eliminar equipo representativo
    """
    if request.method == 'POST': #Obtener los datos por POST
        passwordToVerify=''
        try: #Verificar que efectivamente se haya resibido una contraseña
            passwordToVerify=request.POST['password']
        except:
            return JsonResponse({'status':0,'msg':'Ingresa tu contraseña'})
        currentPassword=request.user.password #obtener la contraseña de loggeo
        matchcheck=check_password(passwordToVerify,currentPassword) #comparar ambas contraseñas
        if(matchcheck): #realizar la acción
            teamId=request.POST.get('team_id',False)
            try:
                objects, dictionary = Team.objects.get(id=teamId).delete()
                return JsonResponse({'status':1,'msg':'Equipo eliminado','objects':objects,'dictionary':dictionary})
            except ObjectDoesNotExist:
                return JsonResponse({'status':0,'msg':'El equipo no existe o ya ha sido eliminado'})
        else:
            return JsonResponse({'status':0,'msg':'La contraseña no coincide'})
    else:
        form = deleteTeamForm()
        return render(request, 'team/deleteTeam.html', {'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def updateTeam(request):
    """
    Editarequipo representativo
    """
    pass

@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def addMemberToTeam(request):
    """
    Agregar Alumno al equipo
    """
    if request.method == 'POST':
        form = addMemberToTeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registro completado')
            return redirect('addMemberToTeam')
        else:
            messages.error(request,'Error: revisa que los datos sean correctos')
            return render(request,'team/addMemberToTeam.html',{'form':form})
    else:
        form = addMemberToTeamForm()
        return render(request,'team/addMemberToTeam.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def deleteTeamMember(request):
    """
    Eliminar Alumno del equipo
    """
    if request.method=='POST':
        passwordToVerify=''
        try: #Verificar que efectivamente se haya resibido una contraseña
            passwordToVerify=request.POST['password']
        except:
            return JsonResponse({'status':0,'msg':'Ingresa tu contraseña'})
        currentPassword=request.user.password #obtener la contraseña de loggeo
        matchcheck=check_password(passwordToVerify,currentPassword) #comparar ambas contraseñas
        if(matchcheck): #realizar la acción
            expedienteMember=request.POST['expediente']
            idTeam=request.POST['idTeam']
            try:
                member = WsMember.objects.get(expediente=expedienteMember, idTeam=idTeam).delete()
                return JsonResponse({'status':1,'msg':'Usuario dado de baja'})
            except ObjectDoesNotExist:
                return JsonResponse({'status': 0, 'msg':'El usuario no existe'})
        else:
            return JsonResponse({'status':0,'msg':'La contraseña no coincide'})
    else:
            form=deleteMemberToTeamForm()
            return render(request,'team/deleteMemberToTeam.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='DC')
def callTheRollTeam(request):
    """
    Pasar lista
    """
    pass

@login_required
@user_passes_test(lambda user: user.userType=='DC')
def statisticsMatches(request):
    pass

# Create your views here.
@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def statisticsAttendance(request):
    pass