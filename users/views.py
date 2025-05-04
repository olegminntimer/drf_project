from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

from lms.models import Course
from users.models import Payment, User, Subscription, Remuneration
from users.serializers import (
    PaymentSerializer,
    UserSerializer,
    SubscriptionSerializer,
    RemunerationSerializer,
)
from users.services import (
    convert_rub_to_usd,
    create_stripe_price,
    create_stripe_session,
    create_stripe_product,
)


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["course_paid", "lesson_paid", "payment_method"]
    ordering_fields = [
        "data",
    ]


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")

        if not course_id:
            return Response({'error': 'Course ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        # Логика подписки/отписки
        subscription, created = Subscription.objects.get_or_create(
            user=user,
            course=course
        )

        if created:
            return Response(
                {'message': 'Вы подписались на обновления курса'},
                status=status.HTTP_201_CREATED
            )
        else:
            subscription.delete()
            return Response(
                {'message': 'Вы отписались от обновления курса'},
                status=status.HTTP_200_OK
            )


class RemunerationCreateAPIView(CreateAPIView):
    serializer_class = RemunerationSerializer
    queryset = Remuneration.objects.all()

    def perform_create(self, serializer):
        remuneration = serializer.save(user=self.request.user)
        amount_in_dollars = convert_rub_to_usd(remuneration.amount)
        product = create_stripe_product(product_name="Course")
        price = create_stripe_price(product["name"], amount_in_dollars)
        session_id, remuneration_link = create_stripe_session(price)
        remuneration.session_id = session_id
        remuneration.link = remuneration_link
        remuneration.save()
