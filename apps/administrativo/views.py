from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 
from django.views.generic import*
from django.views.generic.edit import*
from django.views.generic.detail import*
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .forms import*
from .models import*
from datetime import date
#from django.views.generic.dates import MonthArchiveView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CreateUserView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
	model= User
	permission_required = ('auth.add_user')
	form_class = UserCreationForm
	template_name="add_user.html"
	success_url= reverse_lazy('list-user')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			messages.success(self.request,_('Usuario registrado...'))
			return HttpResponseRedirect(self.get_success_url())
		else:
			messages.error(self.request,_('¡Datos invalidos!'))
			return render(self.request, self.template_name, {'form':self.form_class})

class ListUserView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
	model=User
	permission_required=('auth.view_user')
	#fields='__all__'
	template_name='lista_usuarios.html'
	context_object_name='user_list'

class UpdateUserView(LoginRequiredMixin,SuccessMessageMixin,PermissionRequiredMixin,UpdateView):
	model = User
	permission_required=('auth.change_user')
	form_class= UserChangeForm
	template_name = 'update_user.html'
	success_url = reverse_lazy('list-user')
	success_message=_('Datos actualizados...')

class AsistenciasCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
	model=Asistencias
	permission_required=('administrativo.add_asistencias')
	form_class=AsistenciaForm
	template_name='registro_asistencia.html'
	context_object_name='asistencia'
	success_url=reverse_lazy('list-empleado')
	

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form=self.form_class(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,_('Asistencia registrada...'))
			return HttpResponseRedirect(self.get_success_url())
			
		else:
			messages.error(request, _('Datos invalidos'))
			return render(self.request, self.template_name, {'form':self.form_class})

			 
				
class InasistenciasCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
	model=Inasistencias
	permission_required=('administrativo.add_inasistencias')
	form_class=InasistenciaForm
	template_name='registro_inasistencias.html'
	context_object_name='inasistencia'
	success_url=reverse_lazy('list-empleado')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form=self.form_class(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,_('Inasistencia registrada...'))
			return HttpResponseRedirect(self.get_success_url())
		else:
			messages.error(request, _('Datos invalidos'))
			return HttpResponseRedirect(reverse_lazy('list-empleado'))

class EmpleadosCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
	model=Empleados
	permission_required=('administrativo.add_empleados')
	form_class=EmpleadoForm
	template_name='registro_empleado.html'
	context_object_name='empleado'
	success_url=reverse_lazy('list-empleado')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form=self.form_class(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,_('Empleado registrado...'))
			return HttpResponseRedirect(self.get_success_url())
		else:
			messages.error(request, _('Datos invalidos'))
			return render(self.request, self.template_name, {'form':self.form_class})


class EmpleadoUpdateView(LoginRequiredMixin,SuccessMessageMixin,PermissionRequiredMixin,UpdateView):
	model=Empleados
	permission_required=('administrativo.change_empleados')
	form_class=EmpleadoForm
	template_name='registro_empleado.html'
	context_object_name='empleado'
	success_url=reverse_lazy('list-empleado')
	success_message=_('Datos de empleado actualizados')

class AsistenciaUpdateView(LoginRequiredMixin,SuccessMessageMixin,PermissionRequiredMixin,UpdateView):
	model=Asistencias
	permission_required=('administrativo.change_asistencias')
	form_class=AsistenciaForm
	template_name='registro_asistencia.html'
	context_object_name='asistencia'
	success_url=reverse_lazy('list-empleado')
	success_message=_('Datos de asistencia actualizados...')

class InasistenciaUpdateView(LoginRequiredMixin,SuccessMessageMixin,PermissionRequiredMixin,UpdateView):
	model=Inasistencias
	permission_required=('administrativo.change_inasistencias')
	form_class=InasistenciaForm
	template_name='registro_inasistencias.html'
	context_object_name='inasistencia'
	success_url=reverse_lazy('list-empleado')
	success_message=_('Datos inasistencia actualizados')


class AsistenciaDeleteView(LoginRequiredMixin,SuccessMessageMixin,PermissionRequiredMixin,DeleteView):
	model = Asistencias
	permission_required=('administrativo.delete_asistencias')
	template_name='eliminar_asistencia.html'
	context_object_name='asistencia'
	success_url= reverse_lazy('list-empleado')
	success_message= _('Registro eliminado...')

class InasistenciaDeleteView(LoginRequiredMixin,SuccessMessageMixin,PermissionRequiredMixin,DeleteView):
	model= Inasistencias
	permission_required=('administrativo.delete_inasistencias')
	template_name='eliminar_inasistencias.html'
	context_object_name='inasistencia'
	success_url= reverse_lazy('list-empleado')
	success_message= _('Registro eliminado...')

class EmpleadoDeleteView(LoginRequiredMixin,SuccessMessageMixin,PermissionRequiredMixin,DeleteView):
	model = Empleados
	permission_required=('administrativo.delete_empleados')
	template_name='eliminar_empleado.html'
	context_object_name='empleado'
	success_url= reverse_lazy('list-empleado')
	success_message = _('Registro eliminado...')

class ReporteAsistencias(LoginRequiredMixin,SingleObjectMixin,PermissionRequiredMixin, ListView):
	template_name='reporte_asistencia.html'
	permission_required=('administrativo.view_asistencias','administrativo.view_inasistencias')
	paginate_by=32

	def get(self, request, *args, **kwargs):
		self.object = self.get_object(queryset=Empleados.objects.all())
		return super(ReporteAsistencias,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['empleado']=self.object
		context['inasistencia'] = self.object.inasistencias_set.all().order_by('id')[:15]
		context['fecha_hoy']=date.today()
		return context

	def get_queryset(self):
		return self.object.asistencias_set.all().order_by('id')[:15]

class AsistenciasListView(LoginRequiredMixin,SingleObjectMixin,PermissionRequiredMixin,ListView):
	template_name='lista_asistencias.html'
	permission_required=('administrativo.view_asistencias','administrativo.view_inasistencias')
	paginate_by=10
	dato = date.today()
	mes = dato.strftime("%m")

	def get(self, request,*args, **kwargs):
		self.object = self.get_object(queryset=Empleados.objects.all().filter(rol__exact='Encargado(a) del CBIT'))
		return super(AsistenciasListView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['empleado'] = self.object
		context['inasistencias'] = self.object.inasistencias_set.all().order_by('-fecha')
		return context

	def get_queryset(self):
		return self.object.asistencias_set.filter(fecha__month=self.mes)		

class EmpleadoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
	queryset= Empleados.objects.only('nombre','apellido','cedula','rol').filter(rol__exact='Encargado(a) del CBIT').order_by('id')
	permission_required=('administrativo.view_empleados')
	context_object_name='empleado'
	template_name='lista_empleados.html'
	paginate_by=10
