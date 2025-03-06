from rest_framework.serializers import ModelSerializer

from lms.serializers import CourseSerializer
from users.models import Payment


class PaymentSerializer(ModelSerializer):
    course_paid = CourseSerializer()

    class Meta:
        model = Payment
        fields = "__all__"
