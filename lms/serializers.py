from rest_framework import serializers

from lms.models import Course, Lesson
from lms.validators import validate_allowed_sites
from users.models import Subscription


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    count_lesson = serializers.SerializerMethodField()
    user_subs = serializers.SerializerMethodField()
    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    def get_count_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_user_subs(self, course):
        # user = validated_data.context['context'].user.pk
        # course = validated_data['course']
        user = self.context['request'].user
        return Subscription.objects.filter(user=user, course=course).exists()

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
