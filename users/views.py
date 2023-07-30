from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm


def registration(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('projects')
    form = UserCreationForm
    context = {'form':form}
    return render(request, 'users/registration.html', context)

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form = AuthenticationForm
    
def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            user.email = request.POST.get('email')
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            form.save()
            return redirect('update-profile')
    
    else:
        form = ProfileForm(instance=request.user.profile)
        context = {'form': form}
        return render(request, 'users/profile-update-form.html', context)
