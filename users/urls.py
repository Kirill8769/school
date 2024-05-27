from django.urls import path

from .apps import UsersConfig
from users import views

app_name = UsersConfig.name

urlpatterns = [
    path('', views.PaymentListAPIView.as_view(), name='payment_list')
]
