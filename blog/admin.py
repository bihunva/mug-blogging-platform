from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blog.models import User, Post, Comment


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["username", "email", "first_name", "last_name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["created", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "created"
    ordering = ["created"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["body", "author", "post", "created", "active"]
    list_filter = ["active", "created", "updated"]
    search_fields = ["name", "body"]
