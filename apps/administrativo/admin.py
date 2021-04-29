from django.contrib import admin
from apps.administrativo.models import Empleados
# Register your models here.

class EmpleadosAdmin(admin.ModelAdmin):
	model = Empleados

admin.site.register(Empleados, EmpleadosAdmin)