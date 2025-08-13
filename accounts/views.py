from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets, generics

from accounts.serializers import UserSerializer, RegisterSerializer

# Create your views here.

User = get_user_model()


class AccountsAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
