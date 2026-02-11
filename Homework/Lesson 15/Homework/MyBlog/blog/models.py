from django.db import models


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(verbose_name="Когда создан", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
