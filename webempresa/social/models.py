from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name='nombre clave', max_length=200, unique=True)
    name = models.CharField(verbose_name='red social', max_length=200)
    url = models.URLField(verbose_name='enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['created']

    def __str__(self):
        return self.name