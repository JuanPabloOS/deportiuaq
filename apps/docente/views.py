from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse

#Decoradores
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# import forms
from .forms import addMemberToTeamForm
from .forms import deleteMemberToWorkshopForm
from .forms import deleteMemberToTeamForm
from .forms import updateWorkshopForm

from apps.core.models import User
from apps.core.models import Workshop
from apps.core.models import Team
from apps.core.models import TeamMember
from apps.core.models import Match
from apps.core.models import Player
from apps.core.models import CallTheRollTeam
from apps.core.models import CallTheRollWs

from django.contrib.auth.hashers import check_password

# Create your views here.
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
            return render(request,'exclusiveTeacher/addMemberToTeam.html',{'form':form})
    else:
        form = addMemberToTeamForm()
        return render(request,'exclusiveTeacher/addMemberToTeam.html',{'form':form})

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
            return render(request,'exclusiveTeacher/deleteMemberToTeam.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def addMemberToWs(request):
    """
    Agregar Alumno al taller
    """
    if request.method == 'POST':
        form = addMemberToWorkshopForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registro completado')
            return redirect('addMemberToWs')
        else:
            messages.error(request,'Error: revisa que los datos sean correctos')
            return render(request,'exclusiveTeacher/addMemberToWs.html',{'form':form})
    else:
        form = addMemberToWorkshopForm()
        return render(request,'exclusiveTeacher/addMemberToWs.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def deleteWsMember(request):
    """
    Eliminar Alumno del taller
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
            idWS=request.POST['idWS']
            try:
                member = WsMember.objects.get(expediente=expedienteMember, idWS=idWS).delete()
                return JsonResponse({'status':1,'msg':'Usuario dado de baja'})
            except ObjectDoesNotExist:
                return JsonResponse({'status': 0, 'msg':'El usuario no existe'})
        else:
            return JsonResponse({'status':0,'msg':'La contraseña no coincide'})
    else:
            form=deleteMemberToWorkshopForm()
            return render(request,'exclusiveTeacher/deleteMemberToWs.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def updateWorkshop(request):
    """
    Editar taller deportivo
    """
    if request.method == 'POST':
        form = updateWorkshopForm(request.POST)
        if form.is_valid():
            return HttpResponse('Formulario válido')
        else:
            return HttpResponse('Formulario no válido')
    else:
        form = updateWorkshopForm()
        return render(request,'exclusiveTeacher/updateWorkshop.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def updateTeam(request):
    """
    Editarequipo representativo
    """
    pass

@login_required
@user_passes_test(lambda user: user.userType=='DC')
def callTheRollWs(request):
    """
    Pasar lista
    """
    pass

@login_required
@user_passes_test(lambda user: user.userType=='DC')
def callTheRollTeam(request):
    """
    Pasar lista
    """
    pass

@login_required
@user_passes_test(lambda user: user.userType=='DC')
def absolveWs(request):
    """
    Liberación de taller
    """
    pass

@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def statisticsAttendance(request):
    pass

@login_required
@user_passes_test(lambda user: user.userType=='DC')
def statisticsMatches(request):
    pass