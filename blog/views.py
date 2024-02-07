from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views. generic import ListView, DetailView
from .models import Post, Categoria
from django.db.models import Q
from unidecode import unidecode
# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_aprobados'
    def get_queryset(self):
        post_aprobados = Post.objects.filter(estado = True)
        query = self.request.GET.get('buscar')
        if query:
            normalized_query = unidecode(query)
            post_aprobados = post_aprobados.filter(
                Q(titulo__icontains=normalized_query) |  # Buscar en el campo 'titulo'
                Q(descripcion__icontains=normalized_query) 
            )
        return post_aprobados


            
    
class YacimientosView(ListView):
    model = Post
    template_name = 'yacimientos.html'
    context_object_name = 'post_aprobados'
    def get_queryset(self):
        categoria_ = Categoria.objects.get(nombre = 'yacimientos')
        post_aprobados = Post.objects.filter(estado = True, categoria = categoria_)
        return post_aprobados

class PerforacionView(ListView):
    model = Post
    template_name = 'perforacion.html' 
    context_object_name = 'post_aprobados'
    def get_queryset(self):
        categoria_ = Categoria.objects.get(nombre = 'perforación')
        post_aprobados = Post.objects.filter(estado = True, categoria = categoria_)
        return post_aprobados

class ProduccionView(ListView):
    model = Post
    template_name = 'produccion.html'
    context_object_name = 'post_aprobados'
    def get_queryset(self):
        categoria_ = Categoria.objects.get(nombre = 'producción')
        post_aprobados = Post.objects.filter(estado = True, categoria = categoria_)
        return post_aprobados
    

class PostView(DetailView):
    model = Post
    template_name = 'post.html'


