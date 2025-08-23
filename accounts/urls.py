from django.urls import path

from accounts import views

urlpatterns = [
    path('register/customer/', views.CustomerRegistrationAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('accounts/', views.AccountListAPIView.as_view(), name='accounts')
]

