from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(email="user@sky.com").exists():
            user = User.objects.create(email="user@sky.com")
            user.set_password("12345")
            user.is_active = True
            user.save()
        else:
            self.stdout.write(self.style.SUCCESS(f'Пользователь существует!'))
