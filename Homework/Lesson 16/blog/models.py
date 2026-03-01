from django.db import models


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    content = models.TextField("Содержание поста")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    summary = models.CharField("Краткое содержание", max_length=250)
    tags = models.CharField(" Теги", max_length=50, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "пост"
        verbose_name_plural = "посты"
