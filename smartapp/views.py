from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from smartapp.forms import *
from .models import *



# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})

@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, "profile.html", {"profile": profile})


@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    return render(request, 'update_profile.html', {"form":form})
