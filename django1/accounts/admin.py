from django.contrib import admin
from .models import CustomUser

# admin.site.register(CustomUser)
@admin.register(CustomUser) #We can also write like this

# We can see all the available field using "CustomUser._meta.get_fields()""

class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'last_login',
        'phone_number',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'is_staff',
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ("Credentials", {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )

    readonly_fields = ('created_at', 'updated_at')
