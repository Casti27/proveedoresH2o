from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView  # 👈 importa esto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/cliente/nuevo/')),  # 👈 redirige la raíz
    path('cliente/', include('clientes.urls')),  # 👈 incluye las rutas de la app
]

# Archivos media (solo en desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
