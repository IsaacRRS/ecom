from django.urls import path
from . import views

urlpatterns = [

    path('', views.carrinhoVisualizar, name="carrinhoVisualizar"),
    path('remover', views.carrinhoRemover, name="carrinhoRemover"),
    path('atualizar', views.carrinhoAtualizar, name="carrinhoAtualizar"),
    path('adicionar/', views.carrinhoAdicionar, name="carrinhoAdicionar"),

]
