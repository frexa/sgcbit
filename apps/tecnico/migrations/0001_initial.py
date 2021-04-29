# Generated by Django 3.0.5 on 2021-03-05 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estructura', '0001_initial'),
        ('administrativo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=20, unique=True)),
                ('modelo', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=25)),
                ('observacion', models.CharField(max_length=25)),
                ('tipo_de_bien', models.CharField(default='TECNOLÓGICO', max_length=11)),
                ('fundacion', models.CharField(default='FUNDABIT', max_length=8)),
                ('marca', models.CharField(choices=[('VIT', 'VIT'), ('HP', 'HP'), ('IBM', 'IBM'), ('EPSON', 'EPSON')], max_length=5)),
                ('estado_uso', models.CharField(choices=[('EN USO', 'EN USO'), ('EN DESUSO', 'EN DESUSO'), ('ALMACENADO', 'ALMACENADO')], max_length=10)),
                ('estado_fisico', models.CharField(choices=[('BUENO', 'BUENO'), ('REGULAR', 'REGULAR'), ('MALO', 'MALO')], max_length=7)),
                ('tipo_equipo', models.CharField(choices=[('computador', 'computador'), ('mobiliario', 'mobiliario')], max_length=10)),
                ('cbit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estructura.CBITS')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativo.Empleados')),
            ],
            options={
                'db_table': 'equipos',
            },
        ),
    ]