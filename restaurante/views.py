from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm
# Create your views here.

def crear_pedidos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        print("Datos del formulario:", request.POST)  # Imprimir los datos enviados
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto created successfully!')
            return redirect('listar_pedidos', 'ver_factura')
        else:
            # Imprimir errores de validación
            print("Errores de validación:", form.errors)
    else:
        form = ProductoForm()
    return render(request, 'pedidos/crear_pedidos.html', {'form': form})

def listar_pedidos(request):
    productos = Producto.objects.all().order_by('-created_at')
    return render(request, 'pedidos/listar_pedidos.html', {'productos': productos})

def ver_factura(request):
    productos = Producto.objects.all().order_by('-created_at')
    return render(request, 'pedidos/ver_factura.html', {'productos': productos})