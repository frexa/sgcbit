# Generated by Django 3.0.5 on 2021-03-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencias',
            name='firma',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]