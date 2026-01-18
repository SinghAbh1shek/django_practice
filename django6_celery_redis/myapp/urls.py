from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('check-result/<str:task_id>/', check_result, name='check_result'),
]
