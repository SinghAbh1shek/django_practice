from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login')
def index(request):
    print("USER:", request.user, "AUTHENTICATED:", request.user.is_authenticated)
    return render(request, 'home/home.html')
