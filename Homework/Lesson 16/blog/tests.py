from django.test import TestCase
from django.urls import reverse
from .models import Post


class BlogUrlTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Тестовый заголовок",
            content="Содержание для проверки тестов",
            summary="Краткое описание для проверки тестов",
            tags="тест, джанго",
        )

    def test_pages_availability(self):
        urls = [
            reverse("blog:home"),
            reverse("blog:about"),
            reverse("blog:post_list"),
            reverse("blog:post_detail", args=[self.post.id]),
            reverse("blog:post_create"),
            reverse("blog:post_update", args=[self.post.id]),
            reverse("blog:post_delete", args=[self.post.id]),
        ]

        templates = [
            "blog/home.html",
            "blog/about.html",
            "blog/post/list.html",
            "blog/post/detail.html",
            "blog/post/create.html",
            "blog/post/create.html",
            "blog/post/post_confirm_delete.html",
        ]

        contents = [
            "Блог имени «Ctrl+C, Ctrl+V»",  # home
            "Этот блог — результат долгой борьбы между человеческим разумом и документацией Django",  # about
            self.post.title,  # list
            self.post.content,  # detail
            "Создание поста",  # create
            "Редактирование",  # update
            "Вы уверены?",  # delete
        ]

        for url, template, content in zip(urls, templates, contents):
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, f"Ошибка на {url}")
            self.assertTemplateUsed(response, template, f"Неверный шаблон для {url}")
            self.assertContains(
                response, content, msg_prefix=f"Контент '{content}' не найден на {url}"
            )

    def test_post_creation(self):
        post_data = {
            "title": "Новый пост через тест",
            "summary": "Саммари через тест",
            "content": "Контент из теста",
            "tags": "теги из теста",
        }
        response = self.client.post(reverse("blog:post_create"), post_data)
        self.assertRedirects(response, reverse("blog:post_list"))
        self.assertEqual(Post.objects.count(), 2)

    def test_post_delete(self):
        response = self.client.post(reverse("blog:post_delete", args=[self.post.id]))
        self.assertRedirects(response, reverse("blog:post_list"))
        self.assertEqual(Post.objects.count(), 0)

    def test_post_update(self):
        updated_data = {
            "title": "Отредактированный заголовок",
            "summary": "Новое краткое",
            "content": "Новый контент",
            "tags": "новые теги",
        }
        response = self.client.post(
            reverse("blog:post_update", args=[self.post.id]), updated_data
        )
        self.assertRedirects(response, reverse("blog:post_list"))
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, updated_data["title"])
        self.assertEqual(self.post.summary, updated_data["summary"])
        self.assertEqual(self.post.content, updated_data["content"])
        self.assertEqual(self.post.tags, updated_data["tags"])

    def test_invalid_url(self):
        response = self.client.get("/posts/some_invalid_path/")
        self.assertEqual(response.status_code, 404)

    def test_post_detail_404(self):
        response = self.client.get(reverse("blog:post_detail", args=[999]))
        self.assertEqual(response.status_code, 404)
