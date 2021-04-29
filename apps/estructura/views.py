from django.shortcuts import render
from django.views.generic import*
from django.views.generic.edit import*
from django.views.generic.detail import*
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import*
from .models import*
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 
from django.utils.translation import ugettext_lazy as _

class PlantelesCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
	model=Planteles
	permission_required=('estructura.add_planteles')
	form_class=PlantelForm
	context_object_name='plantel'
	template_name='registrar_plantel.html'
	success_url=reverse_lazy('list-plantel')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form=self.form_class(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, _('Plantel registrado exitosamente...'))
			return HttpResponseRedirect(self.get_success_url())
		else:
			messages.error(request, _('Datos invalidos...'))
			return render(self.request, self.template_name, {'form':self.form_class})


class CBITCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
	model=CBITS
	permission_required=('estructura.add_cbits')
	form_class=CBITForm
	template_name='registrar_cbit.html'
	success_url=reverse_lazy('list-cbit')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form=self.form_class(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, _('CBIT registrado exitosamente...'))
			return HttpResponseRedirect(self.get_success_url())
		else:
			messages.error(request, _('Datos invalidos'))
			return render(self.request, self.template_name, {'form':self.form_class})

class DireccionCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
	model = Direccion
	permission_required=('estructura.add_direccion')
	template_name='crear_direccion.html'
	success_url=reverse_lazy('add-plantel')
	form_class=DireccionForm

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form=self.form_class(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, _('Dirección registrada exitosamente...'))
			return HttpResponseRedirect(self.get_success_url())
		else:
			messages.error(request,_('Datos invalidos...'))
			return render(self.request, self.template_name, {'form':self.form_class})

class CBITDetailView(DetailView,PermissionRequiredMixin):
	queryset= CBITS.objects.only('nombre', 'empleado').order_by('id')
	template_name='detalles_cbit.html'
	permission_required=('estructura.view_cbits')
	context_object_name='cbit' 

class CBITUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
	model=CBITS
	permission_required=('estructura.change_cbits')
	form_class=CBITForm
	template_name='registrar_cbit.html'
	success_url=reverse_lazy('list-cbit')
	success_message = _('Datos del cbit actualizados...')


class DireccionUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
	model=Direccion
	permission_required=('estructura.change_direccion')
	form_class=DireccionForm
	template_name='crear_direccion.html'
	success_url=reverse_lazy('list-direccion')
	success_message=_('Datos de dirección actualizados...')

class CBITDeleteView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
	model=CBITS
	permission_required=('estructura.delete_cbits')
	context_object_name='cbit'
	template_name='eliminar_cbit.html'
	success_url=reverse_lazy('list-cbit')
	success_message = _('Registro eliminado...')


class PlantelUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
	model=Planteles
	form_class=PlantelForm
	context_object_name="plantel"
	permission_required=('estructura.change_planteles')
	template_name='registrar_plantel.html'
	success_url=reverse_lazy('list-plantel')
	success_message=_('Datos del plantel actualizados...')
	
class PlantelListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
	queryset=Planteles.objects.only('empleado','codigo_DEA','nombre_circuito','nivel_academico').order_by('id')
	context_object_name='plantel'
	permission_required=('estructura.view_planteles')
	template_name='lista_planteles.html'
	paginate_by=10


class DireccionListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
	queryset=Direccion.objects.only('id').order_by('id')
	context_object_name='direccion'
	permission_required=('estructura.view_direccion')
	template_name='lista_direcciones.html'
	paginate_by=10

class CBITListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
	queryset = CBITS.objects.only('nombre', 'empleado').order_by('id')
	template_name='lista_cbit.html'
	permission_required=('estructura.view_cbits')
	paginate_by=10
	context_object_name = 'cbits'


class PlantelDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
	model=Planteles
	permission_required=('estructura.view_planteles')
	context_object_name='plantel'
	template_name='detalles_plantel.html'

class PlantelDeleteView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
	model=Planteles
	permission_required=('estructura.delete_planteles')
	context_object_name='plantel'
	template_name='eliminar_plantel.html'
	success_url=reverse_lazy('list-plantel')
	success_message = _('Registro eliminado...')

class ReporteEquipo(LoginRequiredMixin,SingleObjectMixin,PermissionRequiredMixin,ListView):
	template_name='reporte_equipos.html'
	paginate_by=10
	permission_required=('tecnico.view_equipos')

	def get(self,request,*args,**kwargs):
		self.object = self.get_object(queryset=CBITS.objects.all())
		return super(ReporteEquipo,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		context = super(ReporteEquipo,self).get_context_data(**kwargs)
		context['equipos'] =self.object
		context['equipos_danados'] = self.object.equipos_set.filter(estado_fisico='MALO').count()
		context['ubicacion'] = self.object
		return context

	def get_queryset(self):
		return self.object.equipos_set.all().order_by('id')


class EquipoListView(LoginRequiredMixin,SingleObjectMixin,PermissionRequiredMixin,ListView):
	template_name='lista_equipos.html'
	paginate_by=10
	permission_required=('tecnico.view_equipos')

	def get(self,request,*args,**kwargs):
		self.object = self.get_object(queryset=CBITS.objects.all())
		return super().get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context= super().get_context_data(*kwargs)
		context['cbit'] = self.object
		return context

	def get_queryset(self):
		return self.object.equipos_set.only('modelo','descripcion','serial','marca','estado_fisico','estado_uso').order_by('id')


class ReporteEquipoMalo(LoginRequiredMixin,SingleObjectMixin,PermissionRequiredMixin,ListView):
	template_name='reporte_equipos_malos.html'
	paginate_by=10
	permission_required=('tecnico.view_equipos')

	def get(self,request,*args,**kwargs):
		self.object = self.get_object(queryset=CBITS.objects.all())
		return super(ReporteEquipoMalo,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		context = super(ReporteEquipoMalo,self).get_context_data(**kwargs)
		context['equipos'] = self.object
		context['ubicacion'] = self.object
		return context

	def get_queryset(self):
		return self.object.equipos_set.only('modelo','descripcion','serial','marca','estado_fisico','estado_uso').filter(estado_fisico='MALO').order_by('id')
