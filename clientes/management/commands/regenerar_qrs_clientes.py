# clientes/management/commands/regenerar_qrs_clientes.py
from django.core.management.base import BaseCommand
from clientes.models import Cliente

class Command(BaseCommand):
    help = "Regenera los códigos QR de todos los clientes con la URL actual."

    def handle(self, *args, **kwargs):
        clientes = Cliente.objects.all()
        total = clientes.count()

        for i, cliente in enumerate(clientes, start=1):
            cliente.save()  # Esto regenera el QR usando la lógica en models.py
            self.stdout.write(f"[{i}/{total}] QR actualizado para: {cliente}")

        self.stdout.write(self.style.SUCCESS("✅ Todos los QRs fueron regenerados con la URL actual."))
