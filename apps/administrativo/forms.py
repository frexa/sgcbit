from django import forms
from datetime import date
from .models import*
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class EmpleadoForm(forms.ModelForm):
	def clean(self):
		msg = '¡No puedes ingresar numeros este campo es solo alfabetico!'
		msg2 = '¡No puedes ingresar letras este campo es solo numerico!'

		nombre = self.cleaned_data.get("nombre")
		apellido = self.cleaned_data.get("apellido")
		cadula = self.cleaned_data.get("cedula")
		celular = self.cleaned_data.get("celular")

		if nombre.isdigit() or apellido.isdigit():
			raise ValidationError(_(msg))

		if cedula.isalpha() or celular.isalpha():
			raise ValidationError(_(msg2))

	
	class Meta:
		model=Empleados

		attrs={'class':'form-control','autofocus':True}

		fields=['rol', 'cedula', 'nombre', 'apellido','correo','celular']

		widgets={'rol':forms.Select(attrs),
				 'cedula':forms.TextInput(attrs),
				 'nombre':forms.TextInput(attrs),
				 'apellido':forms.TextInput(attrs),
				 'correo':forms.TextInput(attrs),
				 'celular':forms.TextInput(attrs)}

class AsistenciaForm(forms.ModelForm):
	def clean(self):
		msg ='¡No puedes agregar asistencias de fin de semana!'
		dia = self.cleaned_data.get("fecha")
		if dia.strftime("%A") == 'Sunday':
			raise ValidationError(_(msg))

		if dia.strftime("%A") == 'Saturday':
			raise ValidationError(_(msg))

		if dia > date.today():
			raise ValidationError(_('¡Error no puedes marcar asistencias futuras!'))

		if dia < date.today():
			raise ValidationError(_('¡Error no puedes marcar asistencias pasadas!'))

	class Meta:
		model=Asistencias

		fields=['empleado','fecha','hora_entrada', 'hora_salida',
		 'observacion' ,'actividad', 'dia']
		
		widgets={'empleado': forms.Select(attrs={'class':'form-control'}),
		 		 'fecha':forms.DateInput(attrs={'class':'form-control','data-target':'#fecha'}),
		 		 'hora_entrada':forms.TimeInput(attrs={'class':'form-control','data-target':'#hora'}),
		 		 'hora_salida':forms.TimeInput(attrs={'class':'form-control','data-target':'#hora'}),
		 		 'observacion':forms.TextInput(attrs={'class':'form-control'}),
		 		 'actividad':forms.TextInput(attrs={'class':'form-control'})}

class InasistenciaForm(forms.ModelForm):

	def clean(self):
		msg ='¡No puedes agregar inasistencias de fin de semana!'
		dia = self.cleaned_data.get("fecha")
		if dia.strftime("%A") == 'Sunday':
			raise ValidationError(_(msg))

		if dia.strftime("%A") == 'Saturday':
			raise ValidationError(_(msg))

		if dia > date.today():
			raise ValidationError(_('¡Error no puedes marcar asistencias futuras!'))

		if dia < date.today():
			raise ValidationError(_('¡Error no puedes marcar asistencias pasadas!'))

	class Meta:
		model=Inasistencias
		fields=['empleado','fecha','justificativo','motivo']

		widgets={
				'empleado':forms.Select(attrs={'class':'form-control'}),
				'fecha':forms.DateInput(attrs={'class':'form-control','data-target':'#fecha'}),
				'justificativo':forms.FileInput(attrs={'class':'form-control'}),
				'motivo':forms.TextInput(attrs={'class':'form-control'})}