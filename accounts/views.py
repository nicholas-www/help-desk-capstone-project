from django.contrib.auth import get_user_model, login
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from accounts.serializers import UserSerializer, RegisterSerializer, LoginSerializer

# Create your views here.

User = get_user_model()


class AccountListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_agent']
    permission_classes = [IsAuthenticated, IsAdminUser]


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        login(request, user)

        return Response({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }, status=status.HTTP_200_OK)
