from rest_framework import serializers

from .models import Course
from lesson.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'count_lessons', 'lessons', 'owner', )

    @staticmethod
    def get_count_lessons(obj):
        return obj.lessons.count()
