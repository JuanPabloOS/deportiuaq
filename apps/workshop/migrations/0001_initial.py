# Generated by Django 2.2.1 on 2019-10-13 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('Varonil', 'Varonil'), ('Femenil', 'Femenil')], default='Varonil', max_length=7, verbose_name='Rama')),
                ('sport', models.CharField(choices=[('Atletismo', 'Atletismo'), ('Basketball', 'Basketball'), ('eSports', 'ESports'), ('Futbol', 'Futbol'), ('Handball', 'Handball'), ('Tennis', 'Tennis'), ('Ping-Pong', 'Ping pong'), ('Tiro con arco', 'Tiro con arco'), ('Tochito', 'Tochito'), ('Voleibol', 'Voleibol')], default='Futbol', max_length=15, verbose_name='Deporte')),
                ('schedule', models.CharField(blank=True, max_length=50, verbose_name='Horario')),
                ('totalAttendances', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Total Asistencias')),
                ('period', models.CharField(blank=True, max_length=6, null=True, verbose_name='Periodo')),
                ('maxMembers', models.PositiveIntegerField(blank=True, null=True, verbose_name='Máximo de estudiantes')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Taller deportivo',
                'verbose_name_plural': 'Talleres deportivos',
            },
        ),
        migrations.CreateModel(
            name='WsMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expediente', models.IntegerField()),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombre(s)')),
                ('last_name', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('mail', models.EmailField(max_length=254, verbose_name='Correo')),
                ('totalAssists', models.SmallIntegerField(blank=True, null=True, verbose_name='Total asistencias')),
                ('absolved', models.BooleanField(blank=True, default=False, verbose_name='Absuelto')),
                ('idWS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.Workshop')),
            ],
            options={
                'verbose_name': 'Miembro de taller',
                'verbose_name_plural': 'Miembros de taller',
            },
        ),
        migrations.CreateModel(
            name='CallTheRollWs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('attended', models.BooleanField(default=False)),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.WsMember')),
                ('idWs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.Workshop')),
            ],
        ),
    ]