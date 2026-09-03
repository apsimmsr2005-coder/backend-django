from django.http import HttpResponse, JsonResponse
from .models import Producto

def inicio(request):
    return HttpResponse('Modulo de productos activo y operativo') # Método para crear una respuesta HTTP

def acerca(request):
    return HttpResponse('API de Antony')

def api_productos(request): # # Método para crear una respuesta JSON
    productos = Producto.objects.all()
    datos = []

    for producto in productos:
        datos.append({
            'id': producto.id,
            'nombre,': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': float(producto.precio),
            'stock': producto.stock,
            'activo': producto.activo,
        })
        
    return JsonResponse({'productos': datos})