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
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rival', models.CharField(choices=[('FBA', 'Bellas Artes'), ('FCP', 'Ciencias Políticas'), ('FCA', 'Contaduría y Administración'), ('FDE', 'Derecho'), ('FEN', 'Enfermería'), ('FFI', 'Filosofía'), ('FIN', 'Ingeniería'), ('FLL', 'Lenguas y Letras'), ('FME', 'Medicina'), ('FPS', 'Psicología'), ('FQU', 'Química')], max_length=3)),
                ('winned', models.BooleanField(default=False)),
                ('teamScore', models.SmallIntegerField()),
                ('rivalScore', models.SmallIntegerField()),
                ('period', models.CharField(blank=True, max_length=6, null=True)),
            ],
            options={
                'verbose_name': 'Partido',
                'verbose_name_plural': 'Partidos',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('Varonil', 'Varonil'), ('Femenil', 'Femenil')], default='Varonil', max_length=7, verbose_name='Rama')),
                ('sport', models.CharField(choices=[('Atletismo', 'Atletismo'), ('Basketball', 'Basketball'), ('eSports', 'ESports'), ('Futbol', 'Futbol'), ('Handball', 'Handball'), ('Tennis', 'Tennis'), ('Ping-Pong', 'Ping pong'), ('Tiro con arco', 'Tiro con arco'), ('Tochito', 'Tochito'), ('Voleibol', 'Voleibol')], max_length=15, verbose_name='Deporte')),
                ('schedule', models.CharField(blank=True, max_length=50, verbose_name='Horario')),
                ('totalAttendances', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Total asistencias')),
                ('period', models.CharField(blank=True, max_length=6, null=True)),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Equipo Representativo',
                'verbose_name_plural': 'Equipos Representativos',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expediente', models.IntegerField()),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombre(s)')),
                ('last_name', models.CharField(max_length=150, verbose_name='Apellido')),
                ('mail', models.EmailField(max_length=254, verbose_name='Correo')),
                ('totalAssists', models.SmallIntegerField(blank=True, null=True, verbose_name='Total asistencias')),
                ('idTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
            options={
                'verbose_name': 'Miembro de equipo',
                'verbose_name_plural': 'Miembros de equipo',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idMatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Match')),
                ('idTeamMember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.TeamMember')),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
            },
        ),
        migrations.AddField(
            model_name='match',
            name='idTeam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team'),
        ),
        migrations.CreateModel(
            name='CallTheRollTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('attended', models.BooleanField(default=False)),
                ('idTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.TeamMember')),
            ],
        ),
    ]
