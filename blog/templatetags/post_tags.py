from django import template

from blog.forms import SearchForm
from blog.models import Post

register = template.Library()


@register.inclusion_tag("blog/tags/post_list.html")
def show_all_posts():
    posts = Post.objects.all()
    context = {"posts": posts}

    return context


@register.inclusion_tag("blog/tags/search_form.html")
def search_form():
    form = SearchForm()
    context = {"form": form}

    return context
