from .views import *
from django.urls import path

urlpatterns = [
    path('', profile_view, name='profile'),
    path('edit/', profile_edit_view, name='edit'),
    path('setting/', profile_setting_view, name='profile-settings'),
    path('onboarding/', profile_edit_view, name='profile-onboarding'),
    path('emailchange/', profile_emailchange, name='profile-emailchange'),
]