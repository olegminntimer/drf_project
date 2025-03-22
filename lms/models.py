from django.db import models

from config import settings


class Course(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название курса", help_text="Укажите курс"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Создайте описание для курса",
    )
    preview = models.ImageField(
        blank=True,
        null=True,
        verbose_name="Превью для курса",
        help_text="Загрузите превью для курса",
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Владелец",
                              help_text="Укажите владельца курса")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Создайте описание для урока",
    )
    preview = models.ImageField(
        blank=True,
        null=True,
        verbose_name="Превью для урока",
        help_text="Загрузите превью для урока",
    )
    video = models.FileField(
        upload_to="video/",
        blank=True,
        null=True,
        verbose_name="Видео урока",
        help_text="Загрузите видео урока",
    )
    course = models.ForeignKey(
        Course,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Название курса",
        help_text="Укажите курс",
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Владелец", help_text="Укажите владельца урока")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
