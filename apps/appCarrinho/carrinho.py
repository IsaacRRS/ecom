from apps.appLoja.models import Perfil, Produto

class carrinhoClass():

    def __init__(self, request):
    
        self.session = request.session

        self.request = request

        carrinho = self.session.get('key_acesso')

        if 'key_acesso' not in request.session:

            carrinho = self.session['key_acesso'] = {}

        self.carrinho = carrinho


    def db_adicionar(self, produto, quantidade):

        produtoID = str(produto)

        produtoQTD = str(quantidade)

        if produtoID in self.carrinho:

            pass

        else: 

            # self.carrinho[produtoID] = {'Preço: ': str(produto.preco)}
              self.carrinho[produtoID] = int(produtoQTD)

        self.session.modified = True

        if self.request.user.is_authenticated:

            user_atual = Perfil.objects.filter(user__id=self.request.user.id)

            carrinhoPersist = str(self.carrinho)
            carrinhoPersist = carrinhoPersist.replace("\'", "\"")

            user_atual.update(persiste_carrinho=str(carrinhoPersist))


    def adicionar(self, produto, quantidade):

        produtoID = str(produto.id)

        produtoQTD = str(quantidade)

        if produtoID in self.carrinho:

            pass

        else: 

            # self.carrinho[produtoID] = {'Preço: ': str(produto.preco)}
              self.carrinho[produtoID] = int(produtoQTD)

        self.session.modified = True

        if self.request.user.is_authenticated:

            user_atual = Perfil.objects.filter(user__id=self.request.user.id)

            carrinhoPersist = str(self.carrinho)
            carrinhoPersist = carrinhoPersist.replace("\'", "\"")

            user_atual.update(persiste_carrinho=str(carrinhoPersist))

    def total(self):

        produtosID = self.carrinho.keys()

        produtos = Produto.objects.filter(id__in=produtosID)

        quantidades = self.carrinho

        total = 0

        for key, value in quantidades.items():

            key = int(key)

            for produto in produtos:

                if produto.id == key:

                    if produto.desconto:

                        total = total + (produto.descontoPrec * value)
                    
                    else:
                        
                        total = total + (produto.preco * value)

        return total

    def obter_produto(self):

        produtosID = self.carrinho.keys()

        produtos = Produto.objects.filter(id__in=produtosID)

        return produtos

    def obter_quantidade(self):

        quantidades = self.carrinho
        
        return quantidades


    def atualizar(self, produto, quantidade):

        produtoID = str(produto)
        produtoQTD = int(quantidade)

        carrinhoPessoal = self.carrinho

        carrinhoPessoal[produtoID] = produtoQTD

        self.session.modified = True

        if self.request.user.is_authenticated:

            user_atual = Perfil.objects.filter(user__id=self.request.user.id)

            carrinhoPersist = str(self.carrinho)
            carrinhoPersist = carrinhoPersist.replace("\'", "\"")

            user_atual.update(persiste_carrinho=str(carrinhoPersist))

        x = self.carrinho

        return x
    
    def remover(self, produto):

        produtoID = str(produto)

        if produtoID in self.carrinho:

            del self.carrinho[produtoID]

        self.session.modified = True

        if self.request.user.is_authenticated:

            user_atual = Perfil.objects.filter(user__id=self.request.user.id)

            carrinhoPersist = str(self.carrinho)
            carrinhoPersist = carrinhoPersist.replace("\'", "\"")

            user_atual.update(persiste_carrinho=str(carrinhoPersist))


    def __len__(self):

        return len(self.carrinho)



        