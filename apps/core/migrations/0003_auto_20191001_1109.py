# Generated by Django 2.2.1 on 2019-10-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190926_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='period',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='period',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='period',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='branch',
            field=models.CharField(choices=[('VA', 'Varonil'), ('FE', 'Femenil')], default='VA', max_length=2, verbose_name='Rama'),
        ),
        migrations.AlterField(
            model_name='team',
            name='schedule',
            field=models.CharField(blank=True, max_length=50, verbose_name='Horario'),
        ),
        migrations.AlterField(
            model_name='team',
            name='sport',
            field=models.CharField(choices=[('AT', 'Atletismo'), ('BB', 'Basketball'), ('ES', 'ESports'), ('FB', 'Futbol'), ('HB', 'Handball'), ('TN', 'Tennis'), ('PP', 'Ping pong'), ('TA', 'Tiro con arco'), ('TC', 'Tochito'), ('VB', 'Voleibol')], max_length=25, verbose_name='Deporte'),
        ),
        migrations.AlterField(
            model_name='team',
            name='totalAttendances',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Total asistencias'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userType',
            field=models.CharField(choices=[('AD', 'Administrador'), ('DC', 'Docente'), ('BC', 'Becario')], default='AD', max_length=2, verbose_name='Tipo de usuario'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='branch',
            field=models.CharField(choices=[('VA', 'Varonil'), ('FE', 'Femenil')], default='VA', max_length=2, verbose_name='Rama'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='schedule',
            field=models.CharField(blank=True, max_length=50, verbose_name='Horario'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='sport',
            field=models.CharField(choices=[('AT', 'Atletismo'), ('BB', 'Basketball'), ('ES', 'ESports'), ('FB', 'Futbol'), ('HB', 'Handball'), ('TN', 'Tennis'), ('PP', 'Ping pong'), ('TA', 'Tiro con arco'), ('TC', 'Tochito'), ('VB', 'Voleibol')], default='FB', max_length=2, verbose_name='Deporte'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='totalAttendances',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Total Asistencias'),
        ),
    ]