from django.shortcuts import render

# Create your views here.
def login(request):
    """
    Iniciar sesión
    """
    pass

def logout(request):
    """
    Cerrar sesión
    """
    pass

def resetPassword(request):
    """
    Restablecer cualquier contraseña - sólo Admins
    """
    pass

def changePassword(request):
    """
    Cambiar contraseña
    """
    pass

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
