from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from apps.appLoja.models import Produto

from .carrinho import carrinhoClass

def carrinhoVisualizar(request):

    carrinho = carrinhoClass(request)

    produtos_carrinho = carrinho.obter_produto

    quantidades = carrinho.obter_quantidade

    total = carrinho.total()

    return render(request, 'carrinhoVisualizar.html', {"produtos_carrinho":produtos_carrinho, "quantidades": quantidades, "total": total})

def carrinhoRemover(request):

    carrinho = carrinhoClass(request)

    if request.POST.get('action') == 'post':

        produtoID = int(request.POST.get('produtoID'))

        carrinho.remover(produto=produtoID)

        response = JsonResponse({'produto':produtoID})

        return response


def carrinhoAtualizar(request):

    carrinho = carrinhoClass(request)

    if request.POST.get('action') == 'post':

        produtoID = int(request.POST.get('produtoID'))

        produtoQTD = int(request.POST.get('produtoQTD'))

        carrinho.atualizar(produto=produtoID, quantidade=produtoQTD)

        response = JsonResponse({'quantidade':produtoQTD})

        return response

def carrinhoAdicionar(request):

    carrinho = carrinhoClass(request)

    if request.POST.get('action') == 'post':

        produtoID = int(request.POST.get('produtoID'))

        produtoQTD = int(request.POST.get('produtoQTD'))

        produto = get_object_or_404(Produto, id=produtoID)

        carrinho.adicionar(produto=produto, quantidade=produtoQTD)

        carrinhoNum = carrinho.__len__()

        response = JsonResponse({'Quantidade': carrinhoNum})
        return response