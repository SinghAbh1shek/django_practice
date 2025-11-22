from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

class CustomUser(AbstractBaseUser):
    username = None
    phone_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ["email"]     #if we use unique = True other than username_field then we must add those field in Require_field
    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser    # only super user have permission to access all the data

    def has_module_perms(self, app_lebel):
        return self.is_superuser    # only superuser can see the whole app in the admin sidebar
