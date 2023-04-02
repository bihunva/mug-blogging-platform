from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse
from django.db import models

from django_summernote.fields import SummernoteTextField
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="created")
    body = SummernoteTextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    tags = TaggableManager()

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post-detail",
            kwargs={"post_slug": self.slug}
        )

    def total_comments(self):
        return self.comments.filter(active=True).count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created"]
        indexes = [
            models.Index(fields=["created"]),
        ]


class User(AbstractUser):
    saved_posts = models.ManyToManyField(Post, related_name="users_saved")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
