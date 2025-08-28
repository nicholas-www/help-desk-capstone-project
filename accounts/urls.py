from django.urls import path

from accounts import views

urlpatterns = [
    path('register/customer/', views.CustomerRegistrationAPIView.as_view(), name='register-customer'),
    path('register/agent/', views.AgentRegistrationAPIView.as_view(), name='register-agent'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('accounts/', views.AccountListAPIView.as_view(), name='accounts'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),

    path('token/', views.CustomAuthTokenView.as_view(), name='api_token_auth')
]

