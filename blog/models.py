from django.db import models
from ckeditor.fields import RichTextField
from autores.models import Autor
from django.utils.text import slugify

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField('Nombre de la Categoría', max_length = 100, null = True, blank = False)
    estado = models.BooleanField('Activada/No activada', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
    

class Post(models.Model):
    titulo = models.CharField('Titulo', max_length = 90, null = False, blank = False)
    slug = models.SlugField('Slug', unique = True, null = True, blank = True)
    descripcion = models.CharField('Descripción', max_length = 110, null = False, blank = False)
    contenido = RichTextField('Contenido', null = False, blank = False)
    imagen = models.ImageField('Imagen', null = True, blank = True)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No publicado', default = True)
    fecha_creacion = models.DateField('Feacha de creación', auto_now = False, auto_now_add = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo
