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

#importar formularios
from .forms import createUserForm
from .forms import resetPasswordForm
from .forms import deleteUserForm


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
                    new_password=make_password('d'+form.cleaned_data.get('username'))          
                    usuario.password=new_password # reestablecer la contraseña
                    usuario.save()
                    messages.success(request, 'Contraseña restablecida')
                    return render(request,'core/resetPassword.html',{'form':form})
                else:
                    messages.error(request, 'La contraseña no coincide')
                    return render(request,'core/resetPassword.html',{'form':form})
            #usuario erróneo
            except User.DoesNotExist:
                messages.error(request, 'Usuario no existente')
                return render(request,'core/resetPassword.html',{'form':form})                         
        else:
            messages.error(request, 'Petición no completada')
            return render(request,'core/resetPassword.html',{'form':form})
    else:
        form=resetPasswordForm()
        return render(request,'core/resetPassword.html',{'form':form})

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
            return render(request, 'core/createTeacher.html',{'form':form})
    else:
        form=createUserForm()        
        return render(request, 'core/createTeacher.html',{'form':form})

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
            return render(request, 'core/createBecario.html',{'form':form})
    else:
        form=createUserForm()        
        return render(request, 'core/createBecario.html',{'form':form})

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
            return render(request, 'core/createAdmin.html',{'form':form})
    else:
        form=createUserForm()        
        return render(request, 'core/createAdmin.html',{'form':form})

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
        return render(request,'core/deleteAdmin.html',{'form':form})

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
        return render(request,'core/deleteTeacher.html',{'form':form})

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
        return render(request,'core/deleteBecario.html',{'form':form})






