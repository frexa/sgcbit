from django.contrib import admin
from apps.estructura.models import Planteles, INTERNET, Direccion, CBITS
# Register your models here.

class PlantelesAdmin(admin.ModelAdmin):
	model= Planteles

class DireccionAdmin(admin.ModelAdmin):
	model= Direccion

class INTERNETADMIN(admin.ModelAdmin):
	model = INTERNET

class CBITSAdmin(admin.ModelAdmin):
	model = CBITS

admin.site.register(CBITS, CBITSAdmin)
admin.site.register(Planteles, PlantelesAdmin)
admin.site.register(Direccion, DireccionAdmin)
admin.site.register(INTERNET, INTERNETADMIN)
