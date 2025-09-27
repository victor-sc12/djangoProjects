from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name='título', max_length=200)
    content = models.TextField(verbose_name='contenido')
    order = models.SmallIntegerField(verbose_name='orden', default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        ordering = ['order','title']

    def __str__(self):
        return self.title