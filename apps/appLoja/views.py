from django.shortcuts import render, redirect

import json

from apps.appCarrinho.carrinho import carrinhoClass
from .models import Produto, Categoria, Perfil
from apps.appPagamento .models import EndecEnvio

from django.contrib import messages
from django.contrib.auth.models import User

from django.db.models import Q

from django.contrib.auth import authenticate, login, logout

from .forms import registroForm, atualizarForm, senhaForm, infoForm
from apps.appPagamento .forms import envioForm


######### viewSys

def entrar(request):
    
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            user_atual = Perfil.objects.get(user__id=request.user.id)

            carrinho_salvo = user_atual.persiste_carrinho

            if carrinho_salvo:

                carrinho_carregar = json.loads(carrinho_salvo)

                carrinho = carrinhoClass(request)

                for key, value in carrinho_carregar.items():

                    carrinho.db_adicionar(produto=key, quantidade=value)

            return redirect('home')
        
        else:

            return redirect('login')
        
    else: 
        
        return render(request, 'login.html', {})
   
def sair(request):

    logout(request)

    return redirect('entrar')

def registro(request):

    form = registroForm()

    if request.method == "POST":

        form = registroForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request,user)

            messages.success(request, ("Conta criada - Preencha suas informações de contato"))
            return redirect('info_atualizar')
        
        else:

            return redirect('registro')
        
    else:
    
        return render(request, 'registro.html', {'form':form})

######### viewPerfil

def user_atualizar(request):

    if request.user.is_authenticated:

        user_atual = User.objects.get(id=request.user.id)

        user_form = atualizarForm(request.POST or None, instance=user_atual)

        if user_form.is_valid():

            user_form.save()

            login(request, user_atual)

            messages.success(request, "Usuário atualizado")

            return redirect('home')
        
        return render(request, "userAtualizar.html", {'user_form':user_form})

    else:

        messages.success(request, "Você precisa estar logado")

        return redirect('home')
    
def senha_atualizar(request):

    if request.user.is_authenticated:

        user_atual = request.user

        if request.method == 'POST':

            form = senhaForm(user_atual, request.POST)

            if form.is_valid():

                form.save()

                messages.success(request, "Sua senha foi atualizada!")

                login(request, user_atual)
                
                return redirect('senha_atualizar')

            else:

                for erro in list(form.errors.values()):

                    messages.error(request, erro)

                return redirect('senha_atualizar')

        else:

            form = senhaForm(user_atual)

            return render(request, "senhaAtualizar.html", {'form':form})

    else: 

        messages.success(request, "Você deve estar logado")
        return redirect('home')
    
def info_atualizar(request):

    if request.user.is_authenticated:

        user_atual = Perfil.objects.get(user__id=request.user.id)

        user_envio = EndecEnvio.objects.get(user__id=request.user.id)

        form = infoForm(request.POST or None, instance=user_atual)
        
        envio_form = envioForm(request.POST or None, instance=user_envio)

        if form.is_valid() or envio_form.is_valid():

            form.save()
            envio_form.save()

            messages.success(request, "Informações atualizadas!")
            return redirect('home')
        
        return render(request, "infoAtualizar.html", {'form':form, 'envio_form':envio_form})

    else:

        messages.success(request, "Você precisa estar logado")
        return redirect('home')

######### viewProd & Categ

def produto(request,pk):

    produto = Produto.objects.get(id=pk)
    return render(request, 'produto.html', {'produto':produto})

def buscar_produto(request):

    if request.method == "POST":
    
        busca = request.POST['busca']

        busca = Produto.objects.filter(Q(nome__icontains=busca) | Q(desc__icontains=busca) )

        if not busca:

            messages.success(request, "Referência não encontrada")
            return render(request, "buscarProduto.html", {})
        
        else:

            return render(request, "buscarProduto.html", {'busca':busca})

    else:

        return render(request, "buscarProduto.html", {})

def categoria(request, cNome):

    try:

        categoria = Categoria.objects.get(nome=cNome)

        produtos = Produto.objects.filter(categoria=categoria)

        return render(request, 'categoria.html', {'produtos':produtos, 'categoria':categoria})

    except:

        return redirect('home')
    
def categoria_visualizar(request):

    categorias = Categoria.objects.all()

    return render(request, 'categoriaVisualizar.html', {"categorias":categorias})



######### viewTempl

def home(request):

    produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos':produtos})


def sobre(request):

    return render(request, 'sobre.html', {})