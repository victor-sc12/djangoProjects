from .models import Link

# Extensión del diccionario de contexto global:
def ctx_dict(request):
    ctx = {}

    for link in Link.objects.all():
        ctx[link.key] = link.url
    
    return ctx # Los key-value de este dict serán globales para cada template del project