from django.urls import path

from subscription import views
from subscription.apps import SubscriptionConfig

app_name = SubscriptionConfig.name

urlpatterns = [
    path('', views.SubscriptionAPIView.as_view(), name='subscription')
]
