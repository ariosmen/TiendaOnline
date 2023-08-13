from django.contrib import admin
from tienda.models import CategoriaProd, Producto

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
    readonly_fields = ('create', 'update')
    
admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)
