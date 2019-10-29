from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
#Decoradores
from django.contrib.auth.decorators import login_required       #pedir una sesión activa
from django.contrib.auth.decorators import user_passes_test     #Comprobar los permisos de usuario
from django.views.decorators.http import require_http_methods   #admitir determinados tipos de petición
#modelos
from .models import Workshop
from .models import WsMember
from .models import CallTheRollWs
from .models import Sesion
from apps.core.models import User
#formularios
from .forms import createWorkshopForm
from .forms import deleteWorkshopForm
from .forms import deleteMemberToWorkshopForm
from .forms import updateWorkshopForm
from .forms import addMemberToWorkshopForm
#PDF
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape, A4
#Específico para obtener el período actual
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
def talleres_view(request):
    """
    Lista todos los talleres
    """
    talleres = Workshop.objects.all()
    return render(request, 'workshop/talleres.html', {'talleres':talleres})
    #return HttpResponse(talleres)

@login_required
def verTaller_view(request, idTaller):
    """
        Ver un taller en específico
    """
    # print("===================")
    # print(request.user)
    # print("===================")
    try:
        periodo=setPeriod()
        taller=Workshop.objects.get(id=idTaller)
        miembros = WsMember.objects.filter(idWs=idTaller)
        updateForm = updateWorkshopForm(initial={
                'id':taller.id,
                'responsible':taller.responsible,
                'schedule':taller.schedule,
                'maxMembers':taller.maxMembers,
        })
        
        addMemberForm=addMemberToWorkshopForm(initial={
            'idWs':taller.id
        })
        return render(request,'workshop/editarTaller.html',{'miembros':miembros,'taller':taller,'updateForm':updateForm, 'addMemberForm':addMemberForm})
    except ObjectDoesNotExist:
        return redirect('talleres')


def verAlumnosTaller_view(request, idTaller):
    try:
        taller = Workshop.objects.get(id=idTaller)
        miembros = WsMember.objects.filter(idWs=idTaller)
        return render(request, 'workshop/verAlumnos.html', {'taller':taller,'miembros':miembros})
    except:
        return redirect('talleres')

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
                newWs.responsible=form.cleaned_data['responsible']
                newWs.save()
                messages.success(request,'Registro completado')
                return redirect('crearTaller')
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

@require_http_methods(['POST'])
@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def updateWorkshop(request, idTaller):
    """
    Editar taller deportivo
    """
    form = updateWorkshopForm(request.POST)
    if form.is_valid():
        taller=Workshop.objects.get(id=form.cleaned_data['id'])
        taller.responsible=form.cleaned_data['responsible']
        scheduleStr=form.cleaned_data['schedule']
        taller.schedule=scheduleStr
        taller.maxMembers=form.cleaned_data['maxMembers']
        taller.save()
        messages.success(request, 'Se actualizó el taller')
        return redirect('verTaller', idTaller)
    else:
        print('No se pudo actualizar')
        messages.error(request,'No se pudo actualizar el taller')
        return redirect('verTaller', idTaller)

@require_http_methods(['POST'])
@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def addMemberToWs(request):
    """
    Agregar Alumno al taller
    """
    form = addMemberToWorkshopForm(request.POST)
    if form.is_valid():
        try:
            isAlreadyIn = WsMember.objects.get(expediente=form.cleaned_data["expediente"], idWs__period=setPeriod())
            # print("<--------->")
            # print(isAlreadyIn)
            # print("<--------->")
            messages.error(request, 'El alumno ya está registrado en otro taller')
            
        except:
            form.save()
            messages.success(request,'Registro completado')
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
        
def match(request):
    return render(request, 'workshop/createMatch.html')


@login_required
@user_passes_test(lambda user: user.userType=='DC' or user.userType=='BC')
def deleteWsMember(request):
    """
    Eliminar Alumno del taller
    """
    if request.method=='POST':
        passwordToVerify=''
        try: #Verificar que efectivamente se haya recibido una contraseña
            passwordToVerify=request.POST['password']
        except:
            return JsonResponse({'status':0,'msg':'Ingresa tu contraseña'})
        currentPassword=request.user.password #obtener la contraseña de loggeo        
        matchcheck=check_password(passwordToVerify,currentPassword) #comparar ambas contraseñas
        if(matchcheck): #realizar la acción
            expedienteMember=request.POST['expediente']
            idWs=request.POST['idWs']
            try:
                member = WsMember.objects.get(expediente=int(expedienteMember), idWs_id=int(idWs)).delete()
                return JsonResponse({'status':1,'msg':'Usuario dado de baja'})
            except:
                return JsonResponse({'status': 0, 'msg':'El usuario no existe'})
        else:
            return JsonResponse({'status':0,'msg':'La contraseña no coincide'})
    else:
            form=deleteMemberToWorkshopForm()
            return render(request,'workshop/deleteMemberToWs.html',{'form':form})

from django.core import serializers
from django.db.models import Prefetch
from django.db.models import Count
@login_required
@user_passes_test(lambda user: user.userType=='DC')
def callTheRollWs(request, idTaller):
    if request.method == 'POST':
        try:
            pass
        except:
            pass
    else:
        
        asistencias = dict()                                     #Declarar el conjunto de todas las asistencias por alumno

        sesiones = Sesion.objects.filter(idWs=idTaller).values() #Obtener las sesiones del taller corresóndiente
        for sesion in sesiones:
            sesion['date'] =  datetime.date.strftime(sesion['date'],'%d/%m/%y')
        #print("===============sesiones")
        #print(sesiones)
        miembros = WsMember.objects.filter(idWs=idTaller).order_by('last_name') #Buscar los miembros inscritos en el taller
        for miembro in miembros:#Por cada integrante del taller hacer lo siguiente
            attendances = CallTheRollWs.objects.filter(idSesion__idWs=idTaller, idWsMember=miembro.id).values() #obtener asistencias por integrante
            a =dict() #declarar el subconjunto de asistencias como diccionario
            for attendance in attendances: #por cada instancia en el queryset hacer lo siguiente
                #crear una nueva posición en 'a' con el idSesion_id de la instancia 
                #como llave y agregarle la misma instancia
                
                a[attendance['idSesion_id']]=attendance
            asistencias[miembro]=list(a);   #Agregar el subconjunto de asistencias 
                                            #en el conjunto de asistencias por cada miembro del taller
        # print("==============")
        # print(asistencias)
        return render(request,'workshop/callTheRoll.html',{'sesiones':sesiones,'asistencias':asistencias, 'miembros':miembros})
        
   
# @login_required
# @user_passes_test(lambda user: user.userType=='DC')
def absolveWs(request):
    alumnos = list(WsMember.objects.all())
    w, h = A4
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setFont("Times-Roman", 20)
    while(len(alumnos)>0):
        p.drawString(150,h-150,'FACULTAD DE INFORMÁTICA')
        p.setFont("Times-Roman", 18)
        p.drawString(155,h-180,'COORDINACIÓN DE DEPORTES')
        p.setFont("Times-Roman", 12)
        p.drawString(175,h-200,'TALLERES DE DESARROLLO HUMANO')
        p.setFont("Times-Roman", 14)
        p.drawString(215,h-230,'FORMATO DE LIBERACIÓN')

        p.drawString(100,h-300,'Disciplina de taller: Basquetbol')
        p.drawString(100,h-316,'Nombre: '+alumnos[0].first_name)
        p.drawString(100,h-332,'Carrera: %s Grupo: %s Matrícula: %s' %(alumnos[0].plan, alumnos[0].group, alumnos[0].expediente))
        p.drawString(100,h-348,'Por medio de la presente, se hace la notificación de manera oficial, que el')
        p.drawString(100,h-364,'alumno cumplió satisfactoriamente su estadía participando en el Taller')
        p.drawString(100,h-380,'Deportivo de:')
        p.drawString(100,h-396,'Tiro con arco')
        p.drawString(100,h-412,'en el período comprendido de agosto-diciembre 2019.')
        p.drawString(100,h-450,'Se extiende la presente para los efectos que al interesado convengan.')
        alumnos.pop(0)
        p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='Liberación de talleres.pdf')
