from django import template
from pages.models import Page

# Se definira un decorador para incorporar el obj list como templatetag:
register = template.Library()

@register.simple_tag  # <-- decorator 
def get_pages_list():
    pages = Page.objects.all()
    return pages