from msilib.schema import ListView

from django.views.generic import DetailView

from blog.models import Post


class PostListView(ListView):
    """Контроллер отображения постов"""

    model = Post
    template_name = ""


class PostDetailView(DetailView):
    """Контроллер отображения поста"""

    model = Post

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        article.views += 1
        article.save()
        return super().get(request, *args, **kwargs)
