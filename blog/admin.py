from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
