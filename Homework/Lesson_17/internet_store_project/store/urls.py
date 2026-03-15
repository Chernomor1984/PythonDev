from django.urls import path
from django.views.generic import TemplateView
from .views import ProductListView, ProductDetailView

app_name = "store"

urlpatterns = [
    path("", TemplateView.as_view(template_name="store/main.html"), name="main"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
