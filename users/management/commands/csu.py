from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUser.objects.create_user(
            username="admin",
            email="<EMAIL>",
            password="<PASSWORD>",
            is_staff=True,
            is_superuser=True,
        )
        user.set_password("<PASSWORD>")
        user.save()
