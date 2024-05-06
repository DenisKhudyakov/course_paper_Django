from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    """Клиент сервиса, поля email, ФИО, комментарий"""

    email = models.EmailField(max_length=150, unique=True, verbose_name="почта")
    name = models.CharField(max_length=100, verbose_name="ФИО")
    comments = models.TextField(verbose_name="комментарий", **NULLABLE)

    def __str__(self):
        return f"{self.name}, {self.email}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


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

    date_and_time = models.DateField(verbose_name="дата и время первой рассылки")
    period = models.CharField(
        max_length=50,
        choices=PeriodMailingSettings,
        verbose_name="периодичность рассылки",
    )
    status = models.CharField(
        max_length=50, choices=StatusMailingSettings, verbose_name="статус"
    )
    client = models.ManyToManyField(Client, verbose_name="клиенты рассылки")


    def __str__(self):
        return f"{self.date_and_time},{self.period}, {self.status}, {self.client}"

    class Meta:
        verbose_name = "настройка рассылки"
        verbose_name_plural = "настройки рассылки"


class Message(models.Model):

    title = models.CharField(max_length=150, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текс сообщения", **NULLABLE)
    mailing_settings = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name="рассылка", **NULLABLE)

    def __str__(self):
        return f"{self.title}, {self.body[:50]}..."

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"


class Logs(models.Model):
    """Модель попытки рассылки, поля: дата и время последней рассылки, статус(успешно/не успешно)
    ответ почтового сервера, если он был
    """

    date = models.DateField(
        verbose_name="дата и время последней рассылки", auto_now_add=True
    )
    status = models.BooleanField(verbose_name="статус рассылки")
    server_response = models.CharField(
        verbose_name="ответ почтового сервера", **NULLABLE
    )
    client = models.ForeignKey(Client, verbose_name="клиент", on_delete=models.CASCADE)
    mailing_settings = models.ForeignKey(
        MailingSettings, verbose_name="настройка рассылки", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.date}, {self.status}"

    class Meta:
        verbose_name = "лог"
        verbose_name_plural = "логи"
