from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
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
#IMPORTAR Modelos
from .models import Workshop
from .models import WsMember
from .models import CallTheRollWs
from .models import Sesion
from apps.core.models import User
# IMPORTAR Formularios
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

@login_required
def liberaciones_view(request, idTaller):
    try:
        taller = Workshop.objects.get(id=idTaller)
        miembros = WsMember.objects.filter(idWs=idTaller)
        for miembro in miembros:
            miembro.totalAttendances=len(CallTheRollWs.objects.filter(idWsMember=miembro.id, attended=True))
        return render(request, 'workshop/liberaciones.html', {'taller':taller,'miembros':miembros})
    except Exception as e:
        print(str(e))
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
                messages.error(request,'Error en los datos')
                return render(request, 'workshop/createWorkshop.html',{'form':form})
    else:
        form = createWorkshopForm()
        return render(request, 'workshop/createWorkshop.html',{'form':form})

@login_required
@user_passes_test(lambda user: user.userType=='AD')
@require_http_methods(['POST'])
def deleteWorkshop(request):
    """
    Eliminar taller deportivo
    """
    if request.method == 'POST': #Obtener los datos por POST
        passwordToVerify=''
        try: #Verificar que efectivamente se haya resibido una contraseña
            passwordToVerify=request.POST['password']
        except Exception as e:
            print(str(e))
            return JsonResponse({'status':0,'msg':'Ingresa tu contraseña'})
        currentPassword=request.user.password #obtener la contraseña de loggeo
        matchcheck=check_password(passwordToVerify,currentPassword) #comparar ambas contraseñas
        if(matchcheck): #realizar la acción
            workshopId=request.POST['workshop_id']
            try:
                objects, dictionary = Workshop.objects.get(id=workshopId).delete()
                # print("=================")
                # print(str(objects))
                # print(str(dictionary))
                # print("=================")
                return JsonResponse({'status':1,'msg':'Taller eliminado','objects':objects,'dictionary':dictionary})
            except Exception as e:
                print(str(e))
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
        messages.error(request,'Taller no actualizado')
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
            messages.error(request, 'Alumno ya registrado')
        except:
            registrado = form.save()
            if(registrado != False):
                try:
                    sesiones = Sesion.objects.filter(idWs=form.cleaned_data['idWs'])
                    print(sesiones)
                    if len(sesiones)>0:
                        for sesion in sesiones:
                            check = CallTheRollWs(idWsMember=registrado, idSesion=sesion, attended=True)
                            check.save()
                except Exception as e:
                    print(str(e))
                messages.success(request,'Registro completado')
            else:
                messages.error(request, 'Límite alcanzado')
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    else:
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

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

@login_required
# @user_passes_test(lambda user: user.userType=='DC')
def callTheRollWs(request, idTaller):
    #El request tipo POST regresa un JSON
    print("llamando")
    if request.method == 'POST':
        print("Pase de lista taller")
        try:
            try: 
                # Ya existe una sesión para el día de hoy
                #Recuperar la sesión
                sesionExistente = Sesion.objects.get(idWs=idTaller,date=datetime.date.today())
                # print("----- sesión existente")
                # print(str(sesionExistente))
                asistencias = CallTheRollWs.objects.filter(idSesion=sesionExistente) #recuperar las asistencias de la sesion
                # print("-- asistencias")
                # print(str(asistencias))
                for asistencia in asistencias:
                    if str(asistencia.idWsMember_id) in request.POST['attendances']:
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
                idWsInstance = Workshop.objects.get(id=idTaller)
                todaySesion=''
                try:
                    todaySesion = Sesion(idWs=idWsInstance)
                    todaySesion.save()
                    print("--------- try create sesion")
                    print(str(todaySesion))
                    # return JsonResponse({'status':1,'id':todaySesion.id})
                except Exception as e:
                    print("------------- no crear")
                    print(str(e))
                    return JsonResponse({'status':0,'msg':str(e)})
                    # 
                alumnos = WsMember.objects.filter(idWs=idTaller)
                for alumno in alumnos:
                    if str(alumno.id) in request.POST['attendances']:
                        CallTheRollWs(idWsMember=alumno, idSesion=todaySesion, attended=True).save()
                    else:
                        CallTheRollWs(idWsMember=alumno, idSesion=todaySesion, attended=False).save()
                return JsonResponse({'status':1, 'msg':'Se ha tomado el pase de lista'})
        except Exception as e:
            print(str(e))
            return JsonResponse({'status':0,'msg':'No se ha podido pasar lista, intenta de nuevo'})
        # Registrar las asistencias o retardos por POST
        # try:
        #     try: 
        #         # Ya existe una sesión para el día de hoy
        #         #Recuperar la sesión
        #         sesionExistente = Sesion.objects.get(idWs=idTaller,date=datetime.date.today())
        #         asistencias = CallTheRollWs.objects.filter(idSesion=sesionExistente) #recuperar las asistencias de la sesion
        #         for asistencia in asistencias:
        #             if str(asistencia.idWsMember_id) in request.POST['attendances']:
        #                 asistencia.attended = True
        #                 asistencia.save()
        #             else:
        #                 print("inasistencia")
        #                 asistencia.attended = False
        #                 asistencia.save()
        #         return JsonResponse({'status':1, 'msg':'Pase de lista actualizado'})
        #     except Exception as e:
        #         print(str(e))
        #         # No existe una sesión para el día de hoy, por lo tanto se crea
        #         idWsInstance = get_object_or_404(Workshop, id=idTaller)
        #         todaySesion = Sesion(idWs=idWsInstance, date=datetime.date.today())
        #         todaySesion.save(commit=False)
        #         todaySesion.save()
        #         alumnos = WsMember.objects.filter(idWs=idTaller)
        #         for alumno in alumnos:
        #             if str(alumno.id) in request.POST['attendances']:
        #                 CallTheRollWs(idWsMember=alumno, idSesion=todaySesion, attended=True).save()
        #             else:
        #                 CallTheRollWs(idWsMember=alumno, idSesion=todaySesion, attended=False).save()
        #         return JsonResponse({'status':1, 'msg':'Se ha tomado el pase de lista'})
        # except Exception as e:
        #     print(str(e))
        #     return JsonResponse({'status':0,'msg':'No se ha podido pasar lista, intenta de nuevo'})
    else: #El request tipo GET regresa un
        asistencias = dict()                                     #Declarar el conjunto de todas las asistencias por alumno
        sesiones = Sesion.objects.filter(idWs=idTaller).values() #Obtener las sesiones del taller corresóndiente
        miembros = WsMember.objects.filter(idWs=idTaller).order_by('last_name') #Buscar los miembros inscritos en el taller
        print("------------")
        print(sesiones)
        print("------------")
        print(miembros)
        return render(request,'core/callTheRoll.html',{'sesiones':sesiones,'asistencias':asistencias, 'miembros':miembros})

@require_http_methods(['GET'])
def seleccionarEquipo(request):
    equipos = Workshop.objects.filter(responsible=request.user, period=setPeriod())
    return render(request, 'workshop/seleccionarEquipo.html',{'equipos':equipos})


@login_required
@user_passes_test(lambda user: user.userType=='DC')
@require_http_methods(['POST'])
def absolverAlumnos(request, idTaller):
    try:
        liberaciones= request.POST['liberaciones'].split(',')
        print(liberaciones)
        alumnos = WsMember.objects.filter(idWs=idTaller)
        for alumno in alumnos:
            if str(alumno.id) in liberaciones:
                alumno.absolved = True
                alumno.save()
            
        return JsonResponse({'status':1,'msg':'Listo'})
    except Exception as e:
        print(str(e))
        return JsonResponse({'status':0,'msg':str(e)})

from wsgiref.util import FileWrapper
from django.utils.encoding import smart_str
@login_required
@user_passes_test(lambda user: user.userType=='DC')
def showPdf(request, idTaller):
    
    alumnos=list(WsMember.objects.filter(idWs=idTaller, absolved=True))
    w, h = A4
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    
    while(len(alumnos)>0):
        p.setFont("Times-Roman", 20)
        p.drawString(150,h-150,'FACULTAD DE INFORMÁTICA')
        p.setFont("Times-Roman", 18)
        p.drawString(155,h-180,'COORDINACIÓN DE DEPORTES')
        p.setFont("Times-Roman", 12)
        p.drawString(175,h-200,'TALLERES DE DESARROLLO HUMANO')
        p.setFont("Times-Roman", 14)
        p.drawString(200,h-230,'FORMATO DE LIBERACIÓN')
        
        # Escibir los campos
        p.drawString(100,h-300,'Disciplina de taller:')
        p.drawString(100,h-316,'Nombre:')
        p.drawString(100,h-332,'Carrera:')
        p.drawString(210,h-332,'Grupo:')
        p.drawString(290,h-332,'Matrícula:')
        p.drawString(100,h-348,'Por medio de la presente, se hace la notificación de manera oficial, que')
        p.drawString(100,h-364,'el alumno  cumplió satisfactoriamente  su estadía  participando durante')
        p.drawString(100,h-380,'el período comprendido de agosto-diciembre 2019 en el taller:')
        
        
        p.drawString(250,h-550,'ATENTAMENTE')
        p.line(200, h-630, 400, h-630)
        p.drawString(170,h-645,'Coordinador de deportes Facultad de Informática')
        # Escribir los valores
        p.setFont("Times-Bold", 14)
        p.drawString(220,h-300,str(alumnos[0].idWs))
        p.drawString(155,h-316,alumnos[0].first_name)
        p.drawString(150,h-332,str(alumnos[0].plan))
        p.drawString(250,h-332,str(alumnos[0].group))
        p.drawString(350,h-332,str(alumnos[0].expediente))
        p.drawString(100,h-413,str(alumnos[0].idWs))
        p.setFont("Times-Roman", 14)
        p.drawString(100,h-450,'Se extiende la presente para los efectos que al interesado convengan.')
        alumnos.pop(0)
        p.showPage()
    p.save()
    p = buffer.getvalue()
    buffer.close()
    response = HttpResponse(content_type='application/pdf')
    response.write(p)
    return response
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    # buffer.seek(0)
    # w=FileWrapper(buffer)
    # # return FileResponse(w, mimetype="text/plain", as_attachment=False, filename='Liberación de talleres.pdf')
    # response = HttpResponse(content_type='application/pdf') # mimetype is replaced by content_type for django 1.7
    # response['Content-Disposition'] = 'attachment; filename=%s' % 'liberaciones.pdf'
    # response['X-Sendfile'] = smart_str(buffer)
    # # It's usually a good idea to set the 'Content-Length' header too.
    # # You can also set any other required headers: Cache-Control, etc.
    # return response
