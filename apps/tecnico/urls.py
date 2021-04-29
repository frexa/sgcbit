from django.urls import path, include
from .views import*

urlpatterns=[path('add/equipo', EquipoCreateView.as_view(), name='add-equipo'),
			 path('update/equipo/<int:pk>',EquipoUpdateView.as_view(),name='update-equipo'),
			 path('delete/equipo/<int:pk>', EquipoDeleteView.as_view(), name='delete-equipo')]