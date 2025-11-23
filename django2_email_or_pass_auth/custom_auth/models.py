from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(unique=True, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    def save(self, *args, **kwargs):

        if not self.email and not self.phone_number and self.username:
            #  when we create superuser the both email and phonenumber is empty so we have to handle like this
            if '@' in self.username:
                self.email = self.username
            else:
                self.phone_number = self.username

        if self.phone_number:
            if not self.phone_number.isdigit():
                raise ValueError('Phone Number must contains digit only')
            if len(self.phone_number) != 10:
                raise ValueError('Phone Number must be exactly 10 number')
            
        if self.email:
            self.username = self.email
        elif self.phone_number:
            self.username = self.phone_number
        else:
            raise ValueError('Email or phone number is required')
        
        super().save(*args, **kwargs)
    def __str__(self):
        return self.username