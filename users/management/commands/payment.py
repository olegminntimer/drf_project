from django.core.management.base import BaseCommand

from lms.models import Course
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not Course.objects.filter(name="Python").exists():
            course = Course(
                name="Python",
                description="Python developer",
            )
            course.save()

        if not Course.objects.filter(name="Python dev").exists():
            course = Course(
                name="Python dev",
                description="Python development",
            )
            course.save()

        if not Course.objects.filter(name="Java dev").exists():
            course = Course(
                name="Java dev",
                description="Java development",
            )
            course.save()

        payment = Payment(
            user=User.objects.get(email="user@sky.com"),
            course_paid=Course.objects.get(name="Python"),
            amount=100000,
            payment_method="cash",
        )
        payment.save()

        payment = Payment(
            user=User.objects.get(email="user2@sky.pro"),
            course_paid=Course.objects.get(name="Python dev"),
            amount=110000,
            payment_method="bank_transfer",
        )
        payment.save()

        payment = Payment(
            user=User.objects.get(email="user@sky.com"),
            course_paid=Course.objects.get(name="Java dev"),
            amount=120000,
            payment_method="bank_transfer",
        )
        payment.save()
