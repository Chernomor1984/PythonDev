from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Message

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    confirmation = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email"]

    # Проверка email на уникальность
    def clean_email(self):
        input_email = self.cleaned_data.get("email")

        if User.objects.filter(email=input_email).exists():
            raise ValidationError("Этот email уже зарегистрирован. Придумайте другой)")

        return input_email

    # Проверка пароля на сложность
    def clean_password(self):
        input_password = self.cleaned_data.get("password")

        if input_password and len(input_password) < 12:
            raise ValidationError("Пароль слишком короткий. Минимум 12 символов")

        if input_password and not any(char.isdigit() for char in input_password):
            raise ValidationError("Добавьте хотя бы одну цифру)")

        return input_password

    # Проверка совпадения паролей
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmation = cleaned_data.get("confirmation")

        if password and confirmation and password != confirmation:
            self.add_error("confirmation", "Пароли не совпадают. Попробуй ещё раз.")

        return cleaned_data

    # Переопределение перед сохранением в БД
    def save(self, commit=True):
        user = super().save(commit=False)
        # Считаем хэш пароля
        user.set_password(self.cleaned_data.get("password"))

        if commit:
            user.save()

        return user


class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "text"]
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Напишите нам что-нибудь. Не более 500 символов",
                }
            ),
        }

    def clean_text(self):
        input_text = self.cleaned_data.get("text", "")

        if not input_text.strip():
            raise ValidationError("Сообщение не может быть пустым.")

        if len(input_text) > 500:
            raise ValidationError(
                f"Слишком длинное сообщение. Сейчас {len(input_text)} символов, а максимум - 500."
            )

        return input_text
