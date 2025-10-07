from django import forms
from .models import Page
from tinymce.widgets import TinyMCE


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': TinyMCE(),
            'order': forms.NumberInput(attrs={'class': 'form-control'})
        }
        