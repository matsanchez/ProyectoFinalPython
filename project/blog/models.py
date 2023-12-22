from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

    
class Post(models.Model):
    title=models.CharField(max_length=100, verbose_name='Titulo')
    subtitle=models.CharField(max_length=100, verbose_name='Subtitulo')
    body=RichTextField(max_length=500, verbose_name='Experiencia')
    author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Autor')
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="posts/",null=False, blank=False,verbose_name='Imagen')

    def __str__(self):
        return f'{self.title} {self.subtitle}'