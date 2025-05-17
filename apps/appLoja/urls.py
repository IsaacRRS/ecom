from django.urls import path
from . import views

urlpatterns = [

    path('produto/<int:pk>', views.produto, name='produto'),
    path('categoria/<str:cNome>', views.categoria, name='categoria'),
    path('categoriaVisualizar/', views.categoria_visualizar, name='categoria_visualizar'),
    path('buscarProduto/', views.buscar_produto, name='buscar_produto'),

    path('login/', views.entrar, name='entrar'),
    path('logout/', views.sair, name='sair'),
    path('registro/', views.registro, name='registro'),

    path('atualizarUser/', views.user_atualizar, name='user_atualizar'),
    path('atualizarSenha/', views.senha_atualizar, name='senha_atualizar'),
    path('atualizarInfo', views.info_atualizar, name='info_atualizar'),

    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),

]
