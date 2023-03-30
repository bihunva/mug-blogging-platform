from django.urls import path

from blog.views import (
    index,
    search_list_view,
    registration_view,
    post_detail_view,
    post_create_view,
)

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("search/", search_list_view, name="search"),
    path("registration/", registration_view, name="registration"),
    path("posts/create/", post_create_view, name="post-create"),
    path("posts/<slug:post>/", post_detail_view, name="post-detail"),
]


