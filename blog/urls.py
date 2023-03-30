from django.urls import path

from blog.views import index, search_list_view

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("search/", search_list_view, name="search"),
]
