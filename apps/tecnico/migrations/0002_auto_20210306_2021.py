# Generated by Django 3.0.5 on 2021-03-07 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='tipo_equipo',
            field=models.CharField(choices=[('ELECTRÓNICO', 'ELECTRÓNICO'), ('MOBILIARIO', 'MOBILIARIO')], max_length=11),
        ),
    ]
