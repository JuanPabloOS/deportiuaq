from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from django.core import serializers
import json
# IMPORTAR modelos
from .models import Team
from .models import TeamMember
from .models import Match
from .models import Player
from .models import CallTheRollTeam
from .models import Sesion
# IMPORTAR formularios
from .forms import createTeamForm
from .forms import deleteTeamForm
from .forms import addMemberToTeamForm
from .forms import deleteMemberToTeamForm
from .forms import updateTeamForm
from .forms import registerMatchForm
 #decorador
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_http_methods   
#admitir determinados tipos de petición
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
        Ver un equipo en específico
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

# @login_required
# def verAlumnosEquipo_view(request, idTeam):
#     try:
#         taller = Team.objects.get(id=idTeam)
#         miembros = TeamMember.objects.filter(idTeam=idTeam)
#         return render(request, 'team/verAlumnos.html', {'taller':taller,'miembros':miembros})
#     except:
#         return redirect('talleres')

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
                messages.error(request,'Error en los datos')
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
        equipo.save()
        messages.success(request, 'Se actualizó el equipo')
        return redirect('verEquipo', idTeam)
    else:
        print('No se pudo actualizar')
        messages.error(request,'Equipo no actualizado')
        return redirect('verEquipo', idTeam)

@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def addMemberToTeam(request):
    """
    Agregar Alumno al equipo
    """
    if request.method == 'POST':
        form = addMemberToTeamForm(request.POST)
        if form.is_valid():
            try:
                isAlreadyIn = TeamMember.objects.get(expediente=form.cleaned_data['expediente'], idTeam__period=setPeriod())
                messages.error(request, 'El alumno ya registrado')
            except:
                alumno = form.save()
                # print("--------------")
                # print(alumno)
                # print("---------------")
                try:
                    sesiones = Sesion.objects.filter(idTeam=form.cleaned_data['idTeam'])
                    print(sesiones)
                    if len(sesiones)>0:
                        for sesion in sesiones:
                            check = CallTheRollTeam(idTeamMember=alumno, idSesion=sesion, attended=False)
                            check.save()
                except Exception as e:
                    print(str(e))
                messages.success(request, 'Alumno registrado')
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
        else:
            messages.error(request,'Error en los datos')
            # return render(request,'team/addMemberToTeam.html',{'form':form})
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
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
                member = TeamMember.objects.get(expediente=expedienteMember, idTeam=idTeam).delete()
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

@require_http_methods(['POST'])
def getMiembrosTeam(request):
    try:
        id=request.POST['idTeam']
        miembros = serializers.serialize('json', TeamMember.objects.filter(idTeam=id))
        # print(miembros)
        return JsonResponse({'status':1,'msg':'Integrantes recuperados con éxito','miembros':miembros})
    except Exception as e:
        print (str(e))
        return JsonResponse({
            'status':0,
            'msg':'El equipo no tiene integrantes aún.',
            'miembros':''
        })

    
@login_required
@user_passes_test(lambda user: user.userType=='DC')
def callTheRollTeam(request, idTeam):
    #El request tipo POST regresa un JSON
    if request.method == 'POST':
        print("Pase de lista equipo")
        # Registrar las asistencias o retardos por POST
        try:
            try: 
                # Ya existe una sesión para el día de hoy
                #Recuperar la sesión
                sesionExistente = Sesion.objects.get(idTeam=idTeam,date=datetime.date.today())
                asistencias = CallTheRollTeam.objects.filter(idSesion=sesionExistente) #recuperar las asistencias de la sesion
                for asistencia in asistencias:
                    if str(asistencia.idTeamMember_id) in request.POST['attendances']:
                        asistencia.attended = True
                        asistencia.save()
                    else:
                        print("inasistencia")
                        asistencia.attended = False
                        asistencia.save()
                return JsonResponse({'status':1, 'msg':'Pase de lista actualizado'})
            except Exception as e:
                print(str(e))
                # No existe una sesión para el día de hoy, por lo tanto se crea
                idTeamInstance = Team.objects.get(id=idTeam)
                todaySesion=''
                try:
                    todaySesion = Sesion(idTeam=idTeamInstance)
                    todaySesion.save()
                except Exception as e:
                    print(str(e))
                    return JsonResponse({'status':0,'msg':str(e)})
                alumnos = TeamMember.objects.filter(idTeam=idTeam)
                for alumno in alumnos:
                    if str(alumno.id) in request.POST['attendances']:
                        CallTheRollTeam(idTeamMember=alumno, idSesion=todaySesion, attended=True).save()
                    else:
                        CallTheRollTeam(idTeamMember=alumno, idSesion=todaySesion, attended=False).save()
                return JsonResponse({'status':1, 'msg':'Se ha tomado el pase de lista'})
        except Exception as e:
            print(str(e))
            return JsonResponse({'status':0,'msg':'No se ha podido pasar lista, intenta de nuevo'})
    else: #El request tipo GET regresa un
        asistencias = dict()                                     #Declarar el conjunto de todas las asistencias por alumno
        sesiones = Sesion.objects.filter(idTeam=idTeam).values() #Obtener las sesiones del equipo corresóndiente
        miembros = TeamMember.objects.filter(idTeam=idTeam).order_by('last_name') #Buscar los miembros inscritos en el equipo
        return render(request,'core/callTheRoll.html',{'sesiones':sesiones,'asistencias':asistencias, 'miembros':miembros})

@login_required
def registerMatch_view(request):
    if request.method == 'POST':
        try:
            idTeamInstance=get_object_or_404(Team, id=request.POST['idTeam'])
            teamScore=int(request.POST['teamScore'], base=10)
            rivalScore=int(request.POST['rivalScore'], base=10)
            winned=int('2', base=10)
            if teamScore>rivalScore:
                winned=int('1', base=10)
            elif teamScore<rivalScore:
                winned=int('0', base=10)
            form = registerMatchForm({
                'idTeam':int(request.POST['idTeam'], base=10),
                'rival':request.POST['rival'],
                'teamScore':teamScore,
                'rivalScore':rivalScore,
                'period':setPeriod()
            })
            if form.is_valid():
                try:
                    match=form.save(commit=False)
                    match.idTeam_id = idTeamInstance.id
                    match.winned=winned
                    match.save()
                    print(match)
                    alumnos = TeamMember.objects.filter(idTeam=request.POST['idTeam'])
                    for alumno in alumnos:
                        if str(alumno.id) in request.POST['jugadores']:
                            Player(idMatch=match, idTeamMember=alumno).save()
                    return JsonResponse({ 'status':1,'msg':'Petición completada'})
                except Exception as e:
                    print(str(e))
                    return JsonResponse({ 'status':0,'msg':'Petición no completada'})
            else:
                print(form.errors.as_data())
                return JsonResponse({ 'status':0,'msg':'Petición no completada'})
        except Exception as e:
            print(str(e))
            return JsonResponse({ 'status':0,'msg':'Petición no completada'})
    else:
        form = registerMatchForm()
        return render(request, 'team/match.html', {'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='DC')
def statisticsAttendance(request):
    pass
    
# Create your views here.
@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
@require_http_methods(['GET'])
def statisticsMatches(request, idTeam):
    partidos=Match.objects.filter(idTeam_id=idTeam)
    jugadores=serializers.serialize('json', list(TeamMember.objects.filter(idTeam_id=idTeam)),fields=('id','first_name','last_name'))
    # print(jugadores)
    ganados = Player.objects.filter(idMatch__idTeam=idTeam, idMatch__winned=1)
    perdidos = Player.objects.filter(idMatch__idTeam=idTeam, idMatch__winned=0)
    empatados = Player.objects.filter(idMatch__idTeam=idTeam, idMatch__winned=2)

    ganadoSet = dict()
    for ganado in ganados:
        ganadoSet[str(ganado.idMatch_id)]=list()
    for ganado in ganados:
        ganadoSet[str(ganado.idMatch_id)].append(ganado.idTeamMember_id)
    
    perdidoSet = dict()
    for perdido in perdidos:
        perdidoSet[str(perdido.idMatch_id)]=list()
    for perdido in perdidos:
        perdidoSet[str(perdido.idMatch_id)].append(perdido.idTeamMember_id)

    empatadoSet = dict()
    for empatado in empatados:
        empatadoSet[str(empatado.idMatch_id)]=list()
    for empatado in empatados:
        empatadoSet[str(empatado.idMatch_id)].append(empatado.idTeamMember_id)

    ganadoJSON=json.dumps(ganadoSet)
    perdidoJSON=json.dumps(perdidoSet)
    empatadoJSON=json.dumps(empatadoSet)
    print(ganadoJSON)
    print(empatadoJSON)
    print(perdidoJSON)
    return render(request, 'team/estadisticos.html',{
        'partidos':partidos,
        'ganadoJSON':ganadoJSON,
        'perdidoJSON':perdidoJSON,
        'empatadoJSON':empatadoJSON,
        'jugadores':jugadores
    })

# ganados = Match.objects.filter(idTeam = 2, winned=1)
# perdidos = Match.objects.filter(idTeam = 2, winned=0)
# empatados = Match.objects.filter(idTeam = 2, winned=2)
# ganados = Player.objects.filter(idMatch__idTeam=2, idMatch__winned=1)
# perdidos = Player.objects.filter(idMatch__idTeam=2, idMatch__winned=0)
# empatados = Player.objects.filter(idMatch__idTeam=2, idMatch__winned=2)
# perdidos = Player.objects.filter(idMatch__idTeam=2, idMatch__winned=0)
# empatados = Player.objects.filter(idMatch__idTeam=2, idMatch__winned=2)

# ganados = list(map(lambda x: x.idTeamMember_id , ganados))
# perdidos = list(map(lambda x: x.idTeamMember_id , perdidos))
# empatados = list(map(lambda x: x.idTeamMember_id , empatados))
# ganadoSet = dict()
# for ganado in ganados:
#     ganadoSet[ganado.idMatch_id]=set()

# for ganado in ganados:
#     ganadoSet[ganado.idMatch_id].add(ganado.idTeamMember_id)
# print("===========")
# for key in ganadoSet:
#     print(ganadoSet[key])


# perdidoSet = dict()
# for perdido in perdidos:
#     perdidoSet[perdido.idMatch_id]=set()

# for perdido in perdidos:
#     perdidoSet[perdido.idMatch_id].add(perdido.idTeamMember_id)
# print("===========")
# for key in perdidoSet:
#     print(perdidoSet[key])

# empatadoSet = dict()
# for empatado in empatados:
#     empatadoSet[empatado.idMatch_id]=set()

# for empatado in empatados:
#     empatadoSet[empatado.idMatch_id].add(empatado.idTeamMember_id)
# print("===========")
# for key in empatadoSet:
#     print(empatadoSet[key])


# print(ganados)
# print(perdidos)
# print(empatados)
# ganadosSet = serializers.serialize('json', list(ganados))
# perdidosSet = serializers.serialize('json', list(perdidos))
# empatadosSet = serializers.serialize('json', list(empatados))
# print("=========================")
# print(ganadosSet)
# print("=========================")
# print(perdidosSet)
# print("=========================")
# print(empatadosSet)
# print("=========================")