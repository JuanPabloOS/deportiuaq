# Generated by Django 2.2.7 on 2019-12-01 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_auto_20191201_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winned',
            field=models.SmallIntegerField(default=1, verbose_name='¿Se ganó?'),
            preserve_default=False,
        ),
    ]