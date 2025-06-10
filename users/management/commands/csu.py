from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(email="admin@example.com").exists():
            user = User.objects.create(email="admin@example.com")
            user.set_password("12345")
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created admin user with email {user.email}"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("Администратор admin@example.com существует!")
            )
