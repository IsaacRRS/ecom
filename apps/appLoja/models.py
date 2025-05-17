from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User

import datetime

class Categoria(models.Model):

    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:

        verbose_name_plural = 'categorias'
    

class Cliente(models.Model):

    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    senha = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    celular = models.CharField(max_length=14)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Perfil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dia_modif = models.DateTimeField(User, auto_now=True)
    celular = models.CharField(max_length=14, blank=True)

    endec1 = models.CharField(max_length=200, blank=True)
    endec2 = models.CharField(max_length=200, blank=True)
    cidade = models.CharField(max_length=200, blank=True)
    estado = models.CharField(max_length=200, blank=True)
    cod_postal = models.CharField(max_length=200, blank=True)

    persiste_carrinho = models.CharField(max_length=200, blank=True, null=True)

    class Meta:

        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.user.username
    
def criar_perfil(sender, instance, created, **kwargs):

    if created:

        perfil_user = Perfil(user=instance)

        perfil_user.save()

post_save.connect(criar_perfil, sender=User)


class Produto(models.Model):

    nome = models.CharField(max_length=120)
    preco = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    imagem = models.ImageField(upload_to='uploads/produto/')
    desc = models.CharField(max_length=320, default='', blank=True, null=True)

    def __str__(self):
        return self.nome
    
    descontoPrec = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    desconto = models.BooleanField(default=False)

class Pedido(models.Model):

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    enderec = models.CharField(max_length=120, default='', blank=True)
    data = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    quantidade = models.IntegerField(default=1)
    celular = models.CharField(max_length=14, default='', blank=True)
                    
    def __str__(self):
        return self.produto