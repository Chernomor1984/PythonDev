from django.contrib import admin
from .models import Post
from django.template.defaultfilters import truncatechars


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "trunk_content", "created_at")
    list_display_links = ("title",)
    list_filter = ("created_at",)
    search_fields = ("title",)

    @admin.display(description="Содержание (кратко)")
    def trunk_content(self, post: Post):
        return truncatechars(post.content, 50)
