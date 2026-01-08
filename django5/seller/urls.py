from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='seller_home'),
    path('add-product/', seller_add_product, name='seller_add_product'),
]
