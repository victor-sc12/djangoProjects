from django.contrib import admin
from .models import Category, Post

# Model extend configuration
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    # Personalización adicional del panel de administración:
    list_display = ('title', 'author', 'post_categories', 'published')
    ordering = ('author', 'published',)
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    # función para listar todos los 'categories' obj relacionados a la instancia de 'Post' actual: 
    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorías' # sobreescribir el nombre de la función en el panel admin


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)