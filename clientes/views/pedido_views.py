from django.shortcuts import render
from ..forms import pedido_forms

def inserir_pedido(request):
    form_pedido = pedido_forms.PedidoForm()
    return render(request, 'pedidos/form_pedido.html', {'form_pedido': form_pedido})