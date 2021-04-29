from django import forms
from .models import*
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import  datetime


class PlantelForm(forms.ModelForm):
	class Meta:
		model=Planteles

		attrs={'class':'form-control'}

		fields=['direccion',
		'empleado','codigo_DEA',
		'matricula_est','docentes',
		'nivel_academico',
		'dependencia',
		'telefono', 
		'nombre_circuito',
		'anno_fundacion', 
		'cantidad_aulas']

		widgets={'direccion': forms.Select(attrs),
		'empleado':forms.Select(attrs),
		'codigo_DEA':forms.TextInput(attrs),
		'matricula_est':forms.TextInput(attrs),
		'docentes':forms.TextInput(attrs),
		'nivel_academico':forms.TextInput(attrs),
		'dependencia':forms.TextInput(attrs),
		'telefono':forms.TextInput(attrs),
		'nombre_circuito':forms.TextInput(attrs),
		'anno_fundacion':forms.TextInput(attrs),
		'cantidad_aulas':forms.TextInput(attrs)}

class CBITForm(forms.ModelForm):
	class Meta:
		model=CBITS
		attrs={'class':'form-control'}
		fields=['plantel','empleado','internet','nombre']

		widgets={'plantel':forms.Select(attrs={'class':'form-control','placeholder':'Plantel'}),
		'empleado':forms.Select(attrs),
		'internet':forms.Select(attrs),
		'nombre':forms.TextInput(attrs)}

	def validate_even():
		pass

class DireccionForm(forms.ModelForm):
	class Meta:
		model=Direccion

		attrs={'class':'form-control'}
		fields=['estado','municipio','parroquia','comuna','avenida','sector','punto_referencia']

		widgets={'estado':forms.TextInput(attrs),
				 'municipio':forms.TextInput(attrs),
				 'parroquia':forms.TextInput(attrs),
				 'comuna':forms.TextInput(attrs),
				 'avenida':forms.TextInput(attrs),
				 'sector':forms.TextInput(attrs),
				 'punto_referencia':forms.TextInput(attrs)}
