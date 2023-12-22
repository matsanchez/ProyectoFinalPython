from django.db import models
from blog.models import Post
from django.contrib.auth.models import User


# Create your models here.
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body=models.TextField(max_length=2200)
    author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.body} {self.author}'