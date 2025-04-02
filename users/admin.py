from django.contrib import admin

from lms.models import Course
from users.models import User, Payment, Subscription


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "last_login", "email", "phone", "city", "avatar")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date",
        "course_paid",
        "lesson_paid",
        "amount",
        "payment_method",
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "course")
