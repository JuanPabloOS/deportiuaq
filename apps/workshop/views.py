from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
#Decoradores
from django.contrib.auth.decorators import login_required       #pedir una sesión activa
from django.contrib.auth.decorators import user_passes_test     #Comprobar los permisos de usuario
from django.views.decorators.http import require_http_methods   #admitir determinados tipos de petición
#modelos
from apps.core.models import Workshop
#formularios
from .forms import createWorkshopForm
from .forms import deleteWorkshopForm
from .forms import deleteMemberToWorkshopForm
from .forms import updateWorkshopForm
# Create your views here.
def talleres(request):
    talleres = Workshop.objects.all()
    return render (request, 'workshop/talleres.html', {'talleres':talleres})

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
                return render(request, 'workshop/createWorkshop.html',{'form':form})
            else:
                messages.error(request,'Error: revisa que todos los datos sean correctos')
                return render(request, 'workshop/createWorkshop.html',{'form':form})
    else:
        form = createWorkshopForm()
        return render(request, 'workshop/createWorkshop.html',{'form':form})

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
        return render(request, 'workshop/deleteWorkshop.html', {'form':form})

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
        return render(request,'workshop/updateWorkshop.html',{'form':form})


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
            return render(request,'workshop/addMemberToWs.html',{'form':form})
    else:
        form = addMemberToWorkshopForm()
        return render(request,'workshop/addMemberToWs.html',{'form':form})

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
            return render(request,'workshop/deleteMemberToWs.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='DC')
def callTheRollWs(request):
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