#importar herramientas
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
#importar modelos
from apps.core.models import User
from apps.core.models import Workshop
from apps.core.models import Team
#importar formularios
from .forms import createUserForm
from .forms import resetPasswordForm
from .forms import deleteUserForm
from .forms import createWorkshopForm
from .forms import createTeamForm
from .forms import deleteWorkshopForm
from .forms import deleteTeamForm
 #decorador
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

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
def resetPassword(request):
    """
    Restablecer cualquier contraseña - sólo Admins
    """
    if request.method=='POST':
        form=resetPasswordForm(request.POST)
        currentpassword=request.user.password #staff's current password   
        if form.is_valid():
            #Verificar que el usuario exista
            try:
                usuario=User.objects.get(username=form.cleaned_data.get('username')) 
                passwordAdmnistrador=form.cleaned_data.get('passwordAdministrador') 
                matchcheck=check_password(passwordAdmnistrador, currentpassword)    
                # si la contraseña del staff es correcta
                if matchcheck:
                    new_password=make_password('b'+form.cleaned_data.get('username'))          
                    usuario.password=new_password # reestablecer la contraseña
                    usuario.save()
                    messages.success(request, 'Contraseña restablecida')
                    return render(request,'exclusiveAdmin/resetPassword.html',{'form':form})
                else:
                    messages.error(request, 'La contraseña no coincide')
                    return render(request,'exclusiveAdmin/resetPassword.html',{'form':form})
            #usuario erróneo
            except User.DoesNotExist:
                messages.error(request, 'Usuario no existente')
                return render(request,'exclusiveAdmin/resetPassword.html',{'form':form})                         
        else:
            messages.error(request, 'Petición no completada')
            return render(request,'exclusiveAdmin/resetPassword.html',{'form':form})
    else:
        form=resetPasswordForm()
        return render(request,'exclusiveAdmin/resetPassword.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='AD')
def createTeacher(request):
    """
    Registrar docente
    """
    if request.POST:
        form=createUserForm(request.POST)
        if form.is_valid():
            newTeacher=form.save(commit=False)
            newTeacher.userType=User.DOCENTE
            newTeacher.password =make_password('d'+newTeacher.username)
            newTeacher.save()
            messages.success(request, 'Registro completado')
            return redirect('registrarDocente')
        else:
            messages.error(request,'Error: Registro no completado')
            return render(request, 'exclusiveAdmin/createTeacher.html',{'form':form})
    else:
        form=createUserForm()        
        return render(request, 'exclusiveAdmin/createTeacher.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='AD' or user.userType=='DC')
def createBecario(request):
    """
    Registrar becario
    """
    if request.POST:
        form=createUserForm(request.POST)
        if form.is_valid():
            newAdmin=form.save(commit=False)
            newAdmin.userType=User.BECARIO
            newAdmin.password =make_password('d'+newAdmin.username)
            newAdmin.is_staff=1
            newAdmin.save()
            messages.success(request, 'Registro completado')
            return redirect('registrarBecario')
        else:
            messages.error(request,'Error: Registro no completado')
            return render(request, 'sharedAdTea/createBecario.html',{'form':form})
    else:
        form=createUserForm()        
        return render(request, 'sharedAdTea/createBecario.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='AD')
def createAdmin(request):
    """
    Registrar Administrador
    """
    if request.POST:
        form=createUserForm(request.POST)
        if form.is_valid():
            newBecario=form.save(commit=False)
            newBecario.userType=User.ADMINISTRADOR
            newBecario.password =make_password('d'+newBecario.username)

            newBecario.save()
            messages.success(request, 'Registro completado')
            return redirect('registrarAdmin')
        else:
            messages.error(request,'Error: Registro no completado')
            return render(request, 'exclusiveAdmin/createAdmin.html',{'form':form})
    else:
        form=createUserForm()        
        return render(request, 'exclusiveAdmin/createAdmin.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='AD')
def deleteAdmin(request):
    """
        Dar de baja un administrador
    """
    if request.method == 'POST':
        passwordToVerify=''
        try: #Verificar que efectivamente se haya resibido una contraseña
            passwordToVerify=request.POST['password']
        except:
            return JsonResponse({'status':0,'msg':'Ingresa tu contraseña'})
        currentPassword=request.user.password #obtener la contraseña de loggeo
        matchcheck=check_password(passwordToVerify,currentPassword) #comparar ambas contraseñas
        if(matchcheck): #realizar la acción
            usernameTeacher=request.POST['username']
            try:
                administrador = User.objects.get(username=usernameAdmin, userType='AD')
                administrador.is_active = 0
                administrador.save()
                return JsonResponse({'status':1,'msg':'Usuario dado de baja'})
            except ObjectDoesNotExist:
                return JsonResponse({'status': 0, 'msg':'El usuario no existe'})
        else:
            return JsonResponse({'status':0,'msg':'La contraseña no coincide'})
    else:
        form=deleteUserForm()
        return render(request,'exclusiveAdmin/deleteAdmin.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='AD')
def deleteTeacher(request):
    """
        Dar de baja un docente
    """
    if request.method == 'POST':
        passwordToVerify=''
        try: #Verificar que efectivamente se haya resibido una contraseña
            passwordToVerify=request.POST['password']
        except:
            return JsonResponse({'status':0,'msg':'Ingresa tu contraseña'})
        currentPassword=request.user.password #obtener la contraseña de loggeo
        matchcheck=check_password(passwordToVerify,currentPassword) #comparar ambas contraseñas
        if(matchcheck): #realizar la acción
            usernameTeacher=request.POST['username']
            try:
                teacher = User.objects.get(username=usernameTeacher, userType='DC')
                teacher.is_active = 0
                teacher.save()
                return JsonResponse({'status':1,'msg':'Usuario dado de baja'})
            except ObjectDoesNotExist:
                return JsonResponse({'status': 0, 'msg':'El usuario no existe'})
        else:
            return JsonResponse({'status':0,'msg':'La contraseña no coincide'})
    else:
        form=deleteUserForm()
        return render(request,'exclusiveAdmin/deleteTeacher.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='AD' or user.userType=='DC')
def deleteBecario(request):
    """
        Dar de baja un docente
    """
    if request.method == 'POST':
        passwordToVerify=''
        try: #Verificar que efectivamente se haya resibido una contraseña
            passwordToVerify=request.POST['password']
        except:
            return JsonResponse({'status':0,'msg':'Ingresa tu contraseña'})
        currentPassword=request.user.password #obtener la contraseña de loggeo
        matchcheck=check_password(passwordToVerify,currentPassword) #comparar ambas contraseñas
        if(matchcheck): #realizar la acción
            usernameTeacher=request.POST['username']
            try:
                teacher = User.objects.get(username=usernameTeacher, userType='BC')
                teacher.is_active = 0
                teacher.save()
                return JsonResponse({'status':1,'msg':'Usuario dado de baja'})
            except ObjectDoesNotExist:
                return JsonResponse({'status': 0, 'msg':'El usuario no existe'})
        else:
            return JsonResponse({'status':0,'msg':'La contraseña no coincide'})
    else:
        form=deleteUserForm()
        return render(request,'sharedAdTea/deleteBecario.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='AD')
def createWorkshop(request):
    """
    Crear taller deportivo
    """
    if request.method == 'POST':
        form=createWorkshopForm(request.POST)
        try:
            exists = Workshop.objects.get(sport=request.POST['sport'],branch=request.POST['branch'],period=setPeriod())
            messages.error(request, 'Ya existe ese taller')
            return redirect('crearTaller')
        except ObjectDoesNotExist:
            if form.is_valid():
                newWs = form.save(commit=False)
                newWs.period = setPeriod()
                newWs.save()
                messages.success(request,'Registro completado')
                return render(request, 'exclusiveAdmin/createWorkshop.html',{'form':form})
            else:
                messages.error(request,'Error: revisa que todos los datos sean correctos')
                return render(request, 'exclusiveAdmin/createWorkshop.html',{'form':form})
        #return render(request, 'exclusiveAdmin/createWorkshop.html',{'form':form})
    else:
        form = createWorkshopForm()
        return render(request, 'exclusiveAdmin/createWorkshop.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='AD')
def deleteWorkshop(request):
    """
    Eliminar taller deportivo
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
            workshopId=request.POST['workshop_id']
            try:
                objects, dictionary = Workshop.objects.get(id=workshopId).delete()
                return JsonResponse({'status':1,'msg':'Taller eliminado','objects':objects,'dictionary':dictionary})
            except ObjectDoesNotExist:
                return JsonResponse({'status':0,'msg':'El taller no existe o ya ha sido eliminado'})
        else:
            return JsonResponse({'status':0,'msg':'La contraseña no coincide'})
    else:
        form = deleteWorkshopForm()
        return render(request, 'exclusiveAdmin/deleteWorkshop.html', {'form':form})

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
                return render(request, 'exclusiveAdmin/createTeam.html',{'form':form})
            else:
                messages.error(request,'Error: revisa que todos los datos sean correctos')
                return render(request, 'exclusiveAdmin/createTeam.html',{'form':form})
        #return render(request, 'exclusiveAdmin/createTeam.html',{'form':form})
    else:
        form = createTeamForm()
        return render(request, 'exclusiveAdmin/createTeam.html',{'form':form})

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
        return render(request, 'exclusiveAdmin/deleteTeam.html', {'form':form})
