from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    lessons = SerializerMethodField()

    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = Lesson
        fields = "__all__"

class LessonDetailSerializer(ModelSerializer):
    count_lesson = SerializerMethodField()
    course = CourseSerializer()

    def get_count_lesson(self, obj):
        return Lesson.objects.filter(course=obj.course).count()

    class Meta:
        model = Lesson
        fields = ("name", "description", "preview", "video", "course", "count_lesson")
