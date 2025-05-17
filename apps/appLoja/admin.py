from django.contrib import admin

from django.contrib.auth.models import User

from .models import Cliente, Produto, Categoria, Pedido, Perfil

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Pedido)
admin.site.register(Perfil)

class PerfilUser(admin.StackedInline):

    model = Perfil

class AdminUser(admin.ModelAdmin):

    model = User

    fields = ["username", "first_name", "last_name", "email"]
    inlines = [PerfilUser]

admin.site.unregister(User)

admin.site.register(User, AdminUser)