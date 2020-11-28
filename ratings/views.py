from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404
# from .models import Image,Profile
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .forms import UpdateUserForm,UpdateUserProfileForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def landing(request):
    
    # posts = Image.get_images().order_by('-date_posted')
    # users = User.objects.exclude(id=request.user.id)
    # current_user = request.user
    
    return render(request,"awwards/landing.html")



@login_required(login_url='/accounts/login')
def profile(request,profile_id):
  
    # images = request.user.profile.posts.all()
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)

    params = {
        # 'images' : images,   
        'user_form': user_form,
        'prof_form': prof_form,
        
    }
    return render(request, 'awwards/profile.html', params)
@login_required(login_url='/accounts/login/')
def edit(request):
    
    
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            # return redirect('profile')
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)

    params = {
        # 'images' : images,   
        'user_form': user_form,
        'prof_form': prof_form,
        
    }
    return render(request, 'new_profile.html', params )

