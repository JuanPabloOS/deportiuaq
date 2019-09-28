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
from core.models import User
#importar formularios
from .forms import createUserForm
from .forms import resetPasswordForm
from .forms import deleteSomethingForm
from .forms import createWorkshopForm
from .forms import createTeamForm
#decorador
from django.contrib.auth.decorators import login_required
# from core.decorators import confirm_password
#from core.decorators import confirmPassToContinue

# Create your views here.

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

def deleteAdmin(request):
    """
        Dar de baja un administrador

    """
    if request.method == 'POST':
        usernameAdmin=request.POST['username']
        try:
            administrador = User.objects.get(username=usernameAdmin, userType='AD')
            administrador.is_active = 0
            administrador.save()
            return JsonResponse({'status':1,'msg':'Usuario dado de baja'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 0, 'msg':'El usuario no existe'})
    else:
        form=deleteSomethingForm()
        return render(request,'exclusiveAdmin/deleteAdmin.html',{'form':form})


def createWorkshop(request):
    """
    Crear taller deportivo
    """
    if request.method == 'POST':
        form=createWorkshopForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,'Registro completado')
            return render(request, 'exclusiveAdmin/createWorkshop.html',{'form':form})
        else:
            messages.error(request,'Error: revisa que todos los datos sean correctos')
            return render(request, 'exclusiveAdmin/createWorkshop.html',{'form':form})
        #return render(request, 'exclusiveAdmin/createWorkshop.html',{'form':form})
    else:
        form = createWorkshopForm()
        return render(request, 'exclusiveAdmin/createWorkshop.html',{'form':form})


def deleteWorkshop(request):
    """
    Eliminar taller deportivo
    """
    pass

def createTeam(request):
    """
    Crear equipo representativo
    """
    if request.method == 'POST':
        form=createTeamForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,'Registro completado')
            return render(request, 'exclusiveAdmin/createTeam.html',{'form':form})
        else:
            messages.error(request,'Error: revisa que todos los datos sean correctos')
            return render(request, 'exclusiveAdmin/createTeam.html',{'form':form})
        #return render(request, 'exclusiveAdmin/createTeam.html',{'form':form})
    else:
        form = createTeamForm()
        return render(request, 'exclusiveAdmin/createTeam.html',{'form':form})


def deleteTeam(request):
    """
    Eliminar equipo representativo
    """
    pass

