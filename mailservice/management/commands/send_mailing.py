from apscheduler.schedulers.background import BackgroundScheduler
from click.core import BaseCommand


class StartApscheduler(BaseCommand):
    """Класс для запуска APScheduler."""

    help = "Runs APScheduler."
    name = "start"

    def send_mailing(self):
        """Отправляет письмо."""
        pass

    def handle(self, *args, **options):
        """Запускает APScheduler."""
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.send_mailing, 'interval', seconds=10)
        scheduler.start()