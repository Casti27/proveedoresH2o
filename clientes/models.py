from django.db import models
from django.core.files.base import ContentFile
from io import BytesIO
import qrcode
from django.urls import reverse
from django.conf import settings


class Cliente(models.Model):
    # Datos Empresa (obligatorios)
    nombre_empresa = models.CharField(max_length=150)
    nit = models.CharField(max_length=30)

    # Contacto Comercial (opcionales)
    contacto_comercial_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_comercial_cargo = models.CharField(max_length=100, blank=True, null=True)
    contacto_comercial_correo = models.EmailField(blank=True, null=True)
    contacto_comercial_telefono = models.CharField(max_length=20, blank=True, null=True)

    # Contacto Financiero (opcionales)
    contacto_financiero_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_financiero_cargo = models.CharField(max_length=100, blank=True, null=True)
    contacto_financiero_correo = models.EmailField(blank=True, null=True)
    contacto_financiero_telefono = models.CharField(max_length=20, blank=True, null=True)

    # Representante Legal (opcionales)
    representante_nombre = models.CharField(max_length=100, blank=True, null=True)
    
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
        ('NIT', 'NIT'),
    ]
    tipo_documento = models.CharField(
        max_length=3,
        choices=TIPO_DOCUMENTO_CHOICES,
        default='CC'
    )
    numero_documento = models.CharField(max_length=50, blank=True, null=True)
    representante_cargo = models.CharField(max_length=100, blank=True, null=True)
    representante_correo = models.EmailField(blank=True, null=True)
    representante_telefono = models.CharField(max_length=20, blank=True, null=True)

    # Referencias bancarias
    entidad_bancaria = models.CharField(max_length=100, blank=True, null=True)
    numero_cuenta = models.CharField(max_length=50, blank=True, null=True)
    sucursal = models.CharField(max_length=100, blank=True, null=True)
    telefono_banco = models.CharField(max_length=20, blank=True, null=True)
    ciudad_banco = models.CharField(max_length=100, blank=True, null=True)

    # Forma de pago
    forma_pago = models.CharField(max_length=10, choices=[('credito', 'Crédito'), ('contado', 'Contado')])
    cupo_credito = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    plazo_credito = models.PositiveIntegerField(blank=True, null=True, help_text="Días")

    # Archivos adjuntos
    rut = models.FileField(upload_to='documentos/rut/', blank=True, null=True)
    certificacion_bancaria = models.FileField(upload_to='documentos/cert_bancaria/', blank=True, null=True)
    camara_comercio = models.FileField(upload_to='documentos/camara_comercio/', blank=True, null=True)  # opcional
    representante_cedula_archivo = models.FileField(upload_to='documentos/cedulas/', blank=True, null=True)  # opcional

    # QR
    qr_image = models.ImageField(upload_to='qrcodes/', blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        relative_url = reverse('cliente_detalle', args=[self.id])
        qr_data = f"{settings.SITE_URL}{relative_url}"

        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        file_name = f'cliente_{self.id}.png'

        self.qr_image.save(file_name, ContentFile(buffer.getvalue()), save=False)

        super().save(update_fields=['qr_image'])

    def __str__(self):
        return self.nombre_empresa
