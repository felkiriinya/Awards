from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Project,Rating

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.felista = User(username = 'Felista', email = "felkiriinya@gmail.com", password ='Tomorrowfel1#')
        self.profile = Profile(user = self.felista,profile_photo = 'image.jpg', bio = 'I am a software developer')
        self.felista.save()
        # self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.felista, User))
        self.assertTrue(isinstance(self.profile, Profile))        

class ProjectTestClass(TestCase):
    def setUp(self):
        self.felista = User(username = 'Felista', email = "felkiriinya@gmail.com", password ='Tomorrowfel1#')
        self.profile = Profile(user = self.felista,profile_photo = 'image.jpg', bio = 'I am a software developer')
        self.project = Project(sitename = "blogger", image ='blog.jpg',desc ='Cool',link = 'blogger.com', categories = 'website', user = self.felista)
        self.felista.save()
        self.project.save_project()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Project.objects.all().delete()    

    def test_image_instance(self):
        self.assertTrue(isinstance(self.project, Project))    

    def test_save_project(self):
        projects = Project.objects.all()
        self.assertTrue(len(projects)> 0)

    def test_delete_project(self):
        projects1 = Project.objects.all()
        self.assertEqual(len(projects1),1)
        self.project.delete_project()
        projects2 = Project.objects.all()
        self.assertEqual(len(projects2),0)    

    def test_search_project(self):
        project = Project.search_by_name('blogger')
        self.assertEqual(len(project),1)    

    def test_get_user_projects_(self):
        profile_projects = Project.get_images()
        self.assertEqual(profile_projects[0].sitename, 'blogger')
        self.assertEqual(len(profile_projects),1 )
    
class RatingTestClass(TestCase):
    def setUp(self):
        self.felista = User(username = 'Felista', email = "felkiriinya@gmail.com", password ='Tomorrowfel1#')
        self.profile = Profile(user = self.felista,profile_photo = 'image.jpg', bio = 'I am a software developer')
        self.project = Project(sitename = "blogger", image ='blog.jpg',desc ='Cool',link = 'blogger.com', categories = 'website', user = self.felista)
        self.rating = Rating(user = self.felista, post= self.project, usability_rating= 1,design_rating=3, content_rating=8, review="great")
        self.felista.save()
        self.project.save_project()    
        self.rating.save_rating()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Project.objects.all().delete()   
        Rating.objects.all().delete() 

    
    def test_rating_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        ratings = Rating.objects.all()
        self.assertTrue(len(ratings)>0)

    def test_delete_rating(self):
        rating1 = Rating.objects.all()
        self.assertEqual(len(rating1),1)

        self.rating.delete_rating()

        rating2 = Rating.objects.all()
        self.assertEqual(len(rating2),0)    

 