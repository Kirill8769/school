from rest_framework.routers import DefaultRouter

from .apps import CourseConfig
from .views import CourseViewSet

app_name = CourseConfig.name

router = DefaultRouter()
router.register('', CourseViewSet, basename='course')

urlpatterns = [

]

urlpatterns += router.urls
