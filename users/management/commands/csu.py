from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create_user(
            username='admin',
            email='<EMAIL>',
            password='<PASSWORD>',
            is_staff=True,
            is_superuser=True,
        )
        user.set_password('<PASSWORD>')
        user.save()
