from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    """Клиент сервиса, поля email, ФИО, комментарий"""

    email = models.EmailField(max_length=150, unique=True, verbose_name="почта")
    name = models.CharField(max_length=100, verbose_name="ФИО")
    comments = models.TextField(verbose_name="комментарий", **NULLABLE)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="владелец", null=True
    )

    def __str__(self):
        return f"{self.name}, {self.email}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Message(models.Model):

    title = models.CharField(max_length=150, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текс сообщения", **NULLABLE)

    def __str__(self):
        return f"{self.title}, {self.body[:50]}..."

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"


class MailingSettings(models.Model):
    """Класс рассылки, поля дата и время, периодичность(раз в день, раз в неделю, раз в месяц),
    статус рассылки(завершена, создана, запущена)
    """

    class PeriodMailingSettings(models.TextChoices):
        ONE_DAY = "Раз в день", _("Раз в день")
        ONE_WEEK = "Раз в неделю", _("Раз в неделю")
        ONE_MONTH = "Раз в месяц", _("Раз в месяц")

    class StatusMailingSettings(models.TextChoices):
        STARTED = "Запущена", _("Запущена")
        CREATED = "Создана", _("Создана")
        COMPLETED = "Завершена", _("Завершена")

    create_date = models.DateTimeField(
        default=timezone.now, verbose_name="дата создания рассылки"
    )  # создание рассылки

    sent_time = models.DateField(
        default=timezone.now,
        null=True,
        blank=True,
        verbose_name="время отправки рассылки",
    )
    period = models.CharField(
        max_length=50,
        choices=PeriodMailingSettings,
        verbose_name="периодичность рассылки",
    )
    status = models.CharField(
        max_length=50, choices=StatusMailingSettings, verbose_name="статус"
    )
    client = models.ManyToManyField(Client, verbose_name="клиенты рассылки")
    message = models.ForeignKey(
        Message, verbose_name="сообщение", on_delete=models.CASCADE, null=True
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="владелец рассылки", null=True
    )

    def __str__(self):
        return f"{self.date_and_time},{self.period}, {self.status}, {self.client}"

    class Meta:
        verbose_name = "настройка рассылки"
        verbose_name_plural = "настройки рассылки"
        permissions = [
            ("set_deactivate", "Can deactivate mailing"),
            ("view_all_mailings", "Can view all mailing"),
        ]


class Logs(models.Model):
    """Модель попытки рассылки, поля: дата и время последней рассылки, статус(успешно/не успешно)
    ответ почтового сервера, если он был
    """

    TRY_STATUS_TO_SEND = [
        ("success", "Успешно"),
        ("fail", "Не успешно"),
    ]

    date = models.DateField(
        verbose_name="дата и время последней рассылки", auto_now_add=True
    )
    status = models.CharField(
        max_length=50, choices=TRY_STATUS_TO_SEND, verbose_name="статус"
    )
    server_response = models.CharField(
        verbose_name="ответ почтового сервера", **NULLABLE
    )
    mailing_settings = models.ForeignKey(
        MailingSettings, verbose_name="настройка рассылки", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="пользователь"
    )  # пользователь

    def __str__(self):
        return f"{self.mailing_settings}, {self.date}, {self.status}, {self.user}"

    class Meta:
        verbose_name = "попытка рассылки"
        verbose_name_plural = "попытки рассылки"
