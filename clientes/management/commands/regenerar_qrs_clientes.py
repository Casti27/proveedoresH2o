from django.db import models
from django.conf import settings
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
import os

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    qr_code = models.ImageField(upload_to="qrs/", blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # guarda primero el objeto

        # Generar URL actual
        url = f"{settings.SITE_URL}/cliente/{self.pk}/"

        # Generar QR
        qr = qrcode.make(url)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")

        # Nombre fijo para este cliente (se sobrescribe siempre)
        filename = f"qrs/qr_{self.pk}.png"

        # Si ya existe, eliminarlo antes de sobrescribir
        if self.qr_code and os.path.isfile(self.qr_code.path):
            os.remove(self.qr_code.path)

        # Guardar el QR en el mismo nombre
        self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)

        super().save(update_fields=["qr_code"])
