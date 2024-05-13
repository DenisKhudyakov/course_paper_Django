# Generated by Django 5.0.4 on 2024-05-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Заголовок")),
                ("content", models.TextField(verbose_name="Содержимое")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images",
                        verbose_name="Изображение",
                    ),
                ),
                ("views", models.IntegerField(default=0, verbose_name="Просмотры")),
                (
                    "data_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата публикации"
                    ),
                ),
            ],
            options={
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
            },
        ),
    ]
