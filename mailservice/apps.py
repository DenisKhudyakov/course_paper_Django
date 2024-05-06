from django.apps import AppConfig
from django.core.management import call_command



class MailserviceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailservice"

    def ready(self):
        call_command('send_mailing')