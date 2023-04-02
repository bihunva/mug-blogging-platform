from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic
from taggit.models import Tag

from blog.forms import UserRegisterForm, PostForm, CommentForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 8

    def get_queryset(self):
        return super().get_queryset().select_related("author").prefetch_related("tags")


class SearchListView(generic.ListView):
    model = Post
    template_name = "blog/search_list.html"
    context_object_name = "search_results"
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get("query")

        if not query:
            return self.model.objects.none()

        return self.model.objects.filter(title__icontains=query).select_related("author")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["found_number"] = self.object_list.count()

        return context


class RegistrationView(generic.View):
    def get(self, request, *args, **kwargs):
        register_form = UserRegisterForm()
        context = {"register_form": register_form}
        return render(request, "blog/registration.html", context=context)

    def post(self, request, *args, **kwargs):
        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect("blog:index")

        context = {"register_form": register_form}
        return render(request, "blog/registration.html", context=context)


class PostDetailView(generic.View):
    template_name = "blog/post_detail.html"

    def get(self, request, post_slug):
        post = Post.objects.select_related("author").get(slug=post_slug)
        comments = post.comments.filter(active=True).select_related("author")
        form = CommentForm()

        context = {"post": post, "comments": comments, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, post_slug):
        post = get_object_or_404(Post.objects.select_related("author"), slug=post_slug)
        comments = post.comments.filter(active=True).select_related("author")
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect(request.META.get("HTTP_REFERER", ""))

        context = {"post": post, "comments": comments, "form": form}
        return render(request, self.template_name, context)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_create.html"
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form: type[PostForm]):
        post = form.save(commit=False)
        post.author = self.request.user
        post.slug = slugify(post.title)
        post.save()

        return super().form_valid(form)


class SavedPostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "blog/saved_post_list.html"
    context_object_name = "saved_posts"

    def get_queryset(self):
        user = get_user_model().objects.get(id=self.request.user.id)
        queryset = user.saved_posts.select_related("author")

        return queryset


@login_required
def add_post_to_saved(request, post_slug: str) -> HttpResponse:
    post = get_object_or_404(Post, slug=post_slug)
    user = get_user_model().objects.get(id=request.user.id)
    user.saved_posts.add(post)
    user.save()

    return redirect(request.META.get("HTTP_REFERER", ""))


@login_required
def remove_post_from_saved(request, post_slug: str) -> HttpResponse:
    post = get_object_or_404(Post, slug=post_slug)
    user = get_user_model().objects.get(id=request.user.id)
    user.saved_posts.remove(post)
    user.save()

    return redirect(request.META.get("HTTP_REFERER", ""))


def post_list_by_tag(request, tag_slug: str) -> HttpResponse:
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__in=[tag])
    context = {"posts": posts, "tag": tag}

    return render(request, "blog/post_list_by_tag.html", context=context)
