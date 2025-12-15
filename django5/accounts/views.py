from django.shortcuts import render
from django.http import JsonResponse

def login_page(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')
