from rest_framework import serializers

from lesson.serializers import LessonSerializer
from subscription.models import Subscription

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    is_subscribe = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'price', 'description', 'count_lessons', 'lessons', 'owner', 'is_subscribe')

    @staticmethod
    def get_count_lessons(obj):
        return obj.lessons.count()

    def get_is_subscribe(self, obj):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user, course=obj).exists()
