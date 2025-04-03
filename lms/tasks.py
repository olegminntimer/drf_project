import pytz

from celery import shared_task
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from rest_framework.generics import get_object_or_404
from datetime import timedelta, datetime

from lms.models import Course
from users.models import Subscription, User


@shared_task
def subscription_update(pk):
    course = get_object_or_404(Course, pk=pk)
    subscriptions = Subscription.objects.filter(course=course)
    sub_users = [subscription.user for subscription in subscriptions]
    for sub_user in sub_users:
        try:
            send_mail(
                subject="Обновления курса.",
                message=f'Курс "{course.name}" обновился!',
                from_email=EMAIL_HOST_USER,
                recipient_list=[
                    sub_user,
                ],
            )
        except Exception as e:
            print(str(e))


@shared_task
def check_last_login():
    users = User.objects.all()
    for user in users:
        time_difference = datetime.now().replace(tzinfo=pytz.utc) - user.last_login
        if time_difference > timedelta(days=30):
            user.is_active = False
            user.save()
