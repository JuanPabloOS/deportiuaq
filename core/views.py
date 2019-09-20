from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
def principalPage(request):
    return render(request, 'principalPage.html',{})
    
def login_view(request):
    """
    Iniciar sesión
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():            
                expediente = request.POST['username']
                passw = request.POST['password']
                user = authenticate(request, username=expediente, password=passw)  #hacer el loggeo del usuario
                request.session.set_expiry(36000)
                if user is not None:
                    login(request, user)
                    return render(request, 'home.html')
                messages.error(request, 'Error de datos')
                return render(request,'',{'form':form,'data':'Error en los datos'})
            return redirect('login')
        form = LoginForm()
        return render(request,'login.html',{'form':form})

def home(request):
    return render(request, 'home.html')


def logout_view(request):
    """
    Cerrar sesión
    """
    logout(request)
    return redirect('login')

def resetPassword(request):
    """
    Restablecer cualquier contraseña - sólo Admins
    """
    pass

def changePassword(request):
    """
    Cambiar contraseña
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Tu contraseña se actualizó correctamente')
            return redirect('cambiar-password')
        else:
            messages.error(request, 'Contraseña no actualizada')
            return render(request, 'salud/cambiar-password.html', {'form': form })    
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'salud/cambiar-password.html', {'form': form })

def createTeacher(request):
    """
    Registrar docente
    """
    pass

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

def updateWorkshop(request):
    """
    Editar taller deportivo
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

def updateTeam(request):
    """
    Editarequipo representativo
    """
    pass

def deleteTeam(request):
    """
    Eliminar equipo representativo
    """
    pass

def addMemberToTeam(request):
    """
    Agregar miembro al equipo
    """
    pass

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

def deletememberWsMember(request):
    """
    Eliminar miembro del taller
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
