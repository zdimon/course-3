from django.shortcuts import render, redirect

def home(request):
    return render(request,'shop/home.html')


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as l, logout
from django.contrib import messages	

def login(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        l(request, user)
        return redirect('home')
    else:
        messages.warning(request, 'Error!!!!')
        return redirect('home')

def logoutme(request):
    logout(request)
    return redirect('home')
