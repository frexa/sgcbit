from django.urls import path, include
from .views import*

patterns_add_object=[path('asistencia',AsistenciasCreateView.as_view(),name='add-asistencia'),
					 path('inasistencia',InasistenciasCreateView.as_view(),name='add-inasistencia'),
					 path('empleado',EmpleadosCreateView.as_view(),name='add-empleado'),
					 path('user',CreateUserView.as_view(),name='add-user')]

patterns_update_object=[path('asistencia/<int:pk>',AsistenciaUpdateView.as_view(),name='update-asistencia'),
					    path('inasistencia/<int:pk>',InasistenciaUpdateView.as_view(),name='update-inasistencia'),
					    path('empleado/<int:pk>', EmpleadoUpdateView.as_view(), name='update-empleado'),
					    path('user/<int:pk>', UpdateUserView.as_view(),name='update-user')]

patterns_delete_object=[path('asistencia/<int:pk>',AsistenciaDeleteView.as_view(),name='delete-asistencia'),
					    path('inasistencia/<int:pk>',InasistenciaDeleteView.as_view(),name='delete-inasistencia'),
					    path('empleado/<int:pk>', EmpleadoDeleteView.as_view(), name='delete-empleado')]

patterns_list_object=[path('asistencia/<int:pk>',AsistenciasListView.as_view(),name='list-asistencia'),
					  path('empleados', EmpleadoListView.as_view(), name='list-empleado'),
					  path('user',ListUserView.as_view(),name='list-user')]



urlpatterns=[
	path('add/',include(patterns_add_object)),
	path('update/',include(patterns_update_object)),
	path('delete/',include(patterns_delete_object)),
	path('list/',include(patterns_list_object)),
	path('report/asistencias/<int:pk>', ReporteAsistencias.as_view(),name='report-asistencia')
]