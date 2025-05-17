from .carrinho import carrinhoClass

def carrinho(request):

    return {'carrinho': carrinhoClass(request)}