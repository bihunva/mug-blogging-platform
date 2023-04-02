from django.urls import path

from blog.views import (
    PostListView,
    SearchListView,
    RegistrationView,
    post_detail_view,
    post_create_view,
    saved_post_list_view,
    add_post_to_saved,
    remove_post_from_saved,
    post_list_by_tag,
)

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("search/", SearchListView.as_view(), name="search"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("posts/create/", post_create_view, name="post-create"),
    path("posts/saved/", saved_post_list_view, name="saved-posts"),
    path("posts/<slug:post_slug>/add", add_post_to_saved, name="add-post-to-saved"),
    path("posts/<slug:post_slug>/remove", remove_post_from_saved, name="remove-post-from-saved"),
    path("posts/<slug:post_slug>/", post_detail_view, name="post-detail"),
    path("tags/<slug:tag_slug>/", post_list_by_tag, name="post-list-by-tag")
]
