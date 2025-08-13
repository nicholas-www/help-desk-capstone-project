from django.urls import path
from rest_framework.routers import DefaultRouter

from accounts import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('accounts/', views.AccountListAPIView.as_view(), name='accounts')
]

