from django.db import models
from django.urls import reverse
from datetime import date
from django.utils import timezone

ROLES=(('Director(a)', 'Director(a)'),
	   ('Encargado(a) del CBIT', 'Encargado(a) del CBIT'))

class Empleados(models.Model):
	rol = models.CharField(max_length=30,choices=ROLES,blank=True,null=True)
	cedula = models.IntegerField(unique=True)
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	correo = models.EmailField(null=True, blank=True)
	celular = models.BigIntegerField(unique=True)

	class Meta:
		db_table='empledos'

	def __str__(self):
		return '%s %s'%(self.nombre, self.apellido)
	
	def get_absolute_url(self):
		return reverse('detail-empleado', args=[str(self.id)])
	
	def get_url_update(self):
		return reverse('update-empleado', args=[str(self.id)])

	def get_url_delete(self):
		return reverse('delete-empleado', args=[str(self.id)])



class Asistencias(models.Model):
	empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
	fecha = models.DateField(blank=True,null=True)
	dia = models.CharField(max_length=10,blank=True,null=True)
	hora_entrada = models.TimeField()
	hora_salida = models.TimeField(null=True, blank=True)
	observacion = models.CharField(null=True, blank=True,max_length=40)
	actividad = models.CharField(null=True, blank=True,max_length=40)
	firma = models.CharField(null=True, blank=True,max_length=30)
	
	class Meta:
		db_table='asistencias'

	def translate(self):
		if self.fecha.strftime("%A") == 'Monday':
			return "Lunes"

		if self.fecha.strftime("%A") == 'Tuesday':
			return "Martes"

		if self.fecha.strftime("%A") == 'Wednesday':
			return "Miércoles"

		if self.fecha.strftime("%A") == 'Thursday':
			return "Jueves"

		if self.fecha.strftime("%A") == 'Friday':
			return "Viernes"

		if self.fecha.strftime("%A") == 'Sunday':
			return "Domingo"

		if self.fecha.strftime("%A") == 'Saturday':
			return "Sábado"

	def save(self, *args, **kwargs):
		self.dia = self.translate()
		super(Asistencias,self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('detail-asistencia', args=[str(self.id)])

	def get_url_update(self):
		return reverse('update-asistencia', args=[str(self.id)])

	def get_url_delete(self):
		return reverse('delete-asistencia', args=[str(self.id)])

class Inasistencias(models.Model):
	empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
	fecha = models.DateField(null=True, blank=True)
	dia = models.CharField(max_length=10,blank=True, null=True)
	justificativo = models.ImageField(upload_to='media/',null=True, blank=True)
	motivo = models.CharField(max_length=40,null=True, blank=True)

	class Meta:
		db_table='inasistencias'
	
	def translate(self):
		if self.fecha.strftime("%A") == 'Monday':
			return "Lunes"

		if self.fecha.strftime("%A") == 'Tuesday':
			return "Martes"

		if self.fecha.strftime("%A") == 'Wednesday':
			return "Miercoles"

		if self.fecha.strftime("%A") == 'Tuesday':
			return "Jueves"

		if self.fecha.strftime("%A") == 'Friday':
			return "Viernes"

		if self.fecha.strftime("%A") == 'Sunday':
			return "Domingo"

		if self.fecha.strftime("%A") == 'Saturday':
			return "Sábado"


	def save(self, *args, **kwargs):
		self.dia = self.translate()
		super(Inasistencias,self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('detail-inasistencia', args=[str(self.id)])

	def get_url_update(self):
		return reverse('update-inasistencia', args=[str(self.id)])

	def get_url_delete(self):
		return reverse('delete-inasistencia', args=[str(self.id)])
