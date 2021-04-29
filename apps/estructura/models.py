from django.db import models
from django.urls import reverse
from apps.administrativo.models import Empleados

tipo_de_servicio=(('EVDO','EVDO'),
					('ABA','ABA'),
					('SATELITAL','SATELITAL'),
					('NINGUNO','NINGUNO'))

class Direccion(models.Model):
	estado = models.CharField(max_length=40, null=True)
	municipio = models.CharField(max_length=40, null=True)
	parroquia = models.CharField(max_length=40, null=True)
	comuna = models.CharField(max_length=40, null=True,blank=True)
	avenida = models.CharField(max_length=40, null=True)
	sector = models.CharField(max_length=40, null=True)
	calle = models.CharField(max_length=40, null=True)
	punto_referencia= models.CharField(max_length=40, null=True)

	def __str__(self):
		return '%s %s %s %s %s %s %s'%(self.estado,
									self.municipio,
									self.parroquia,
									self.avenida,
									self.sector,
									self.calle,
									self.punto_referencia)

	def get_absolute_url(self):
		return reverse('update-direccion', args=[str(self.id)])

class Planteles(models.Model):
	direccion = models.OneToOneField(Direccion, on_delete=models.SET_NULL,blank=True, null=True)
	empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE,blank=True, null=True)
	codigo_DEA = models.CharField(max_length=15,default='OD06491504',unique=True)
	matricula_est = models.PositiveIntegerField(null=True)
	docentes = models.PositiveIntegerField(null=True)
	nivel_academico = models.CharField(max_length=20,default='NIVEL Y BÁSICA')
	dependencia = models.CharField(max_length=10,default='NACIONAL')
	telefono= models.CharField(max_length=15,null=True)
	nombre_circuito = models.CharField(max_length=25,null=True)
	anno_fundacion=models.IntegerField(null=True)
	cantidad_aulas=models.PositiveIntegerField(null=True)

	def get_absolute_url(self):
		return reverse('detail-plantel', args=[str(self.id)])

	def get_url_update(self):
		return reverse('update-plantel', args=[str(self.id)])

	def get_url_delete(self):
		return reverse('delete-plantel', args=[str(self.id)])

	def __str__(self):
		return '%s'%(self.nombre_circuito)

	class Meta:
		db_table='planteles'


class INTERNET(models.Model):
	serial = models.CharField(max_length=20,blank=True, null=True)
	linea_asociada=models.CharField(max_length=20,blank=True, null=True)
	tipo = models.CharField(max_length=15, choices=tipo_de_servicio, blank=True)

	class Meta:
		db_table='internet'

class CBITS(models.Model):
	plantel = models.OneToOneField(Planteles, on_delete=models.SET_NULL,blank=True, null=True)
	empleado=models.ForeignKey(Empleados, on_delete=models.SET_NULL,blank=True, null=True)
	internet=models.OneToOneField(INTERNET, on_delete=models.SET_NULL, null=True, blank=True)
	nombre = models.CharField(max_length=25,blank=True, null=True)

	def __str__(self):
		return '%s'%(self.nombre)
	
	def get_absolute_url(self):
		return reverse('detail-cbit', args=[str(self.id)])

	def get_url_update(self):
		return reverse('update-cbit', args=[str(self.id)])

	def get_url_delete(self):
		return reverse('delete-cbit', args=[str(self.id)])

	class Meta:
		db_table='cbits'