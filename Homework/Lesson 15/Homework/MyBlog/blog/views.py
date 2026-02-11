from django.views.generic import ListView, DetailView
from django.utils import timezone
from datetime import timedelta
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post/list.html"
    context_object_name = "posts"  # Название списка внутри HTML
    ordering = ["-created_at"]
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_type = self.request.GET.get("filter")
        now = timezone.now()

        filters = {
            "hour": now - timedelta(hours=1),
            "today": now.date(),
            "week": now - timedelta(days=7),
            "month": now - timedelta(days=30),
            "year": now - timedelta(days=365),
        }

        if filter_type == "hour":
            return queryset.filter(created_at__gte=filters["hour"])
        elif filter_type == "today":
            return queryset.filter(created_at__date=filters["today"])
        elif filter_type in filters:
            return queryset.filter(created_at__gte=filters[filter_type])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_filter"] = self.request.GET.get("filter", "all")
        titles = {
            "hour": "Записи за последний час",
            "today": "Записи за сегодня",
            "week": "Записи за неделю",
            "month": "Записи за месяц",
            "year": "Записи за год",
            "all": "Все записи",
        }
        context["page_title"] = titles.get(
            self.request.GET.get("filter"), "Список записей"
        )
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post/detail.html"
    context_object_name = "post"
