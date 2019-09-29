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
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
# from .forms import ConfirmPasswordForm


def principalPage(request):
    """
    Muestra la página informativa del portal
    """
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
                    return redirect('home')
                messages.error(request, 'Error de datos')
                return redirect('login')
            return redirect('login')
        form = LoginForm()
        return render(request,'core/login.html',{'form':form})

@login_required
def home(request):
    """
    Muestra el Panel de Control
    """
    return render(request, 'core/home.html')


def logout_view(request):
    """
    Cerrar sesión
    """
    logout(request)
    return redirect('login')

@login_required
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
            return redirect('changePassword')
        else:
            messages.error(request, 'Contraseña no actualizada')
            return render(request, 'core/changePassword.html', {'form': form })    
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'core/changePassword.html', {'form': form })

# class confirmPassToContinue(UpdateView):
#     form_class = ConfirmPasswordForm
#     template_name = 'core/confirmPassToContinue.html'

#     def get_object(self):
#         return self.request.user

#     def get_success_url(self):
#         print("=========================")
#         print("Continuar")
#         return self.request.get_full_path()

