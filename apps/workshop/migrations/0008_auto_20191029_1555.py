# Generated by Django 2.2.1 on 2019-10-29 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0007_auto_20191028_1550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calltherollws',
            options={'verbose_name': 'Asistencia', 'verbose_name_plural': 'Asistencias'},
        ),
        migrations.RenameField(
            model_name='wsmember',
            old_name='idWS',
            new_name='idWs',
        ),
    ]
