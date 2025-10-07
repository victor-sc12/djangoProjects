from django.shortcuts import render
from django.views.generic.base import TemplateView

# CBV usadas en lugar de FBV:
class HomeView(TemplateView):
    template_name = "core/home.html"

    # Extender diccionario de contexto mediante funcion predifinida
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = 'Article.objects.all()[:5]'
    #     return context
    
    # Una manera mas directa de devolver el response del view como si fuese un fbv, es
    # sobreescribiendo la funcion get:
    def get(self, request, *args, **kwargs):
        # return super().get(request, *args, **kwargs)
        return render(request, self.template_name, {'title': 'rticle.objects.all()[:5]'})

class SampleView(TemplateView):
    template_name = "core/sample.html"

# FBV usadas previamente:
# def home(request):
#     return render(request, "core/home.html")

# def sample(request):
#     return render(request, "core/sample.html")