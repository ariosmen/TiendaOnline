from django.contrib import admin
from blog.models import Categoria, Post

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)