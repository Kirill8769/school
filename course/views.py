from rest_framework import viewsets

from subscription.models import Subscription
from users.permissions import IsModerator, IsOwner

from .models import Course
from .paginators import CoursePagination
from .serializers import CourseSerializer
from .tasks import send_course_changes


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePagination

    def perform_create(self, serializer):
        course = serializer.save(owner=self.request.user)
        course.save()

    def perform_update(self, serializer):
        course = serializer.save(owner=self.request.user)
        course.save()
        if self.action in ['update', 'partial_update']:
            subscriptions = Subscription.objects.filter(course=course)
            if subscriptions:
                for subscription in subscriptions:
                    send_course_changes.delay(
                        subject=f'Курс {course.title} был обновлён',
                        message='Информация в материалах курса была обновлена, пожалуйста ознакомьтесь с изменениями.',
                        email=subscription.user.email,
                    )

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='moderator').exists():
            return Course.objects.all()
        return Course.objects.filter(owner=user)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [~IsModerator]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            self.permission_classes = [IsModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwner]
        return super().get_permissions()
