from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    updated_at = models.DateTimeField(auto_now=True)
    
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
    

class Project(models.Model):
    image = CloudinaryField('image')
    sitename = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    technologies = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    def __str__(self):
        return self.sitename

    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images     

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        got_projects = Project.objects.filter(sitename__icontains=search_term)
        return got_projects
    # @classmethod
    # def search_by_projects(cls,search_term):
    #     projects = cls.objects.filter(title__icontains=search_term)
    #     return projects 

class Rating(models.Model):
    RATINGS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    post = models.ForeignKey(Project, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    usability_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
    design_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
    content_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
    review = models.CharField(max_length=200)

    def __str__(self):
        return self.review

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()