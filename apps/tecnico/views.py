from django.shortcuts import render
from .models import*
from django.views.generic import*
from django.views.generic.detail import*
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import*
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 
from django.utils.translation import ugettext_lazy as _


class EquipoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
	model=Equipos
	permission_required = ('tecnico.add_equipos')
	form_class=EquiposForm
	template_name='registrar_equipo.html'
	context_object_name='equipo'
	success_url= reverse_lazy('list-cbit')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, _('Equipo registrado exitosamente...'))
			return HttpResponseRedirect(self.get_success_url())
		else:
			messages.error(request, _('Datos invalidos...'))
			return reverse(self.request, self.template_name, {'form':self.form_class})


class EquipoUpdateView(LoginRequiredMixin,SuccessMessageMixin,PermissionRequiredMixin,UpdateView):
	model=Equipos
	permission_required=('tecnico.change_equipos')
	form_class=EquiposForm
	template_name='registrar_equipo.html'
	context_object_name='equipo'
	success_url= reverse_lazy('list-cbit')
	success_message= _('Datos del equipo actualizados...')

class EquipoDeleteView(LoginRequiredMixin,SuccessMessageMixin,PermissionRequiredMixin,DeleteView):
	model=Equipos
	permission_required=('tecnico.delete_equipos')
	template_name='eliminar_equipo.html'
	success_url=reverse_lazy('list-cbit')
	success_message= _('Registro eliminado...')