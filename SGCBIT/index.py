from django.shortcuts import render, get_object_or_404
from apps.administrativo.models import*
from apps.estructura.models import*
from apps.tecnico.models import*
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required
def Index(request):
	template='index4.html'
	return render(request, template, {'fecha':date.today(),
		'empleados':Empleados.objects.only('id').count(),
		'planteles':Planteles.objects.only('id').count(),
		'cbit':CBITS.objects.only('id').count(),
		'direccion':Direccion.objects.only('id').count()})