from ..models import Produto

def inserir_produto(produto):
    Produto.objects.create(nome=produto.nome, descricao=produto.descricao, valor=produto.valor)
