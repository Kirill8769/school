from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView

from .apps import UsersConfig
from users import views

app_name = UsersConfig.name

urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='user_list'),
    path('create/', views.UserCreateAPIView.as_view(), name='user_create'),
    path('detail/<int:pk>/', views.UserRetrieveAPIView.as_view(), name='user_detail'),
    path('update/<int:pk>/', views.UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', views.UserDestroyAPIView.as_view(), name='user_delete'),
    path('token/', views.TokenCreateView.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=[AllowAny]), name='token_refresh'),
    path('payments/', views.PaymentListAPIView.as_view(), name='payment_list')
]
