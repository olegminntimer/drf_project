from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import (CourseViewSet, LessonCreateAPIView,
                       LessonDestroyAPIView, LessonListAPIView,
                       LessonRetrieveAPIView, LessonUpdateAPIView)

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)


urlpatterns = [
    path("course/", LessonListAPIView.as_view(), name="course_list"),
    path("course/<int:pk>/", LessonRetrieveAPIView.as_view(), name="course_retrieve"),
    path("course/create/", LessonCreateAPIView.as_view(), name="course_create"),
    path(
        "course/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="course_update"
    ),
    path(
        "course/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="course_delete"
    ),
]

urlpatterns += router.urls
