from django.db import models
from django.urls import reverse
from apps.administrativo.models import Empleados
from apps.estructura.models import CBITS 
# Create your models here.

ESTADO_USO = (('EN USO','EN USO'),
		   ('EN DESUSO', 'EN DESUSO'),
		   ('ALMACENADO','ALMACENADO'))

ESTADO_FISICO = (('BUENO','BUENO'),
				 ('REGULAR', 'REGULAR'),
				 ('MALO','MALO'))

MARCAS=(('VIT','VIT'),
		('HP','HP'),
		('IBM','IBM'),
		('EPSON','EPSON'))

TIPO_EQUIPO=(('ELECTRÓNICO', 'ELECTRÓNICO'),
			('MOBILIARIO','MOBILIARIO'))

class Equipos(models.Model):
	cbit = models.ForeignKey(CBITS, on_delete= models.CASCADE)
	serial = models.CharField(max_length=20, unique=True)
	modelo = models.CharField(max_length=40)
	descripcion = models.CharField(max_length=25,null=True)
	observacion = models.CharField(max_length=25,null=True)
	tipo_de_bien = models.CharField(max_length=11,default='TECNOLÓGICO')
	fundacion = models.CharField(max_length=8,default='FUNDABIT')
	marca = models.CharField(max_length=5,choices=MARCAS)
	estado_uso = models.CharField(max_length=10,choices=ESTADO_USO)
	estado_fisico=models.CharField(max_length=7,choices=ESTADO_FISICO)
	tipo_equipo=models.CharField(max_length=11,choices=TIPO_EQUIPO)

	class Meta:
		db_table='equipos'

	def get_url_detail(self):
		return reverse('detail-equipo', args=[str(self.id)])

	def get_url_update(self):
		return reverse('update-equipo', args=[str(self.id)])

	def get_url_delete(self):
		return reverse('delete-equipo', args=[str(self.id)])