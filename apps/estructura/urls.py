from django.urls import path, include
from .views import*

urlpatterns=[path('report/equipos/<int:pk>', ReporteEquipo.as_view(),name='report-equipo'),
			path('report/equipos/malos/<int:pk>', ReporteEquipoMalo.as_view(),name='report-equipo-malo'),
			 path('add/plantel', PlantelesCreateView.as_view(), name='add-plantel'),
			 path('detail/plantel/<int:pk>', PlantelDetailView.as_view(),name='detail-plantel'),
			 path('list/planteles', PlantelListView.as_view(), name='list-plantel'),
			 path('delete/plantel/<int:pk>', PlantelDeleteView.as_view(),name='delete-plantel'),
			 path('update/plantel/<int:pk>', PlantelUpdateView.as_view(), name='update-plantel'),
			 path('add/cbit', CBITCreateView.as_view(), name='add-cbit'),
			 path('list/cbit', CBITListView.as_view(),name='list-cbit'),
			 path('update/cbit/<int:pk>',CBITUpdateView.as_view(), name='update-cbit'),
			 path('delete/cbit/<int:pk>',CBITDeleteView.as_view(), name='delete-cbit'),
			 path('detail/cbit/<int:pk>',CBITDetailView.as_view(), name='detail-cbit'),
			 path('add/direccion', DireccionCreateView.as_view(),name='add-direccion'),
			 path('update/direccion/<int:pk>', DireccionUpdateView.as_view(),name='update-direccion'),
			 path('list/direcciones', DireccionListView.as_view(),name='list-direccion'),
			 path('list/equipos/cbit/<int:pk>', EquipoListView.as_view(), name='list-equipo')]