from django.db import models


class Product(models.Model):
    name = models.CharField("Название товара", max_length=350)
    description = models.TextField("Описание товара")
    price = models.DecimalField("Цена товара", max_digits=10, decimal_places=2)
    image = models.ImageField("Изображение товара", upload_to="products/")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
