from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, get_object_or_404

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
        print(self.request.data.get("course"))
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "Вы отписались от обновления курса"

        else:
            subs_item = Subscription.objects.create(user=user, course=course_item)
            message = "Вы подписались на обновления курса"
        return Response({"message": message})


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
