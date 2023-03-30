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
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog:index")

    form = UserRegisterForm()
    context = {"register_form": form}

    return render(request, "blog/registration.html", context=context)
