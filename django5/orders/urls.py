from django.urls import path
from .views import *

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('remove-to-cart/', remove_to_cart, name='remove_to_cart'),
]
