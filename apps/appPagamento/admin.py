from django.contrib import admin

from .models import EncomendarProduto, EndecEnvio, Pedido

admin.site.register(EndecEnvio)
admin.site.register(Pedido)
admin.site.register(EncomendarProduto)
# Register your models here.
