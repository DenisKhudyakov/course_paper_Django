from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
#     """Класс пользователя"""
#
#     username = None
#     email = models.EmailField(
#         unique=True, verbose_name="Электронная почта", max_length=254
#     )  # email
#     first_name = models.CharField(max_length=30, verbose_name="Имя")
#     last_name = models.CharField(max_length=30, verbose_name="Фамилия")
#     telephone = models.CharField(max_length=20, null=True, blank=True)  # телефон
#
#     token = models.CharField(max_length=255, null=True, blank=True)
#
#     USERNAME_FIELD = "email"  # имя пользователя
#     REQUIRED_FIELDS = []  # обязательные поля
#
#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"
#         permissions = (
#             ("set_user_deactivate", "Can deactivate user"),
#             ("view_all_user", "Can view all user"),
#         )
#
#     def __str__(self):
#         return self.email, self.first_name, self.last_name
