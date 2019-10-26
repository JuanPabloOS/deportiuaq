from django.db import models


# Create your models here.
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
    responsible=models.ForeignKey('core.User', on_delete=models.CASCADE)
    branch=models.CharField(verbose_name='Rama', max_length=7,choices=RAMA_OPTIONS, default=VARONIL)
    sport=models.CharField(verbose_name='Deporte', max_length=15, choices=SPORT_OPTIONS, default=FUTBOL)
    schedule=models.CharField(verbose_name='Horario', max_length=50, blank=True)
    totalAttendances=models.PositiveSmallIntegerField(verbose_name='Total Asistencias', blank=True, null=True)
    period=models.CharField(verbose_name='Periodo', max_length=6, blank=True, null=True) # 2019-1
    maxMembers=models.PositiveIntegerField(verbose_name='Máximo de estudiantes', blank=True, null=True)

    class Meta:
        verbose_name='Taller deportivo'
        verbose_name_plural='Talleres deportivos'

    def __str__(self):
        return '%s %s' %(self.sport, self.branch)



class WsMember(models.Model):
    PLAN_CHOICES = (
        ('SOF11','SOF11'),
        ('LAT11','LAT11'),
        ('INF11','INF11'),
        ('INC11','INC11'),
        ('TEL11','TEL11'),
        ('SOF18','SOF18'),
        ('LAT18','LAT18'),
        ('INF18','INF18'),
        ('INC18','INC18'),
        ('TEL18','TEL18'),
    )
    GROUP_CHOICES=(
        (60,'60'),
        (70,'70'),
        (71,'71'),
        (72,'72'),
        (73,'73'),
        (74,'74'),
    )
    idWS=models.ForeignKey('Workshop', on_delete=models.CASCADE)
    expediente=models.IntegerField()
    first_name=models.CharField(verbose_name='Nombre(s)', max_length=30)
    last_name=models.CharField(verbose_name='Apellidos',max_length=150)
    mail=models.EmailField(verbose_name='Correo',max_length=254)
    plan=models.CharField(choices=PLAN_CHOICES, max_length=5, default='SOF11')
    group=models.SmallIntegerField(choices=GROUP_CHOICES, default=70)
    totalAssists=models.SmallIntegerField(verbose_name='Total asistencias', blank=True, null=True)
    absolved=models.BooleanField(verbose_name='Absuelto',default=False, blank=True)
    
    class Meta:
        verbose_name='Miembro de taller'
        verbose_name_plural='Miembros de taller'

    def __str__(self):
        return '%s %s' %(self.last_name, self.first_name)


class CallTheRollWs(models.Model):
    idUser=models.ForeignKey('WsMember', on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    attended=models.BooleanField(default=False)
