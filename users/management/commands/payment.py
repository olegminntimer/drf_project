from django.core.management.base import BaseCommand

from lms.models import Course
from users.models import User, Payment


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not Course.objects.filter(name='Python').exists():
            course = Course(
                name="Python",
                description="Python developer",
            )
            course.save()

        payment = Payment(
            user=User.objects.get(email="user@sky.com"),
            course_paid=Course.objects.get(name="Python"),
            amount=100000,
            payment_method="cash",
        )
        payment.save()
