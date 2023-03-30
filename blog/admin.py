from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['created', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'created'
    ordering = ['created']
