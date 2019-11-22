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
from .models import Sesion
#formularios
from .forms import createTeamForm
from .forms import deleteTeamForm
from .forms import addMemberToTeamForm
from .forms import deleteMemberToTeamForm
from .forms import updateTeamForm
from .forms import registerMatchForm
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
def equipos_view(request):
    """
    Lista todos los equipos
    """
    equipos = Team.objects.all()
    return render(request, 'team/equipos.html', {'equipos':equipos})

@login_required
def verEquipo_view(request, idTeam):
    """
        Ver un taller en específico
    """
    # print("===================")
    # print(request.user)
    # print("===================")
    try:
        periodo=setPeriod()
        equipo=Team.objects.get(id=idTeam)
        miembros = TeamMember.objects.filter(idTeam=idTeam)
        updateForm = updateTeamForm(initial={
                'id':equipo.id,
                'responsible':equipo.responsible,
                'schedule':equipo.schedule,
        })
        
        addMemberForm=addMemberToTeamForm(initial={
            'idTeam':equipo.id
        })
        return render(request,'team/editarEquipo.html',{'miembros':miembros,'equipo':equipo,'updateForm':updateForm, 'addMemberForm':addMemberForm})
    except ObjectDoesNotExist:
        return redirect('equipos')

@login_required
def verAlumnosEquipo_view(request, idTeam):
    try:
        taller = Team.objects.get(id=idTaller)
        miembros = TeamMember.objects.filter(idWs=idTaller)
        return render(request, 'workshop/verAlumnos.html', {'taller':taller,'miembros':miembros})
    except:
        return redirect('talleres')

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
                team.responsible=form.cleaned_data['responsible']
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
def updateTeam(request, idTeam):
    """
    Editar equipo representativo
    """
    form = updateTeamForm(request.POST)
    if form.is_valid():
        equipo=Team.objects.get(id=form.cleaned_data['id'])
        equipo.responsible=form.cleaned_data['responsible']
        scheduleStr=form.cleaned_data['schedule']
        equipo.schedule=scheduleStr
        equipo.maxMembers=form.cleaned_data['maxMembers']
        equipo.save()
        messages.success(request, 'Se actualizó el equipo')
        return redirect('verEquipo', idTeam)
    else:
        print('No se pudo actualizar')
        messages.error(request,'No se pudo actualizar el taller')
        return redirect('verTaller', idTaller)

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

@require_http_methods(['GET'])
def seleccionarEquipo(request):
    equipos = Team.objects.filter(responsible=request.user, period=setPeriod())
    return render(request, 'team/seleccionarEquipo.html',{'equipos':equipos})

@login_required
@user_passes_test(lambda user: user.userType=='DC')
def callTheRollTeam(request, idTeam):
    #El request tipo POST regresa un JSON
    if request.method == 'POST':
        # Registrar las asistencias o retardos por POST
        try:
            try: 
                # Ya existe una sesión para el día de hoy
                #Recuperar la sesión
                sesionExistente = Sesion.objects.get(idTeam=idTeam,date=datetime.date.today())
                asistencias = CallTheRollTeam.objects.filter(idSesion=sesionExistente) #recuperar las asistencias de la sesion
                for asistencia in asistencias:
                    if str(asistencia.idWsMember_id) in request.POST['attendances']:
                        asistencia.attended = True
                        asistencia.save()
                    else:
                        print("inasistencia")
                        asistencia.attended = False
                        asistencia.save()
                return JsonResponse({'status':1, 'msg':'Pase de lista actualizado'})
            except ObjectDoesNotExist:
                # No existe una sesión para el día de hoy, por lo tanto se crea
                idTeamInstance = get_object_or_404(Workshop, id=idTeam)
                todaySesion = Sesion(idWs=idTeamInstance, date=datetime.date.today())
                todaySesion.save()
                alumnos = TeamMember.objects.filter(idTeam=idTeam)
                for alumno in alumnos:
                    if str(alumno.id) in request.POST['attendances']:
                        CallTheRollTeam(idTeamMember=alumno, idSesion=todaySesion, attended=True).save()
                    else:
                        CallTheRollTeam(idTeamMember=alumno, idSesion=todaySesion, attended=False).save()
                return JsonResponse({'status':1, 'msg':'Se ha tomado el pase de lista'})
        except Exception as e:
            return JsonResponse({'status':0,'msg':'No se ha podido pasar lista, intenta de nuevo'})
    else: #El request tipo GET regresa un
        asistencias = dict()                                     #Declarar el conjunto de todas las asistencias por alumno
        sesiones = Sesion.objects.filter(idTeam=idTeam).values() #Obtener las sesiones del taller corresóndiente
        miembros = TeamMember.objects.filter(idTeam=idTeam).order_by('last_name') #Buscar los miembros inscritos en el taller
        return render(request,'team/callTheRoll.html',{'sesiones':sesiones,'asistencias':asistencias, 'miembros':miembros})


def registerMatch_view(request):
    form = registerMatchForm()
    return render(request, 'team/match.html', {'form':form})
@login_required
@user_passes_test(lambda user: user.userType=='DC')
def statisticsMatches(request):
    pass

# Create your views here.
@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def statisticsAttendance(request):
    pass