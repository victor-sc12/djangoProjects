from django.contrib import admin
from .models import Page
from tinymce.widgets import TinyMCE
from django.db import models
from django import forms

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        forms.Textarea: {'widget': TinyMCE()}
    }


admin.site.register(Page, PageAdmin)
