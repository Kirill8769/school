from rest_framework import serializers

from .models import Lesson
from .validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='url')]
