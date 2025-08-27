from django.contrib import admin
from django.utils.html import format_html
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('mostrar_qr',)  # Solo lectura en el formulario

    # Mostramos el QR directamente en la lista
    list_display = ('nombre_empresa', 'nit', 'mostrar_qr')

    def mostrar_qr(self, obj):
        if obj.qr_image:
            return format_html('<img src="{}" width="80" />', obj.qr_image.url)
        return "No generado"

    mostrar_qr.short_description = "Código QR"
