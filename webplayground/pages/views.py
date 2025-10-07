from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Page
from django.urls import reverse, reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.utils.text import slugify
from .forms import PageForm


# Mixin Class para verificar user loged:
class StaffRequiredMixin(object):

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

    # def get(self, request, *args, **kwargs):
    #     return render(request, 'pages/page.html', {'page':self.page})
    
@method_decorator(staff_member_required, name = 'dispatch')
class PageCreate(StaffRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    # fields = ["title", "content", "order"]

    # Método para redireccionar a página de éxito tras llenar el formulario de creación:
    # def get_success_url(self):
        # return super().get_success_url()
    #    return reverse('pages:pages')
    
    # para evitar escribir todo el método reciente, usar método 'reverse_lazy'
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name = 'dispatch')
class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    fields = ["title", "content", "order"]
    template_name_suffix = "_update_form"

    def get_success_url(self): 
        return reverse_lazy('pages:page', args = (self.object.id, slugify(self.object.title))) + '?ok'

@method_decorator(staff_member_required, name = 'dispatch')
class PageDelete(StaffRequiredMixin, DeleteView):
    model = Page
    # template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('pages:pages')

    # def get_queryset(self):
    #     return super().get_queryset().filter(owner=self.request.user)
    