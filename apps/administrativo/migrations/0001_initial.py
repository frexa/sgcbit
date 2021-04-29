# Generated by Django 3.0.5 on 2021-03-05 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('Director(a)', 'Director(a)'), ('Encargado(a) del CBIT', 'Encargado(a) del CBIT')], max_length=30)),
                ('cedula', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('celular', models.BigIntegerField(unique=True)),
            ],
            options={
                'db_table': 'empledos',
            },
        ),
        migrations.CreateModel(
            name='Inasistencias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('dia', models.CharField(choices=[('L', 'lunes'), ('M', 'martes'), ('Mi', 'miercoles'), ('J', 'jueves'), ('V', 'viernes')], max_length=2)),
                ('justificativo', models.FileField(blank=True, null=True, upload_to='')),
                ('motivo', models.TextField(blank=True, null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativo.Empleados')),
            ],
            options={
                'db_table': 'inasistencias',
            },
        ),
        migrations.CreateModel(
            name='Asistencias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('dia', models.CharField(choices=[('L', 'lunes'), ('M', 'martes'), ('Mi', 'miercoles'), ('J', 'jueves'), ('V', 'viernes')], max_length=2)),
                ('hora_entrada', models.TimeField()),
                ('hora_salida', models.TimeField(blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('actividad', models.TextField(blank=True, null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativo.Empleados')),
            ],
            options={
                'db_table': 'asistencias',
            },
        ),
    ]