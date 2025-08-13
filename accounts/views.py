from django.contrib.auth import get_user_model
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from accounts.serializers import UserSerializer, RegisterSerializer

# Create your views here.

User = get_user_model()


class AccountListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_agent']
    permission_classes = [IsAdminUser]


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
