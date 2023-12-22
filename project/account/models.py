from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here. 
class Profile(models.Model):
    avatar=models.ImageField(default="/users/default_avatar.jpeg",upload_to="avatars/",null=True, blank=True)
    user=models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name=models.CharField(max_length=100, null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True, blank=True)
    email=models.EmailField(max_length=100, null=True, blank=True)
    birthday=models.DateField(null=True, blank=True)
    description=models.CharField(max_length=500, null=True, blank=True)
    link_url=models.URLField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name} >> {self.user}'
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)