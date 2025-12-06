from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='login')
def index(request):
    return render(request, 'home/home.html')

def login_page(request):
    return render(request, 'home/login.html')

def register_page(request):
    return render(request, 'home/register.html')

def logout_page(request):
    logout(request)
    print('Successfully loggedout')
    return redirect('login')