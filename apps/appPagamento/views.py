from django.shortcuts import render

from apps.appCarrinho.carrinho import carrinhoClass

from .forms import envioForm
from .models import EndecEnvio

def pagamento_sucesso(request):

    return render(request, "pagamentoSucesso.html", {})

def checkout(request):

    carrinho = carrinhoClass(request)

    produtos_carrinho = carrinho.obter_produto

    quantidades = carrinho.obter_quantidade

    total = carrinho.total()

    if request.user.is_authenticated:

        user_envio = EndecEnvio.objects.get(user__id=request.user.id)

        envio_form = envioForm(request.POST or None, instance=user_envio)

        return render(request, "checkout.html", {"produtos_carrinho":produtos_carrinho, "quantidades": quantidades, "total": total, "envio_form":envio_form})

    else:

        envio_form = envioForm(request.POST or None)

        return render(request, "checkout.html", {"produtos_carrinho":produtos_carrinho, "quantidades": quantidades, "total": total, "envio_form":envio_form})