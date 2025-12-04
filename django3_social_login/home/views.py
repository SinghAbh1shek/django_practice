from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    return render(request, 'home/home.html')

def login_page(request):
    return render(request, 'home/login.html')

def register_page(request):
    return render(request, 'home/register.html')
