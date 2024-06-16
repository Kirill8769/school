from django.urls import path

from amount import views

from .apps import AmountConfig

app_name = AmountConfig.name

urlpatterns = [
    path('', views.AmountListAPIView.as_view(), name='amount_list'),
    path('create/', views.AmountCreateAPIView.as_view(), name='amount_create'),
    path('detail/<int:pk>/', views.AmountRetrieveAPIView.as_view(), name='amount_detail'),
    path('update/<int:pk>/', views.AmountUpdateAPIView.as_view(), name='amount_update'),
    path('delete/<int:pk>/', views.AmountDestroyAPIView.as_view(), name='amount_delete'),
    path('success/', views.SuccessTemplateView.as_view(), name='success'),
]
