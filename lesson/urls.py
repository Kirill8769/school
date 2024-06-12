from django.urls import path

from lesson import views

from .apps import LessonConfig

app_name = LessonConfig.name

urlpatterns = [
    path('', views.LessonListAPIView.as_view(), name='lesson_list'),
    path('create/', views.LessonCreateAPIView.as_view(), name='lesson_create'),
    path('detail/<int:pk>/', views.LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('update/<int:pk>/', views.LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('delete/<int:pk>/', views.LessonDestroyAPIView.as_view(), name='lesson_delete'),
]
