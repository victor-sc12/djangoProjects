from django.contrib import admin
from .models import Project

# Configuracion extendida del modelo:
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Register your models here.
admin.site.register(Project, ProjectAdmin)