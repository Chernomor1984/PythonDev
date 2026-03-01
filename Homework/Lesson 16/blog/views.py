from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


def home(request):
    try:
        last_post = Post.objects.latest("created_at")
    except Post.DoesNotExist:
        last_post = None

    return render(request, "blog/home.html", {"last_post": last_post})


def about(request):
    return render(request, "blog/about.html")


class PostListView(ListView):
    model = Post
    template_name = "blog/post/list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]


class PostDetail(DetailView):
    model = Post
    template_name = "blog/post/detail.html"
    context_object_name = "post"


class PostAddOrUpdateView(UpdateView):
    model = Post
    template_name = "blog/post/create.html"
    form_class = PostForm
    success_url = reverse_lazy("blog:post_list")

    # Если в URL есть ID (pk) - редактирование
    # Иначе возвращаем None <=> создание поста
    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except AttributeError:
            return None


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")
