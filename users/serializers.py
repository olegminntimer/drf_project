from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from lms.serializers import CourseSerializer
from users.models import Payment, User, Subscription


class PaymentSerializer(ModelSerializer):
    course_paid = CourseSerializer()

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.exists()

    class Meta:
        model = Subscription
        fields = ("user", "course", "status")
