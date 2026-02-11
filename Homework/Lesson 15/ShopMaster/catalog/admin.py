from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Авто слаг (заполнение)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Какие колонки показывать в списке
    list_display = ("name", "category", "price", "stock", "available")
    # По каким полям можно кликнуть, чтобы перейти в товар
    list_display_links = ("name",)
    # Фильтры
    list_filter = ("available", "category", "created_at")
    # Поля для поиска (ищет по названию и описанию)
    search_fields = ("name", "description")
    # Быстрое редактирование прямо в списке (не заходя внутрь товара)
    list_editable = ("price", "stock", "available")
    # Авто слаг (заполнение)
    prepopulated_fields = {"slug": ("name",)}
