from clientes.forms.produto_forms import ProdutoForm
from ..entidades.produto import Produto
from ..services import produto_service

from django.shortcuts import render

def listar_produtos(request):
    produtos = produto_service.listar_produtos()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def inserir_produto(request):
    if request.method == "POST":
        form_produto = ProdutoForm(request.POST)
        if form_produto.is_valid():
            nome = form_produto.cleaned_data["nome"]
            descricao = form_produto.cleaned_data["descricao"]
            valor = form_produto.cleaned_data["valor"]
            produto_novo = Produto(nome=nome, descricao=descricao, valor=valor)
            produto_service.inserir_produto(produto_novo)
    else:
        form_produto = ProdutoForm()
    return render(request, 'produtos/form_produto.html', {'form_produto':form_produto})