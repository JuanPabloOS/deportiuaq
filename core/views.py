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