from rest_framework import viewsets

from users.permissions import IsModerator, IsOwner
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        course = serializer.save(owner=self.request.user)
        course.save()

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
