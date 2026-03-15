from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (  # Отображение в виде колонок в таблице
        "name",
        "price",
        "created_at",
    )
    list_display_links = ("name",)  # Кликабельный заголовок
    search_fields = ("name",)  # Поиск по имени
    list_filter = ("created_at",)  # Фильтр по дате
