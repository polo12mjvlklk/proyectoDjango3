from django.shortcuts import render
from.models import *
# Create your views here.
def verCategorias(request):
    #consultar categorias
    listaCateg = categoria.objects.all()

    #ensamblar context
    context = {
        'categorias': listaCateg,
        'titulo': 'categorias de productos del supermercado',

    }
    #renderizar
    return render(request, 'productos/categorias.html', context)
def verProductosCategoria(request, idcategoria):
    #consultar categorias
    idcat = int(idcategoria)
    nombreCat = categoria.objects.get(id=idcat)
    listaProductos = producto.objects.filter(categoria= idcat)

    #ensamblar  context
    context = {
        'productos': listaProductos,
        'titulo': 'productos de la categoria' + str(nombreCat),
    }
    #renderizar
    return render(request, 'productos/productos.html', context)
def verProducto(request, idProd, mj = None):
    #consultar
    idProd = int(idProd)
    regProducto = producto.objects.get(id= idProd)
    #ensamblar context
    context = {
        'producto': regProducto,
        'titulo': 'Detalles de' + str(regProducto.nombre),
    }
    #renderizar
    return render(request, 'productos/producto.html',context)
    
