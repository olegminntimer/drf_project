from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import PaymentViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register("payment", PaymentViewSet)

urlpatterns = [

]

urlpatterns += router.urls