from django.db import models

from django.contrib.auth.models import AbstractUser

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
    userType = models.CharField(max_length=2, choices = USER_TYPE_OPTIONS, default=ADMINISTRADOR)

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

class Team(models.Model):
    VARONIL='VA'
    FEMENIL='FE'
    RAMA_OPTIONS=(
        (VARONIL,'Varonil'),
        (FEMENIL,'Femenil'),
    )
    ATLETISMO='AT'
    BASKETBALL='BB'
    ESPORTS='ES'
    FUTBOL='FB'
    HANDBALL='HB'
    TENNIS='TN'
    PINGPONG='PP'
    TIROCONARCO='TA'
    TOCHITO='TC'
    VOLEIBOL='VB'
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
    branch=models.CharField(max_length=2,choices=RAMA_OPTIONS, default=VARONIL)
    sport=models.CharField(max_length=25, choices=SPORT_OPTIONS)
    schedule=models.CharField(max_length=50, blank=True)
    totalAttendances=models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return '%s %s' %(self.sport, self.branch) 
class Workshop(models.Model):
    VARONIL='VA'
    FEMENIL='FE'
    RAMA_OPTIONS=(
        (VARONIL,'Varonil'),
        (FEMENIL,'Femenil'),
    )
    ATLETISMO='AT'
    BASKETBALL='BB'
    ESPORTS='ES'
    FUTBOL='FB'
    HANDBALL='HB'
    TENNIS='TN'
    PINGPONG='PP'
    TIROCONARCO='TA'
    TOCHITO='TC'
    VOLEIBOL='VB'
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
    branch=models.CharField(max_length=2,choices=RAMA_OPTIONS, default=VARONIL)
    sport=models.CharField(max_length=2, choices=SPORT_OPTIONS, default=FUTBOL)
    schedule=models.CharField(max_length=50, blank=True)
    totalAttendances=models.PositiveSmallIntegerField(blank=True, null=True)

class TeamMember(models.Model):
    idTeam=models.ForeignKey('Team', on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=150)
    mail=models.EmailField(max_length=254)
    totalAssists=models.SmallIntegerField(blank=True, null=True)


class WsMember(models.Model):
    idWS=models.ForeignKey('Workshop', on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=150)
    mail=models.EmailField(max_length=254)
    totalAssists=models.SmallIntegerField(blank=True, null=True)

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
    period=models.CharField(max_length=6) # 2019-1

class Player(models.Model):
    idMatch=models.ForeignKey('Match', on_delete=models.CASCADE)
    idTeamMember=models.ForeignKey(TeamMember, on_delete=models.CASCADE)

class CallTheRollTeam(models.Model):
    idUser=models.ForeignKey('User', on_delete=models.CASCADE)
    idTeamTeam=models.ForeignKey('Team', on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    attended=models.BooleanField(default=False)