from django import template

from blog.models import Post

register = template.Library()


@register.inclusion_tag("blog/post_list.html")
def show_all_posts():
    posts = Post.objects.all()
    context = {"posts": posts}

    return context
