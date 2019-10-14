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



