from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

import cloudinary

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = CloudinaryField('image', default='media/default.jpg')
    bio = models.CharField(blank=True,default='I am a new user!', max_length = 200)
    name = models.CharField(blank=True, max_length=120)
    contact = models.PositiveIntegerField(blank=True)
    
    def __str__(self):
        return f'{self.user.username} profile'


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
           

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
   
    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete()

    def update_bio(self,new_bio):
        self.bio = new_bio
        self.save()

    def update_image(self, user_id, new_image):
        user = User.objects.get(id = user_id)
        self.photo = new_image 
        self.save()              
    