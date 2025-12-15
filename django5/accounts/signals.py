from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer, UserRole
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def customer_post_save(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user = instance)
        UserRole.objects.create(user = instance)