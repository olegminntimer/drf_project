from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(email="user1@sky.com").exists():
            user = User.objects.create(email="user1@sky.com")
            user.set_password("12345")
            user.is_active = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Пользователь {user.email} создан!"))
        else:
            self.stdout.write(
                self.style.SUCCESS("Пользователь user1@sky.com существует!")
            )

        if not User.objects.filter(email="user2@sky.pro").exists():
            user = User.objects.create(email="user2@sky.pro")
            user.set_password("12345")
            user.is_active = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Пользователь {user.email} создан!"))
        else:
            self.stdout.write(
                self.style.SUCCESS("Пользователь user2@sky.pro существует!")
            )
