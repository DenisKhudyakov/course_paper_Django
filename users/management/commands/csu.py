from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUser.objects.create(
            email="admin@admin.ru",
        )
        user.set_password("qwe123")
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
