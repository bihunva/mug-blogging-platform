from django.shortcuts import render

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
