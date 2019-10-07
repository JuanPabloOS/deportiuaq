from django.db import models
from django.contrib.auth.models import AbstractUser

import datetime

class User(AbstractUser):
    #username
    #first_name
    #last_name
    #password
    #mail
    #is_staff
    ADMINISTRADOR='AD'
    DOCENTE='DC'
    BECARIO='BC'
    USER_TYPE_OPTIONS = (
      (ADMINISTRADOR,'Administrador'),
      (DOCENTE,'Docente'),
      (BECARIO,'Becario'),
    )
    userType = models.CharField(verbose_name='Tipo de usuario', max_length=2, choices = USER_TYPE_OPTIONS, default=ADMINISTRADOR)

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

class Team(models.Model):
    VARONIL='Varonil'
    FEMENIL='Femenil'
    RAMA_OPTIONS=(
        (VARONIL,'Varonil'),
        (FEMENIL,'Femenil'),
    )
    ATLETISMO='Atletismo'
    BASKETBALL='Basketball'
    ESPORTS='eSports'
    FUTBOL='Futbol'
    HANDBALL='Handball'
    TENNIS='Tennis'
    PINGPONG='Ping-Pong'
    TIROCONARCO='Tiro con arco'
    TOCHITO='Tochito'
    VOLEIBOL='Voleibol'
    SPORT_OPTIONS=(
        (ATLETISMO,'Atletismo'),
        (BASKETBALL,'Basketball'),
        (ESPORTS,'ESports'),
        (FUTBOL,'Futbol'),
        (HANDBALL,'Handball'),
        (TENNIS,'Tennis'),
        (PINGPONG,'Ping pong'),
        (TIROCONARCO,'Tiro con arco'),
        (TOCHITO,'Tochito'),
        (VOLEIBOL,'Voleibol'),
    )
    responsible=models.ForeignKey('User', on_delete=models.CASCADE)
    branch=models.CharField(verbose_name='Rama', max_length=7,choices=RAMA_OPTIONS, default=VARONIL)
    sport=models.CharField(verbose_name='Deporte', max_length=15, choices=SPORT_OPTIONS)
    schedule=models.CharField(verbose_name='Horario', max_length=50, blank=True)
    totalAttendances=models.PositiveSmallIntegerField(verbose_name='Total asistencias', blank=True, null=True)
    period=models.CharField(max_length=6, blank=True, null=True) # 2019-1

    class Meta:
        verbose_name='Equipo Representativo'
        verbose_name_plural='Equipos Representativos'

    def __str__(self):
        return '%s %s' %(self.sport, self.branch)

class Workshop(models.Model):
    VARONIL='Varonil'
    FEMENIL='Femenil'
    RAMA_OPTIONS=(
        (VARONIL,'Varonil'),
        (FEMENIL,'Femenil'),
    )
    ATLETISMO='Atletismo'
    BASKETBALL='Basketball'
    ESPORTS='eSports'
    FUTBOL='Futbol'
    HANDBALL='Handball'
    TENNIS='Tennis'
    PINGPONG='Ping-Pong'
    TIROCONARCO='Tiro con arco'
    TOCHITO='Tochito'
    VOLEIBOL='Voleibol'
    SPORT_OPTIONS=(
        (ATLETISMO,'Atletismo'),
        (BASKETBALL,'Basketball'),
        (ESPORTS,'ESports'),
        (FUTBOL,'Futbol'),
        (HANDBALL,'Handball'),
        (TENNIS,'Tennis'),
        (PINGPONG,'Ping pong'),
        (TIROCONARCO,'Tiro con arco'),
        (TOCHITO,'Tochito'),
        (VOLEIBOL,'Voleibol'),
    )
    responsible=models.ForeignKey('User', on_delete=models.CASCADE)
    branch=models.CharField(verbose_name='Rama', max_length=7,choices=RAMA_OPTIONS, default=VARONIL)
    sport=models.CharField(verbose_name='Deporte', max_length=15, choices=SPORT_OPTIONS, default=FUTBOL)
    schedule=models.CharField(verbose_name='Horario', max_length=50, blank=True)
    totalAttendances=models.PositiveSmallIntegerField(verbose_name='Total Asistencias', blank=True, null=True)
    period=models.CharField(verbose_name='Periodo', max_length=6, blank=True, null=True) # 2019-1

    class Meta:
        verbose_name='Taller deportivo'
        verbose_name_plural='Talleres deportivos'

    def __str__(self):
        return '%s %s' %(self.sport, self.branch)

class TeamMember(models.Model):
    idTeam=models.ForeignKey('Team', on_delete=models.CASCADE)
    expediente=models.IntegerField()
    first_name=models.CharField(verbose_name='Nombre(s)', max_length=30)
    last_name=models.CharField(verbose_name='Apellido',max_length=150)
    mail=models.EmailField(verbose_name='Correo', max_length=254)
    totalAssists=models.SmallIntegerField(verbose_name='Total asistencias', blank=True, null=True)

    class Meta:
        verbose_name='Miembro de equipo'
        verbose_name_plural='Miembros de equipo'

class WsMember(models.Model):
    idWS=models.ForeignKey('Workshop', on_delete=models.CASCADE)
    expediente=models.IntegerField()
    first_name=models.CharField(verbose_name='Nombre(s)', max_length=30)
    last_name=models.CharField(verbose_name='Apellidos',max_length=150)
    mail=models.EmailField(verbose_name='Correo',max_length=254)
    totalAssists=models.SmallIntegerField(verbose_name='Total asistencias', blank=True, null=True)
    absolved=models.BooleanField(verbose_name='Absuelto',default=False, blank=True)

    class Meta:
        verbose_name='Miembro de taller'
        verbose_name_plural='Miembros de taller'

class Match(models.Model):
    RIVAL_OPTIONS=(
        ('FBA','Bellas Artes'),
        ('FCP','Ciencias Políticas'),
        ('FCA','Contaduría y Administración'),
        ('FDE','Derecho'),
        ('FEN','Enfermería'),    
        ('FFI','Filosofía'),
        ('FIN','Ingeniería'),
        ('FLL','Lenguas y Letras'),
        ('FME','Medicina'),
        ('FPS','Psicología'),                        
        ('FQU','Química'),                
    )
    idTeam=models.ForeignKey('Team', on_delete=models.CASCADE)
    rival=models.CharField(max_length=3, choices=RIVAL_OPTIONS)
    winned=models.BooleanField(default=False)
    teamScore=models.SmallIntegerField()
    rivalScore=models.SmallIntegerField()
    period=models.CharField(max_length=6, blank=True, null=True) # 2019-1

    class Meta:
        verbose_name='Partido'
        verbose_name_plural='Partidos'

class Player(models.Model):
    idMatch=models.ForeignKey('Match', on_delete=models.CASCADE)
    idTeamMember=models.ForeignKey(TeamMember, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Jugador'
        verbose_name_plural='Jugadores'

class CallTheRollTeam(models.Model):
    idUser=models.ForeignKey('TeamMember', on_delete=models.CASCADE)
    idTeam=models.ForeignKey('Team', on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    attended=models.BooleanField(default=False)

class CallTheRollWs(models.Model):
    idUser=models.ForeignKey('WsMember', on_delete=models.CASCADE)
    idWs=models.ForeignKey('Workshop', on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    attended=models.BooleanField(default=False)
