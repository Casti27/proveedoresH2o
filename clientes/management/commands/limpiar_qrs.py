from django.core.management.base import BaseCommand
from django.conf import settings
from clientes.models import Cliente
import os
import glob

class Command(BaseCommand):
    help = "Elimina QR antiguos y regenera los actuales para que no se acumulen."

    def handle(self, *args, **kwargs):
        qr_dir = os.path.join(settings.MEDIA_ROOT, 'qrcodes')

        # 🔥 1. Borrar todos los PNG de la carpeta qrcodes/
        self.stdout.write("🗑️ Eliminando archivos viejos en qrcodes/ ...")
        for file in glob.glob(os.path.join(qr_dir, "*.png")):
            os.remove(file)

        # 🔄 2. Regenerar QR para todos los clientes
        self.stdout.write("🔄 Regenerando códigos QR...")
        for cliente in Cliente.objects.all():
            cliente.save()  # fuerza regeneración del QR

        self.stdout.write(self.style.SUCCESS("✅ Limpieza completada. QR regenerados."))
