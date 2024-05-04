from django.db import models

NULLABLE = {"null": True, "blank": True}


class Post(models.Model):
    """Модель блога"""

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(
        upload_to="images", verbose_name="Изображение", **NULLABLE
    )
    views = models.IntegerField(
        verbose_name="Просмотры", default=0
    )  # TODO: сделать поле для счетчика
    data_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
