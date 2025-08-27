from django.contrib import admin
from django.urls import path, include  # include para las rutas de apps
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),  # todas las rutas de la app clientes aquí
]

# Para servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
