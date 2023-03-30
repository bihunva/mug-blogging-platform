from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify

from blog.forms import UserRegisterForm, CommentForm, PostForm
from blog.models import Post


def index(request):
    return render(request, "blog/index.html")


def search_list_view(request):
    query = request.GET.get("query")
    search_results = Post.objects.filter(title__icontains=query)
    found_number = search_results.count()
    context = {
        "search_results": search_results,
        "found_number": found_number
    }

    return render(request, "blog/search_list.html", context=context)


def registration_view(request):
    if request.method == "GET":
        register_form = UserRegisterForm()
        context = {"register_form": register_form}
        return render(request, "blog/registration.html", context=context)

    elif request.method == "POST":
        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect("blog:index")

        context = {"register_form": register_form}
        return render(request, "blog/registration.html", context=context)


def post_detail_view(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    comments = post.comments.filter(active=True)

    if request.method == "GET":
        context = {
            "post": post,
            "form": CommentForm(),
            "comments": comments,
        }
        return render(request, "blog/post_detail.html", context=context)

    elif request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect(request.META.get('HTTP_REFERER', ''))

        context = {
            "form": form,
            "post": post,
            "comments": comments
        }
        return render(request, "blog/post_detail.html", context=context)


@login_required
def post_create_view(request):
    if request.method == "GET":
        context = {"form": PostForm()}
        return render(request, "blog/post_create.html", context=context)

    elif request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return HttpResponseRedirect(reverse("blog:index"))

        context = {"form": form}
        return render(request, "blog/post_create.html", context=context)


@login_required
def saved_post_list_view(request):
    user = get_user_model().objects.get(id=request.user.id)
    saved_posts = user.saved_posts
    context = {"saved_posts": saved_posts}

    return render(request, "blog/saved_post_list.html", context=context)


@login_required
def add_post_to_saved(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    user = get_user_model().objects.get(id=request.user.id)
    user.saved_posts.add(post)
    user.save()

    return redirect(request.META.get("HTTP_REFERER", ""))


@login_required
def remove_post_from_saved(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    user = get_user_model().objects.get(id=request.user.id)
    user.saved_posts.remove(post)
    user.save()

    return redirect(request.META.get("HTTP_REFERER", ""))
