from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    PaymentViewSet,
    RemunerationCreateAPIView,
    SubscriptionAPIView,
    UserCreateAPIView,
)

app_name = UsersConfig.name

router = DefaultRouter()
router.register("payment", PaymentViewSet)

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("subscription/", SubscriptionAPIView.as_view(), name="subscription"),
    path("remunerations/", RemunerationCreateAPIView.as_view(), name="remunerations"),
]

urlpatterns += router.urls
