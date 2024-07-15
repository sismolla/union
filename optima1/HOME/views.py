from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import ProfileForm
from .models import Videos
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url='user:login')
def homepage(request):
    return render(request,'home/hbase.html')

@login_required(login_url='user:login')
def dashboard(request):
    file = Videos.objects.all()
    return render(request,'home/dashbored.html',{'files':file})

@login_required(login_url='user:login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('home:profile')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('home:profile')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'home/profile.html', {'form': form})

@login_required(login_url='user:login')
def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('user:login')