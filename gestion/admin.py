from django.contrib import admin
from gestion.models import Cliente, Articulo, Pedido

class ClienteAdmin(admin.ModelAdmin):
    pass

class ArticuloAdmin(admin.ModelAdmin):
    pass

class PedidoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Pedido, PedidoAdmin)