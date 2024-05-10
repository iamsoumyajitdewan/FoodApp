from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Create your views here.

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'users/register.html', {'form':form})


def profile(request):
    profile_instances = Profile.objects.all()
    context={
        'profile_instances':profile_instances,
    }
    return render(request, 'users/profile.html', context)

# def logout(request):
#     return render(request, 'users/logout.html')

