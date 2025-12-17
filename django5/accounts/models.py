from django.db import models
from django.contrib.auth .models import User
from utils.utility.models import BaseModel


class UserRole(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_role')
    is_customer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        if self.is_seller and self.is_customer:
            return f'Seller and Customer'
        elif self.is_customer:
            return f'Customer'
        elif self.is_seller:
            return f'Seller'
        else:
            return 'None'


class Customer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    phone = models.CharField(max_length=12, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username

