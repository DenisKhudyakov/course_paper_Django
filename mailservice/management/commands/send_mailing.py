from datetime import datetime

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django.core.management import BaseCommand

from config import settings
from mailservice.models import MailingSettings, Message


class Command(BaseCommand):
    """Класс для запуска APScheduler."""
    help = "Runs APScheduler."

    @staticmethod
    def send_mailing() -> None:
        """Отправляет письмо."""
        zone = pytz.timezone(settings.TIME_ZONE)
        current_datetime = datetime.now(zone)
        mailing = MailingSettings.objects.filter(date_and_time_lte=current_datetime).\
            filter(status_in=[MailingSettings.StatusMailingSettings.CREATED])

        for mailing in mailing:
            send_mail(
                subject=Message.objects.get(id=mailing.id).title,
                message=Message.objects.get(id=mailing.id).body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.client.all()],
            )

    def handle(self, *args, **options) -> None:
        """Запускает APScheduler."""
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.send_mailing, "interval", seconds=10)
        scheduler.start()
