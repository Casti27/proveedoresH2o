from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm


def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente_detalle', pk=cliente.pk)  # redirige al detalle
    else:
        form = ClienteForm()
    return render(request, 'clientes/crear_cliente.html', {'form': form})


def cliente_detalle(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    # Validar si hay archivo cargado antes de enviar al template
    archivo = cliente.camara_comercio.url if cliente.camara_comercio else None

    return render(request, 'clientes/detalle.html', {
        'cliente': cliente,
        'archivo': archivo
    })
