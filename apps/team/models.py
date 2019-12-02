from django.db import models
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.
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
    TENIS='Tenis'
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
        (TENIS,'Tenis'),
        (PINGPONG,'Ping pong'),
        (TIROCONARCO,'Tiro con arco'),
        (TOCHITO,'Tochito'),
        (VOLEIBOL,'Voleibol'),
    )
    responsible=models.ForeignKey('core.User', on_delete=models.CASCADE, verbose_name='Responsable')
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

class TeamMember(models.Model):
    idTeam=models.ForeignKey('Team', on_delete=models.CASCADE)
    expediente=models.IntegerField()
    first_name=models.CharField(verbose_name='Nombre(s)', max_length=30)
    last_name=models.CharField(verbose_name='Apellido',max_length=150)
    mail=models.EmailField(verbose_name='Correo', max_length=254)
    totalAttendances=models.SmallIntegerField(verbose_name='Total asistencias', blank=True, null=True)

    class Meta:
        verbose_name='Miembro de equipo'
        verbose_name_plural='Miembros de equipo'

    def __str__(self):
        return '%s %s' %(self.last_name, self.first_name)

class Match(models.Model):
    RIVAL_OPTIONS=(
        ('FBA','Bellas Artes'),
        ('FCP','Ciencias Políticas y Sociales'),
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
    # GANADO = 1
    # PERDIDO = 0
    # EMPATADO = 2
    # WINNED_OPTIONS=(
    #     (GANADO,'Se ganó'),
    #     (PERDIDO,'Se perdió'),
    #     (EMPATADO,'Empate')
    # )
    idTeam=models.ForeignKey('Team', on_delete=models.CASCADE)
    rival=models.CharField(verbose_name='Rival',max_length=3, choices=RIVAL_OPTIONS)
    winned=models.SmallIntegerField(verbose_name='¿Se ganó?')
    teamScore=models.SmallIntegerField(verbose_name='Puntos a favor')
    rivalScore=models.SmallIntegerField(verbose_name='Puntos en contra')
    period=models.CharField(verbose_name='Periodo', max_length=6, blank=True, null=True) # 2019-1

    class Meta:
        verbose_name='Partido'
        verbose_name_plural='Partidos'
    
    def __str__(self):
        return '%s vs %s' %(self.idTeam, self.rival)

class Player(models.Model):
    idMatch=models.ForeignKey('Match', on_delete=models.CASCADE)
    idTeamMember=models.ForeignKey(TeamMember, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Jugador'
        verbose_name_plural='Jugadores'
    
    def __str__(self):
        return '%s' %(self.idTeamMember)

class Sesion(models.Model):
    idTeam=models.ForeignKey('Team', on_delete=models.CASCADE)
    date=models.DateField(verbose_name='Día', auto_now_add=True)

    def __str__(self):
        return '%s %s' %(self.idTeam, self.date)

    def save(self, *args, **kwargs):
        #Evitar sesiones duplicadas
        try:
            alreadyExists = Sesion.objects.get(date=self.date)
            return False
        except ObjectDoesNotExist:
            return super(Sesion, self).save(*args, **kwargs)

class CallTheRollTeam(models.Model):
    idTeamMember=models.ForeignKey('TeamMember', on_delete=models.CASCADE, related_name='get_attendances')
    idSesion=models.ForeignKey('Sesion',on_delete=models.CASCADE, related_name="get_sesion")
    attended=models.BooleanField(verbose_name='Asistió',default=False)
    
    class Meta:
        verbose_name='Asistencia'
        verbose_name_plural='Asistencias'

    def __str__(self):
        return '%s %s' %(self.attended, self.idTeamMember)