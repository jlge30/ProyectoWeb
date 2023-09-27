from django.shortcuts import render
from tienda.models import CategoriaProd, Producto

# Create your views here.
def tienda(request): 
    productos = Producto.objects.all()
    return render(request,'tienda/tienda.html', {"productos": productos} )

def categoriaProd(request, categorias_id):
    categoria = CategoriaProd.objects.get(id = categorias_id)
    productos = Producto.objects.filter(categoria = categoria)
    return render(request, 'tienda/tienda.html', {"categoriaProd": categoria, "productos": productos })





