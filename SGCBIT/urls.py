from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from SGCBIT.index import Index
from apps.administrativo.urls import*
from apps.tecnico import views
from apps.administrativo import views
from apps.estructura.urls import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'),name='login'),
    path('sgcbit',Index, name='index'),
    path('sgcbit/', include('apps.administrativo.urls')),
    path('sgcbit/', include('apps.tecnico.urls')),
    path('sgcbit/', include('apps.estructura.urls'))
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
