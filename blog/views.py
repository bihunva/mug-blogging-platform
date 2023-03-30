from django.contrib.auth import login
from django.shortcuts import render, redirect

from blog.forms import UserRegisterForm
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
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect("blog:index")

    register_form = UserRegisterForm()
    context = {"register_form": register_form}

    return render(request, "blog/registration.html", context=context)


def post_detail_view(request, post):
    post = Post.objects.get(slug=post)
    context = {"post": post}

    return render(request, "blog/post_detail.html", context=context)
