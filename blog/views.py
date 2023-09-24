from django.shortcuts import render

# Create your views here.
from blog.models import Categoria, Post


# Create your views here.
def blogs(request): 
    posts = Post.objects.all()
    return render(request,'blog/blog.html',{"posts": posts})

