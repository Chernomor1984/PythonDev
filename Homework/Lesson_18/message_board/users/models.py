from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendedUser(AbstractUser):
    phone_number = models.CharField(
        "Номер телефона", max_length=25, blank=True, null=True
    )
    bio = models.TextField("О себе", blank=True, null=True)

    def __str__(self):
        return self.username


class Message(models.Model):
    user = models.ForeignKey(
        ExtendedUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="messages",  # Обратная связь сообщений с конкретным юзером <--> user.messages.all()
    )

    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Электронная почта")
    text = models.TextField("Текст сообщения")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Сообщение от {self.name} ({self.created_at.strftime('%d.%m.%Y')})"
