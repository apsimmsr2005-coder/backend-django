from django.http import HttpResponse, JsonResponse

def inicio(request):
    return HttpResponse('Modulo de productos activo y operativo') # Método para crear una respuesta HTTP

def acerca(request):
    return HttpResponse('API de Antony')

def api_productos(request): # # Método para crear una respuesta JSON
    if request.method == 'GET':
        datos = [
            {'id':1, 'nombre': 'Teclado'},
            {'id':2, 'nombre': 'Mouse'},
        ]
        return JsonResponse(datos, safe=False)

    return JsonResponse(
        {'error': 'Método no permitido'},
        status=405
    )