from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Categoria, Post

# Register your models here.
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre', 'fecha_creacion']
    list_display = ('nombre','estado', 'fecha_creacion')
    resource_class = CategoriaResource

admin.site.register(Categoria, CategoriaAdmin)


class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo', 'autor', 'categoria']
    list_display = ('titulo', 'autor', 'categoria', 'estado', 'fecha_creacion')
    resource_class = PostResource

admin.site.register(Post, PostAdmin)