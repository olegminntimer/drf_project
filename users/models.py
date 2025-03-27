from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    city = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):

    CASH = "cash"
    BANK_TRANSFER = "bank_transfer"

    method = [
        (CASH, "наличные"),
        (BANK_TRANSFER, "перевод на счет"),
    ]

    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
        related_name="payments"
    )
    date = models.DateField(
        # auto_now=True,
        blank=True,
        null=True,
        verbose_name="Дата оплаты",
        help_text="Введите дату оплаты",
    )
    course_paid = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Курс",
        help_text="Введите курс",
        related_name="courses"
    )
    lesson_paid = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Урок",
        help_text="Введите урок",
        related_name="lessons"
    )
    amount = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Сумма оплаты",
        help_text="Введите сумму оплаты",
    )
    payment_method = models.CharField(
        max_length=15,
        choices=method,
        blank=True,
        null=True,
        verbose_name="Способ оплаты",
        help_text="Введите способ оплаты",
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплата"


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
        related_name="users_subs"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Курс",
        help_text="Введите курс",
        related_name="courses_subs"
    )
    # subscription_status = models.BooleanField(
    #     blank=True,
    #     null=True,
    #     verbose_name="Подписка",
    #     help_text="Введите статус подписки",
    # )