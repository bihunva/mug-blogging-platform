from django import template
from django.db.models import Count
from taggit.models import Tag

from blog.forms import SearchForm
from blog.models import Post

register = template.Library()


@register.inclusion_tag("blog/inclusions/search_form.html")
def search_form():
    form = SearchForm()
    context = {"form": form}

    return context


@register.inclusion_tag("blog/inclusions/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-created').select_related("author")[:count]
    content = {"latest_posts": latest_posts}

    return content


@register.inclusion_tag("blog/inclusions/most_commented_posts.html")
def show_most_commented_posts(count=5):
    most_commented_posts = Post.objects.annotate(
        total_comments=Count("comments")
    ).select_related("author").order_by("-total_comments")[:count]
    context = {"most_commented_posts": most_commented_posts}

    return context


@register.inclusion_tag("blog/inclusions/tag_list.html")
def show_tags(count=10):
    tags = Tag.objects.all()[:count]
    context = {"tags": tags}

    return context
