from django.contrib import admin
from .models import Page
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Page, PageAdmin)