#importar herramientas
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib import messages
#importar modelos
from core.models import User
#importar formularios
from .forms import createUserForm
from .forms import resetPasswordForm



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
                    print("=== matchcheck")
                    # nueva contraseña a:
                    # username + .  (El nombre de usuario más un punto)
                    new_password=make_password(form.cleaned_data.get('username')+'.')          
                    usuario.password=new_password # reestablecer la contraseña
                    usuario.save()
                    messages.success(request, 'Contraseña reestablecida')
                    return render(request,'',{'form':form})
                else:
                    messages.error(request, 'La contraseña no coincide')
                    return render(request,'',{'form':form})
            #usuario erróneo
            except User.DoesNotExist:
                messages.error(request, 'Usuario no existente')
                return render(request,'',{'form':form})                         
        else:
            messages.error(request, 'Petición no completada')
            return render(request,'',{'form':form})
    else:
        form=resetPassword()
        return render(request,'',{'form':form})

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
            return HttpResponse('Registro completado')
        else:
            messages.error(request,'Error: Registro no completado')
            return HttpResponse('Error: Registro completado')
    else:
        form=createUserForm()
        context={
            'form':form
        }
        return render(request, 'exclusiveAdmin/createTeacher.html',context)

def createBecario(request):
    """
    Registrar becario
    """
    pass

def createAdmin(request):
    """
    Registrar Administrador
    """
    pass

def deleteUser(request):
    """
    Eliminar usuario
    """
    pass

def updateUser(request):
    """
    Actualizar usuario
    """
    pass

def createWorkshop(request):
    """
    Crear taller deportivo
    """
    pass


def deleteWorkshop(request):
    """
    Eliminar taller deportivo
    """
    pass

def createTeam(request):
    """
    Crear equipo representativo
    """
    pass


def deleteTeam(request):
    """
    Eliminar equipo representativo
    """
    pass

