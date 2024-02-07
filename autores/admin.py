from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Autor

# Register your models here.

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor
    
class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'email']
    list_display = ('nombres', 'apellidos', 'email', 'estado')
    resource_class = AutorResource

admin.site.register(Autor, AutorAdmin)
