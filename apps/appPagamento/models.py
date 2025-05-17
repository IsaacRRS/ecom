from django.db import models

from django.contrib.auth.models import User

from apps.appLoja.models import Produto

class EndecEnvio(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_completo = models.CharField(max_length=255)

    endec1 = models.CharField(max_length=255)
    endec2 = models.CharField(max_length=255, null=True, blank=True)
    
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255, null=True, blank=True)

    cod_postal = models.CharField(max_length=255, null=True, blank=True)

    class Meta:

        verbose_name_plural = 'Endereços de Envio'

    def __str__(self):

        return f'Endereço de envio - {str(self.id)}'
    

class Pedido(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    envio_endec = models.TextField(max_length=500)

    total_pago = models.DecimalField(max_digits=12, decimal_places=2)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido - {str(self.id)}'
    

class EncomendarProduto(models.Model):

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    quantidade = models.PositiveBigIntegerField(default=1)
    preco = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:

        verbose_name_plural = 'Encomenda de Produtos'

    def __str__(self):
        return f'Encomendar Produto - {str(self.id)}'