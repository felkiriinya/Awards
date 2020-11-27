from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from .models import Image,Profile
from django.shortcuts import render,redirect,get_object_or_404
# from .forms import NewPostForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def landing(request):
    
    # posts = Image.get_images().order_by('-date_posted')
    # users = User.objects.exclude(id=request.user.id)
    # current_user = request.user
    
    return render(request,"awwards/landing.html")



