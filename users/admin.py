from django.contrib import admin

from users.models import Payment, Subscription, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "last_login", "email", "phone", "city", "avatar")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date",
        "paid_course",
        # "paid_lesson",
        "amount",
        "payment_method",
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "course")
