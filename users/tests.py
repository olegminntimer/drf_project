import json

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
        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json',
            # Отключаем follow, чтобы не следовать за редиректами
            follow=False
        )
        # Проверяем либо 201 (если APPEND_SLASH=False), либо 301 (если APPEND_SLASH=True)
        self.assertEqual(response.status_code, [status.HTTP_201_CREATED, status.HTTP_301_MOVED_PERMANENTLY])
        # self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

        # Если был редирект (301), проверяем конечный статус
        if response.status_code == status.HTTP_301_MOVED_PERMANENTLY:
            redirected_response = self.client.post(
                response.url,  # URL со слешом
                data=json.dumps(data),
                content_type='application/json'
            )
            self.assertEqual(redirected_response.status_code, status.HTTP_201_CREATED)
            response = redirected_response

        # Проверяем содержимое ответа
        result = response.json()
        # self.assertEqual(
        #     response.status_code, status.HTTP_200_OK
        # )
        self.assertEqual(
            result, {'message': 'Вы подписались на обновления курса'}
        )
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

        # Тест удаления подписки
        response = self.client.post(
            path=url,
            data=json.dumps(data),
            content_type='application/json',
            follow=False
        )
        # Аналогичная проверка для редиректа
        if response.status_code == status.HTTP_301_MOVED_PERMANENTLY:
            redirected_response = self.client.post(
                response.url,
                data=json.dumps(data),
                content_type='application/json'
            )
            self.assertEqual(redirected_response.status_code, status.HTTP_200_OK)
            response = redirected_response

        # Проверяем результат отписки
        self.assertEqual(response.json(), {'message': 'Вы отписались от обновления курса'})
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())
