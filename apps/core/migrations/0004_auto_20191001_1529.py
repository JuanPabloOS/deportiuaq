# Generated by Django 2.2.1 on 2019-10-01 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191001_1109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name': 'Partido', 'verbose_name_plural': 'Partidos'},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name': 'Jugador', 'verbose_name_plural': 'Jugadores'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Equipo Representativo', 'verbose_name_plural': 'Equipos Representativos'},
        ),
        migrations.AlterModelOptions(
            name='teammember',
            options={'verbose_name': 'Miembro de equipo', 'verbose_name_plural': 'Miembros de equipo'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterModelOptions(
            name='workshop',
            options={'verbose_name': 'Taller deportivo', 'verbose_name_plural': 'Talleres deportivos'},
        ),
        migrations.AlterModelOptions(
            name='wsmember',
            options={'verbose_name': 'Miembro de taller', 'verbose_name_plural': 'Miembros de taller'},
        ),
        migrations.AlterField(
            model_name='team',
            name='branch',
            field=models.CharField(choices=[('Varonil', 'Varonil'), ('Femenil', 'Femenil')], default='Varonil', max_length=2, verbose_name='Rama'),
        ),
        migrations.AlterField(
            model_name='team',
            name='sport',
            field=models.CharField(choices=[('Atletismo', 'Atletismo'), ('Basketball', 'Basketball'), ('eSports', 'ESports'), ('Futbol', 'Futbol'), ('Handball', 'Handball'), ('Tennis', 'Tennis'), ('Ping-Pong', 'Ping pong'), ('Tiro con arco', 'Tiro con arco'), ('Tochito', 'Tochito'), ('Voleibol', 'Voleibol')], max_length=25, verbose_name='Deporte'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Nombre(s)'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='mail',
            field=models.EmailField(max_length=254, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='totalAssists',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Total asistencias'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='branch',
            field=models.CharField(choices=[('Varonil', 'Varonil'), ('Femenil', 'Femenil')], default='Varonil', max_length=7, verbose_name='Rama'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='period',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Periodo'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='sport',
            field=models.CharField(choices=[('Atletismo', 'Atletismo'), ('Basketball', 'Basketball'), ('eSports', 'ESports'), ('Futbol', 'Futbol'), ('Handball', 'Handball'), ('Tennis', 'Tennis'), ('Ping-Pong', 'Ping pong'), ('Tiro con arco', 'Tiro con arco'), ('Tochito', 'Tochito'), ('Voleibol', 'Voleibol')], default='Futbol', max_length=15, verbose_name='Deporte'),
        ),
        migrations.AlterField(
            model_name='wsmember',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Nombre(s)'),
        ),
        migrations.AlterField(
            model_name='wsmember',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='wsmember',
            name='mail',
            field=models.EmailField(max_length=254, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='wsmember',
            name='totalAssists',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Total asistencias'),
        ),
    ]