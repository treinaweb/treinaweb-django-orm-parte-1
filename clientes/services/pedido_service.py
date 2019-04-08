from ..models import Pedido

def cadastrar_pedido(pedido):
    Pedido.objects.create(cliente=pedido.cliente, data_pedido=pedido.data_pedido, valor=pedido.valor,
                          status=pedido.status, observacoes=pedido.observacoes)


def listar_pedidos():
    pedidos = Pedido.objects.all()
    return pedidos

def editar_pedido(pedido, pedido_novo):
    pedido.cliente = pedido_novo.cliente
    pedido.observacoes = pedido_novo.observacoes
    pedido.data_pedido = pedido_novo.data_pedido
    pedido.valor = pedido_novo.valor
    pedido.status = pedido_novo.status
    pedido.save(force_update=True)

def listar_pedido_id(id):
    pedido = Pedido.objects.get(id=id)
    return pedido