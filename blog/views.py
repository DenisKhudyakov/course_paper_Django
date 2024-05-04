from msilib.schema import ListView

from blog.models import Post


class PostListView(ListView):
    """Контроллер отображения постов"""

    model = Post
    template_name = ""
