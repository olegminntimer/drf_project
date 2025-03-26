from rest_framework.serializers import ModelSerializer

from lms.serializers import CourseSerializer
from users.models import Payment, User


class PaymentSerializer(ModelSerializer):
    course_paid = CourseSerializer()

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
