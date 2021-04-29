# Generated by Django 3.0.5 on 2021-03-25 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estructura', '0008_remove_cbits_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='punto_referencia',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='avenida',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='calle',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='comuna',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='estado',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='municipio',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='parroquia',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='sector',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
