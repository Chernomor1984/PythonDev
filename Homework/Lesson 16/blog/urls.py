from django.urls import path
from .views import (
    home,
    about,
    PostListView,
    PostDetail,
    PostAddOrUpdateView,
    PostDeleteView,
)

app_name = "blog"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("posts/create/", PostAddOrUpdateView.as_view(), name="post_create"),
    path("posts/<int:pk>/update/", PostAddOrUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
