from django.urls import path

from blog.views import (
    PostListView,
    SearchListView,
    RegistrationView,
    PostDetailView,
    PostCreateView,
    SavedPostListView,
    # add_post_to_saved,
    # remove_post_from_saved,
    add_remove_post_from_saved,
    post_list_by_tag,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("search/", SearchListView.as_view(), name="search"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("posts/saved/", SavedPostListView.as_view(), name="saved-posts"),
    path("posts/<slug:post_slug>/", PostDetailView.as_view(), name="post-detail"),
    # path("posts/<slug:post_slug>/add", add_post_to_saved, name="add-post-to-saved"),
    # path("posts/<slug:post_slug>/remove", remove_post_from_saved, name="remove-post-from-saved"),
    path("post/<slug:post_slug>/<int:already_added>/", add_remove_post_from_saved, name="add_remove_post"),
    path("tags/<slug:tag_slug>/", post_list_by_tag, name="post-list-by-tag"),
]

app_name = "blog"
