from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "summary", "created_at", "tags")
    list_display_links = ("title",)
    list_filter = ("created_at", "tags")
    search_fields = ("title", "tags")
