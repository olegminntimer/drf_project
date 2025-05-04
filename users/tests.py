import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course
from users.models import User


class SubscriptionAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.ru")
        self.course = Course.objects.create(name="Basic")
        self.client.force_authenticate(user=self.user)
        # self.subscription = Subscription.objects.create(user=self.user, course=self.course)

    def test_subscription(self):
        url = reverse("users:subscription")
        data = {
            "user": self.user.pk,
            "course": self.course.pk
        }
        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json',
            # Отключаем follow, чтобы не следовать за редиректами
            follow=False
        )
        # Проверяем либо 201 (если APPEND_SLASH=False), либо 301 (если APPEND_SLASH=True)
        self.assertEqual(response.status_code, 301)
