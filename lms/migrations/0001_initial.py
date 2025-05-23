# Generated by Django 5.1.7 on 2025-04-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите курс",
                        max_length=100,
                        verbose_name="Название курса",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Создайте описание для курса",
                        null=True,
                        verbose_name="Описание курса",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью для курса",
                        null=True,
                        upload_to="",
                        verbose_name="Превью для курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название урока",
                        max_length=100,
                        verbose_name="Название урока",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Создайте описание для урока",
                        null=True,
                        verbose_name="Описание урока",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью для урока",
                        null=True,
                        upload_to="",
                        verbose_name="Превью для урока",
                    ),
                ),
                (
                    "video",
                    models.FileField(
                        blank=True,
                        help_text="Загрузите видео урока",
                        null=True,
                        upload_to="video/",
                        verbose_name="Видео урока",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]
