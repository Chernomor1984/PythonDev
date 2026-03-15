from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "store/product/list.html"
    context_object_name = "products"
    ordering = ["-created_at"]


class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product/detail.html"
    context_object_name = "product"
