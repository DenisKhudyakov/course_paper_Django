from apscheduler.schedulers.background import BackgroundScheduler
from click.core import BaseCommand


class StartApscheduler(BaseCommand):
    help = "Runs APScheduler."
    name = "start"

    def send_mailing(self):
        pass

    def handle(self, *args, **options):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.send_mailing, 'interval', seconds=10)
        scheduler.start()