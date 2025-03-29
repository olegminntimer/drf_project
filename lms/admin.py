from django.contrib import admin

from lms.models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "preview", "video", "course")
