from django import forms
from .models import*

class EquiposForm(forms.ModelForm):
	class Meta:
		model=Equipos
		fields=['cbit','serial','modelo','descripcion','observacion',
				'tipo_de_bien','fundacion','marca','estado_uso','estado_fisico',
				'tipo_equipo']

		widgets={'cbit':forms.Select(attrs={'class':'form-control'}),
				 'serial': forms.TextInput(attrs={'class':'form-control'}),
				 'modelo': forms.TextInput(attrs={'class':'form-control'}),
				 'descripcion':forms.TextInput(attrs={'class':'form-control'}),
				 'observacion':forms.TextInput(attrs={'class':'form-control'}),
				 'tipo_de_bien': forms.TextInput(attrs={'class':'form-control'}),
				 'fundacion':forms.TextInput(attrs={'class':'form-control'}),
				 'marca':forms.Select(attrs={'class':'form-control'}),
				 'estado_uso':forms.Select(attrs={'class':'form-control'}),
				 'estado_fisico':forms.Select(attrs={'class':'form-control'}),
				 'tipo_equipo':forms.Select(attrs={'class':'form-control'})}