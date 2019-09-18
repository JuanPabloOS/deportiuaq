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

class Team(models.Model):
    VARONIL='VA'
    FEMENIL='FE'
    RAMA_OPTIONS=(
        (VARONIL,'Varonil'),
        (FEMENIL,'Femenil'),
    )
    responsible=models.ForeignKey(User, on_delete=models.CASCADE)
    branch=models.CharField(max_length=2,choices=RAMA_OPTIONS, default=VARONIL)
    sport=models.CharField(max_length=25)
    schedule=models.CharField(max_length=50)
    totalAttendances=models.PositiveSmallIntegerField(blank=True, null=True)
    
class Workshop(models.Model):
    VARONIL='VA'
    FEMENIL='FE'
    RAMA_OPTIONS=(
        (VARONIL,'Varonil'),
        (FEMENIL,'Femenil'),
    )
    responsible=models.ForeignKey(User, on_delete=models.CASCADE)
    branch=models.CharField(max_length=2,choices=RAMA_OPTIONS, default=VARONIL)
    sport=models.CharField(max_length=25)
    schedule=models.CharField(max_length=50)
    totalAttendances=models.PositiveSmallIntegerField(blank=True, null=True)

class TeamMember(models.Model):
    idTeam=models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=150)
    mail=models.EmailField(max_length=254)
    totalAssists=models.SmallIntegerField(blank=True, null=True)


class WsMember(models.Model):
    idWS=models.ForeignKey(Workshop, on_delete=models.CASCADE)
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
    idTeam=models.ForeignKey(Team, on_delete=models.CASCADE)
    rival=models.CharField(max_length=3, choices=RIVAL_OPTIONS)
    winned=models.BooleanField(default=False)
    teamScore=models.SmallIntegerField()
    rivalScore=models.SmallIntegerField()
    period=models.CharField(max_length=6) #2019-1


class Player(models.Model):
    idMatch=models.ForeignKey(Match, on_delete=models.CASCADE)
    idTeamMember=models.ForeignKey(TeamMember, on_delete=models.CASCADE)