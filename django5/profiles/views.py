from django.shortcuts import render

def profile_page(request):
    return render(request, 'profile.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')
