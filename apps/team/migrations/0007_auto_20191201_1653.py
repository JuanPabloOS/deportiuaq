# Generated by Django 2.2.7 on 2019-12-01 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_auto_20191201_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winned',
            field=models.SmallIntegerField(null=True, verbose_name='¿Se ganó?'),
        ),
    ]
