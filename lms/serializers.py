from rest_framework import serializers

from lms.models import Course, Lesson
from lms.validators import validate_allowed_sites


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    count_lesson = serializers.SerializerMethodField()

    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    def get_count_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    name = serializers.CharField(validators=[validate_allowed_sites])

    class Meta:
        model = Lesson
        fields = "__all__"


class LessonDetailSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = "__all__"
