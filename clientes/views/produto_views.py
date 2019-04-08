from clientes.forms.produto_forms import ProdutoForm

from django.shortcuts import render

def inserir_produto(request):
    form_produto = ProdutoForm()
    return render(request, 'produtos/form_produto.html', {'form_produto':form_produto})