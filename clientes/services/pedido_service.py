from ..models import Pedido

def cadastrar_pedido(pedido):
    Pedido.objects.create(cliente=pedido.cliente, data_pedido=pedido.data_pedido, valor=pedido.valor,
                          status=pedido.status, observacoes=pedido.observacoes)


def listar_pedidos():
    pedidos = Pedido.objects.all()
    return pedidos