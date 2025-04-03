from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course
from users.models import User, Subscription


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
        response = self.client.post(url, data)
        result = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            result, {'message': 'Вы подписались на обновления курса'}
        )

        url = reverse("users:subscription")
        data = {
            "user": self.user.pk,
            "course": self.course.pk
        }
        response = self.client.post(url, data)
        result = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            result, {'message': 'Вы отписались от обновления курса'}
        )
