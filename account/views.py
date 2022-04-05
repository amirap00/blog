from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm




# روش یوتیوب
def user_register(request):
    if request.method == 'POST':
        # به خاطر اضافه کردن اسم و فامیلی و ایمیل در پوشه forms اسم هم تغییر می کند
        # form = UserCreationForm(request.POST)
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # messages.success(request, ('Registration successfull'))
            return redirect('home:home')
    else:
        # form = UserCreationForm()
        form = RegisterUserForm()

    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'account/account.html', {})

def user_logout(request):
    logout(request)
    return redirect('/')

