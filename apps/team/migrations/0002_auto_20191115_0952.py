# Generated by Django 2.2.1 on 2019-11-15 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammember',
            old_name='totalAssists',
            new_name='totalAttendances',
        ),
        migrations.AlterField(
            model_name='calltherollteam',
            name='attended',
            field=models.BooleanField(default=False, verbose_name='Asistió'),
        ),
        migrations.AlterField(
            model_name='match',
            name='period',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Periodo'),
        ),
        migrations.AlterField(
            model_name='match',
            name='rival',
            field=models.CharField(choices=[('FBA', 'Bellas Artes'), ('FCP', 'Ciencias Políticas y Sociales'), ('FCA', 'Contaduría y Administración'), ('FDE', 'Derecho'), ('FEN', 'Enfermería'), ('FFI', 'Filosofía'), ('FIN', 'Ingeniería'), ('FLL', 'Lenguas y Letras'), ('FME', 'Medicina'), ('FPS', 'Psicología'), ('FQU', 'Química')], max_length=3, verbose_name='Rival'),
        ),
        migrations.AlterField(
            model_name='match',
            name='rivalScore',
            field=models.SmallIntegerField(verbose_name='Puntos en contra'),
        ),
        migrations.AlterField(
            model_name='match',
            name='teamScore',
            field=models.SmallIntegerField(verbose_name='Puntos a favor'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winned',
            field=models.BooleanField(default=False, verbose_name='¿Se ganó?'),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='date',
            field=models.DateField(verbose_name='Día'),
        ),
        migrations.AlterField(
            model_name='team',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Responsable'),
        ),
    ]
