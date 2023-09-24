from django.shortcuts import render

# Create your views here.
from blog.models import Categoria, Post


# Create your views here.
def blogs(request): 
    posts = Post.objects.all()
    return render(request,'blog/blog.html',{"posts": posts})

def categoria(request, categoria_id): 
    categoria = Categoria.objects.get(id= categoria_id)
    posts = Post.objects.filter(categoria = categoria)
    return render(request,'blog/categoria.html',{"categoria": categoria, "posts": posts})


